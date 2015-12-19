import sqlite3
import csv
import strings


def db_conn():
    """
    Connect to db and return the connection and cursor
    """
    try:
        conn = sqlite3.connect(strings.DATABASE)
        conn.row_factory = sqlite3.Row  # fetch rows as dictionaries
        cur = conn.cursor()
        return cur, conn
    except sqlite3.Error, e:
        print strings.SQLITE3_ERROR.format(e.args[0])
        exit(1)


def read_csv(csv_file):
    """
    Read in CSV file in the form of dictionaries and yield (evaluate lazily) data
    @param csv_file          csv file
    """
    try:
        with open(csv_file, strings.RU) as data:
            record_set = csv.DictReader(data)
            for row in record_set:
                yield row
    except IOError, e:
        print strings.IO_ERROR.format(e.strerror), strings.IO_ERROR.format(e)
        exit(1)


def insert_data():
    """
    Insert each dictionary returned by the read_csv() generator
    """
    cr, cn = db_conn()
    try:
        cr.execute(strings.DROP_TABLE_IF_EXISTS + strings.CD_TABLE_NAME)
        cr.execute(strings.CREATE_TABLE)
        for d in iter(read_csv(strings.CSV_FILE)):
            # Build SQL statement for each dictionary and execute
            query = strings.INSERT.format(
                        strings.CD_TABLE_NAME,
                        strings.CD_TABLE_FIELDS,
                        (d['Borough'], d['CD Number'], d['CD Name'],
                         d['1970 Population'], d['1980 Population'], d['1990 Population'],
                         d['2000 Population'], d['2010 Population']))
            cr.execute(query)
        cn.commit()
        cr.close()
        cn.close()
    except sqlite3.Error, e:
        if cn:
            cn.rollback()
        print strings.SQLITE3_ERROR.format(e.args[0])
        exit(1)
    except KeyError, e:
        if cn:
            cn.rollback()
        print strings.KEY_ERROR.format(e.args[0])
        exit(1)
    finally:
        if cn:
            cn.close()


def retrieve_data():
    """
    Retrieve one record at a time and print to console
    """
    cr, cn = db_conn()
    try:
        cr.execute(strings.SELECT_ALL)
        with cn:
            while True:
                row = cr.fetchone()
                if row is None:
                    break
                # fetch data as tuples (default)
                print row
                # fetch specific columns using dictionary cursor set on line 12
                # print row['borough'], row['district_number'], row['district_name']
    except sqlite3.OperationalError, e:
        if cn:
            cn.rollback()
        print strings.SQLITE3_OPERATIONAL_ERROR.format(e.args[0])
        exit(1)


def main():
    # insert records from csv file
    insert_data()
    # query db and print to console
    retrieve_data()


if __name__ == strings.MAIN:
    main()
