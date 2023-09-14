import sqlite3


class local_sql:
    """creates a local db file

    create_db_with_columns()
    -----
            CREATE TABLE IF NOT EXISTS 'table'
            >>> from TOOLS.File_Handler import local_sql
            >>> db = local_sql()
            >>> db.create_db_with_columns(dbname="test.db",table="ppl", {"FIRST_NAME": "TEXT"},{"SECOND_NAME": "TEXT"},{"AGE": "INTEGER"}, {"place": "TEXT"},{"country": "TEXT"})"

    -----
    insert_into_db()
    -----
            INSERT INTO 'table' VALUES (args)
            >>> from TOOLS.File_Handler import local_sql
            >>> db = local_sql()
            >>> db.insert_into_db(dbfilename="dbfilename.db", table="table", {'name': 'type'}, {'name': 'type'})

    -----
    find_into_db()
    -----
            SELECT * FROM 'table' WHERE {command}
            >>> from TOOLS.File_Handler import local_sql
            >>> db = local_sql()
            >>> print(db.find_into_db(dbfilename="dbfilename.db", table="table", command="first_name='NOOR'"))
            >>> print(db.find_into_db(dbfilename="dbfilename.db", table="table", command="name='NooR' AND second_name='MaseR' AND email='NOOR@example.com'"))

    -----
    find_one_into_db()
    -----
            SELECT 'column_name' FROM 'table' WHERE {where}
            >>> from TOOLS.File_Handler import local_sql
            >>> db = local_sql()
            >>> print(db.find_one_into_db(dbfilename="dbfilename.db", table="table", column_name="owner", where="first_name='NOOR'"))
            >>> print(db.find_one_into_db(dbfilename="dbfilename.db", table="table", column_name="owner", where="email='NOOR@example.com' AND place='EGYPT'"))

    -----
    Get_db_data()
    -----
            SELECT * FROM 'table'
            >>> from TOOLS.File_Handler import local_sql
            >>> db = local_sql()
            >>> print(db.Get_db_data("dbfilename=dbfilename.db", table="table"))

    -----
    Update_db_data()
    -----
            SELECT * FROM 'table'
            >>> from TOOLS.File_Handler import local_sql
            >>> db = local_sql()
            >>> db.Update_db_data(dbfilename="dbfilename.db", table="table", update_command="Name='ali', email='MaseR@example.org', phone='20*********'", where="ID='**********' AND country='EGYPT'")
    """

    def __init__(self) -> None:
        self._sql_command: str

    def create_db_with_columns(self, dbfilename: str, table: str, *args: dict) -> None:
        """
        CREATE TABLE IF NOT EXISTS 'table'
        >>> from TOOLS.File_Handler import local_sql
        >>> db = local_sql()
        >>> db.create_db_with_columns(dbfilename="test.db",table="ppl", {"FIRST_NAME": "TEXT"},{"SECOND_NAME": "TEXT"},{"AGE": "INTEGER"}, {"place": "TEXT"},{"country": "TEXT"})
        """
        count = 0
        if dbfilename.endswith(".db"):
            try:
                for k, v in args[0].items():
                    global first_column_name, first_column_type
                    first_column_name = k
                    first_column_type = v.upper()
            except:
                raise ValueError(
                    "no coulmns has been provided, please make sure to type the columns like {'name':'type'}, *args"
                )
            connect = sqlite3.connect(f"{dbfilename}")
            c = connect.cursor()
            c.execute(
                f"CREATE TABLE IF NOT EXISTS '{table}' ({first_column_name} {first_column_type.upper()})"
            )
            self._sql_command = f"CREATE TABLE IF NOT EXISTS '{table}' ({first_column_name} {first_column_type.upper()})"
            for i in args:
                for k, v in i.items():
                    try:
                        # Get the columns info
                        c.execute(f"PRAGMA table_info({table})")
                        connect.commit()
                        result = c.fetchall()
                        print(result)
                        if k == result[count][1]:
                            print(f"{k} is already exist")
                        count += 1
                        # print(result)
                    except:
                        for k, v in i.items():
                            c.execute(f"PRAGMA table_info({table})")
                            connect.commit()
                            result = c.fetchall()
                            count += 1
                            c.execute(f"ALTER TABLE {table} ADD COLUMN {k} {v}")
                        continue
                    finally:
                        continue
            connect.commit()
            connect.close()
        else:
            raise TypeError(f"the [{dbfilename}] does not end with .db Extention")

    def insert_into_db(
        self, dbfilename: str, table: str, *args: str | int | float
    ) -> None:
        """
        INSERT INTO 'table' VALUES (args)
        >>> from TOOLS.File_Handler import local_sql
        >>> db = local_sql()
        >>> db.insert_into_db(dbfilename="dbfilename.db", table="table", 'NooR', "MaseR", 'EGYPT')
        """
        if dbfilename.endswith(".db"):
            connect = sqlite3.connect(f"{dbfilename}")
            c = connect.cursor()
            insert = f"INSERT INTO '{table}' VALUES"
            data = tuple(data for data in args)
            c.execute(f"{insert}{data}")
            connect.commit()
            connect.close()
            self._sql_command = f"{insert}{data}"
        else:
            raise TypeError(f"the [{dbfilename}] does not end with .db Extention")

    def find_into_db(self, dbfilename: str, table: str, where: str) -> list:
        """
        SELECT * FROM 'table' WHERE {where}
        >>> from TOOLS.File_Handler import local_sql
        >>> db = local_sql()
        >>> db.find_into_db(dbfilename="dbfilename.db", table="table", where="first_name='NOOR'")
        >>> db.find_into_db(dbfilename="dbfilename.db", table="table", where="name='NooR' AND second_name='MaseR' AND email='NOOR@example.com'")
        >>> db.find_into_db(dbfilename="dbfilename.db", table="table", where="name like'NooR' AND second_name like 'MaseR' AND email like 'NOOR@example.com'")
        """
        if dbfilename.endswith(".db"):
            connect = sqlite3.connect(f"{dbfilename}")
            c = connect.cursor()
            c.execute(f"SELECT * FROM '{table}' WHERE {where}")
            result = c.fetchall()
            connect.commit()
            connect.close()
            self._sql_command = f"SELECT * FROM '{table}' WHERE {where}"
            return result
        else:
            raise TypeError(f"the [{dbfilename}] does not end with .db Extention")

    def find_col_into_db(
        self, dbfilename: str, table: str, column_name: str, command: str
    ) -> list:
        """
        SELECT 'column_name' FROM 'table' WHERE {command}
        >>> from TOOLS.File_Handler import local_sql
        >>> db = local_sql()
        >>> db.find_one_into_db(dbfilename="dbfilename.db", table="table", column_name="owner", command="first_name='NOOR'")
        >>> db.find_one_into_db(dbfilename="dbfilename.db", table="table", column_name="owner", command="email='NOOR@example.com' AND place='EGYPT'")
        """
        if dbfilename.endswith(".db"):
            connect = sqlite3.connect(f"{dbfilename}")
            c = connect.cursor()
            c.execute(f"SELECT {column_name} FROM '{table}' WHERE {command}")
            result = c.fetchall()
            connect.commit()
            connect.close()
            self._sql_command = f"SELECT {column_name} FROM '{table}' WHERE {command}"
            return result
        else:
            raise TypeError(f"the [{dbfilename}] does not end with .db Extention")

    def Get_db_data(self, dbfilename: str, table: str) -> list:
        """
        SELECT * FROM 'table'
        >>> from TOOLS.File_Handler import local_sql
        >>> db = local_sql()
        >>> print(db.Get_db_data(dbfilename="dbfilename.db", table="table"))
        """
        if dbfilename.endswith(".db"):
            connect = sqlite3.connect(f"{dbfilename}")
            c = connect.cursor()
            c.execute(f"SELECT * FROM '{table}'")
            result = c.fetchall()
            connect.commit()
            connect.close()
            self._sql_command = f"SELECT * FROM '{table}'"
            return result
        else:
            raise TypeError(f"the [{dbfilename}] does not end with .db Extention")

    def Update_db_data(
        self, dbfilename: str, table: str, update_command: str, where: str
    ) -> None:
        """
        SELECT * FROM 'table'
        >>> from TOOLS.File_Handler import local_sql
        >>> db = local_sql()
        >>> db.Update_db_data(dbfilename="dbfilename.db", table="table", update_command="Name='ali', email='MaseR@example.org', phone='20*********'", where="ID='**********' AND country='EGYPT'")
        """
        if dbfilename.endswith(".db"):
            connect = sqlite3.connect(f"{dbfilename}")
            c = connect.cursor()
            c.execute(f"UPDATE '{table}' SET {update_command} WHERE {where}")
            connect.commit()
            connect.close()
            self._sql_command = f"UPDATE '{table}' SET {update_command} WHERE {where}"
        else:
            raise TypeError(f"the [{dbfilename}] does not end with .db Extention")

    def Delete_from_db(self, dbfilename: str, table: str, where: str):
        """
        DELETE FROM 'table' WHERE
        >>> from TOOLS.File_Handler import local_sql
        >>> db = local_sql()
        >>> db.Delete_from_db(dbfilename="dbfilename.db", table="table", where="EMAIL='exam@example.or' AND PASSWORD ='123456789' AND PHONE='+1*******")
        """
        if dbfilename.endswith(".db"):
            connect = sqlite3.connect(f"{dbfilename}")
            c = connect.cursor()
            c.execute(f"DELETE FROM '{table}' WHERE {where}")
            connect.commit()
            connect.close()
            self._sql_command = f"DELETE FROM '{table}' WHERE {where}"
        else:
            raise TypeError(f"the [{dbfilename}] does not end with .db Extention")