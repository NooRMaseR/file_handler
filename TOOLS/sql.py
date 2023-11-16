import sqlite3


class local_sql:
    """create a local db file with lower and easy code

    create_db_with_columns()
    -----
            CREATE TABLE IF NOT EXISTS 'table'
            >>> from TOOLS.sql import local_sql
            >>> db = local_sql()
            >>> db.create_db_with_columns(dbname="test.db",table="ppl", {"FIRST_NAME": "TEXT"},{"SECOND_NAME": "TEXT"},{"AGE": "INTEGER"}, {"place": "TEXT"},{"country": "TEXT"})"

    -----
    insert_into_db()
    -----
            INSERT INTO 'table' VALUES (args)
            >>> from TOOLS.sql import local_sql
            >>> db = local_sql()
            >>> db.insert_into_db(dbfilename="dbfilename.db", table="table", {'name': 'type'}, {'name': 'type'})

    -----
    find_into_db()
    -----
            SELECT * FROM 'table' 'where'
            >>> from TOOLS.sql import local_sql
            >>> db = local_sql()
            # like=False meens first_name ='NOOR'
            >>> db.find_into_db(dbfilename="dbfilename.db", table="table", like=False, first_name='NOOR')
            >>> db.find_into_db(dbfilename="dbfilename.db", table="table", like=False, name='NooR' , second_name='MaseR' , email='NOOR@example.com')
            # like=True meens first_name like'NOOR'
            >>> db.find_into_db(dbfilename="dbfilename.db", table="table", like=True, name='NooR' , second_name='MaseR' , email='NOOR@example.com')

    -----
    find_one_into_db()
    -----
            SELECT 'column_name' FROM 'table' WHERE {where}
            >>> from TOOLS.sql import local_sql
            >>> db = local_sql()
            >>> print(db.find_one_into_db(dbfilename="dbfilename.db", table="table", column_name="owner", where="first_name='NOOR'"))
            >>> print(db.find_one_into_db(dbfilename="dbfilename.db", table="table", column_name="owner", where="email='NOOR@example.com' AND place='EGYPT'"))

    -----
    Get_db_data()
    -----
            SELECT * FROM 'table'
            >>> from TOOLS.sql import local_sql
            >>> db = local_sql()
            >>> print(db.Get_db_data("dbfilename=dbfilename.db", table="table"))

    -----
    Update_db_data()
    -----
            SELECT * FROM 'table'
            >>> from TOOLS.sql import local_sql
            >>> db = local_sql()
            >>> db.Update_db_data(dbfilename="dbfilename.db", table="table", set_command=({"Name":'ali'}, {"email":'MaseR@example.org'}), {"phone":'20*********'}), ID='**********' , country='EGYPT')
    
    -----
    Delete_from_db()
    -----
            DELETE FROM 'table' WHERE
            >>> from TOOLS.sql import local_sql
            >>> db = local_sql()
            >>> db.Delete_from_db(dbfilename="dbfilename.db", table="table", EMAIL='exam@example.or' , PASSWORD ='123456789' , PHONE='+1*******')
    """

    def __init__(self) -> None:
        self._sql_command: str

    def create_table_if_not(self, dbfilename: str, table: str, *args: dict) -> None:
        "CREATE TABLE IF NOT EXISTS 'table'"
        creation:str = f"CREATE TABLE IF NOT EXISTS {table} ("
        for i in args:
            creation += f"{list(i.keys())[0]} {list(i.values())[0].upper()}, "
        creation = creation.removesuffix(", ")
        creation += ")"
        print(f"{creation = }")
        if dbfilename.endswith(".db"):
            try:
                conn = sqlite3.connect(dbfilename)
                c = conn.cursor()
                c.execute(creation)
                conn.commit()
                conn.close()
            except Exception as e:
                raise Exception(e)
    
    def create_db_with_columns(self, dbfilename: str, table: str, *args: dict) -> None:
        """
        CREATE TABLE IF NOT EXISTS 'table'
        >>> from TOOLS.sql import local_sql
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
                        if k == result[count][1]:
                            pass
                            # print(f"{k} is already exist")
                        count += 1
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

    def insert_into_db(self, dbfilename: str, table: str, *args: str | int | float | bytes) -> None:
        """
        INSERT INTO 'table' VALUES (args)
        >>> from TOOLS.sql import local_sql
        >>> db = local_sql()
        >>> db.insert_into_db(dbfilename="dbfilename.db", table="table", 'NooR', "MaseR", 'EGYPT')
        """
        if dbfilename.endswith(".db"):
            connect = sqlite3.connect(f"{dbfilename}")
            c = connect.cursor()
            data = tuple(data for data in args)
            insert = f"INSERT INTO '{table}' VALUES ({"?," * len(data)})".replace(",)",")")
            self._sql_command = f"{insert}{data}"
            c.execute(f"{insert}",data)
            connect.commit()
            connect.close()
        else:
            raise TypeError(f"the [{dbfilename}] does not end with .db Extention")

    def find_into_db(self, dbfilename: str, table: str, like:bool = False, **where) -> list:
        """
        SELECT * FROM 'table' 'where'
        >>> from TOOLS.sql import local_sql
        >>> db = local_sql()
        # like=False meens first_name ='NOOR'
        >>> db.find_into_db(dbfilename="dbfilename.db", table="table", like=False, first_name='NOOR')
        >>> db.find_into_db(dbfilename="dbfilename.db", table="table", like=False, name='NooR' , second_name='MaseR' , email='NOOR@example.com')
        # like=True meens first_name like'NOOR'
        >>> db.find_into_db(dbfilename="dbfilename.db", table="table", like=True, name='NooR' , second_name='MaseR' , email='NOOR@example.com')
        """
        if dbfilename.endswith(".db"):
            query:str = "WHERE "
            connect = sqlite3.connect(f"{dbfilename}")
            c = connect.cursor()
            for k,v in where.items():
                if like:
                    query += f"{k} like'{v}' AND "
                else:
                    query += f"{k}='{v}' AND "
            query = query.removesuffix(" AND ")
            c.execute(f"SELECT * FROM '{table}' {query}")
            result = c.fetchall()
            connect.commit()
            connect.close()
            self._sql_command = f"SELECT * FROM '{table}' {query}"
            return result
        else:
            raise TypeError(f"the [{dbfilename}] does not end with .db Extention")

    def find_col_into_db(self, dbfilename: str, table: str, column_name: str, command: str) -> list:
        """
        SELECT 'column_name' FROM 'table' WHERE 'command'
        >>> from TOOLS.sql import local_sql
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
        >>> from TOOLS.sql import local_sql
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

    def Update_db_data(self, dbfilename: str, table: str, set_command: tuple | list, **where) -> None:
        """
        Update 'table' 'set_command' **where
        >>> from TOOLS.sql import local_sql
        >>> db = local_sql()
        >>> db.Update_db_data(dbfilename="dbfilename.db", table="table", set_command=({"Name":'ali'}, {"email":'MaseR@example.org'}, {"phone":'20*********'}), ID='**********' , country='EGYPT')
        """
        if dbfilename.endswith(".db"):
            where_query:str = "WHERE "
            where_update:str = "SET  "
            connect = sqlite3.connect(f"{dbfilename}")
            c = connect.cursor()
            for i in set_command:
                for k,v in i.items():
                    where_update += f"{k}='{v}', "
            where_update = where_update.removesuffix(", ")
                
            for k,v in where.items():
                where_query += f"{k}='{v}' AND "
            where_query = where_query.removesuffix(" AND ")
            self._sql_command = f"UPDATE '{table}' {where_update} {where_query}"
            c.execute(f"UPDATE '{table}' {where_update} {where_query}")
            connect.commit()
            connect.close()
        else:
            raise TypeError(f"the [{dbfilename}] does not end with .db Extention")

    def Delete_from_db(self, dbfilename: str, table: str, **where) -> None:
        """
        DELETE FROM 'table' WHERE
        >>> from TOOLS.sql import local_sql
        >>> db = local_sql()
        >>> db.Delete_from_db(dbfilename="dbfilename.db", table="table", EMAIL='exam@example.or' , PASSWORD ='123456789' , PHONE='+1*******')
        """
        if dbfilename.endswith(".db"):
            query:str = "WHERE "
            connect = sqlite3.connect(f"{dbfilename}")
            c = connect.cursor()
            for k,v in where.items():
                query += f"{k}='{v}' AND "
            query = query.removesuffix(" AND ")
            c.execute(f"DELETE FROM '{table}' {query}")
            connect.commit()
            connect.close()
            self._sql_command = f"DELETE FROM '{table}' {query}"
        else:
            raise TypeError(f"the [{dbfilename}] does not end with .db Extention")
