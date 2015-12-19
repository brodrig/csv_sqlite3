# file name
CSV_FILE = "New_York_City_Population_By_Community_Districts.csv"

# app strings
MAIN = "__main__"
RU = "rU"
ERROR = "Error: {}\n"
KEY_ERROR = "Key Error: {}\n"
SQLITE3_ERROR = "Sqlite3 Error: {}\n"
SQLITE3_OPERATIONAL_ERROR = "Sqlite3 Operational Error: {}\n"
IO_ERROR = "IO Error: {}\n"

# database strings
DATABASE = "nyc_population.db"

DROP_TABLE_IF_EXISTS = "drop table if exists "

CD_TABLE_NAME = "nyc_community_districts"

CD_TABLE_FIELDS = "borough, district_number, district_name, population1970, population1980, " \
                  "population1990, population2000, population2010"

CREATE_TABLE = '''CREATE TABLE ''' + CD_TABLE_NAME + '''
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        borough TEXT,
                        district_number INT,
                        district_name TEXT,
                        population1970 INT,
                        population1980 INT,
                        population1990 INT,
                        population2000 INT,
                        population2010 INT
                        )'''

INSERT = "INSERT INTO {} ({}) VALUES {};"

SELECT_ALL = "SELECT * FROM " + CD_TABLE_NAME
