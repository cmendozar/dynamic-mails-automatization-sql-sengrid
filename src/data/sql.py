import time
import pandas as pd 
import pymssql
import os

class SQL:
    """ 
    SQL_SERVER OBJECT: Create a SQL Server connection 
    to use functionality of SQL in python.
    """
    def __connection(self):
        return pymssql.connect(self.server,self.user,self.password,self.database)

    def __init__(self,database):
        self.server     = os.environ.get('SERVER')
        self.user       = os.environ.get('USER')
        self.password   = os.environ.get('PASSWORD')
        self.database   = database
        self.connection = self.__connection()
        
    def get_query(self,file):
        """
        Return a List with the rows of data
        """
        conn = self.connection
        cursor = conn.cursor()
        with open(file) as sql_file:
            query = sql_file.read()
        cursor.execute(query)
        data = []
        for row in cursor: 
            data = data.append(row)
        conn.close()
        return data

    def get_query_df(self,file):
        """
        Return a DataFrame Object with the queried data.
        """
        conn = self.connection
        start = time.time()
        with open(file) as sql_file:
            query = sql_file.read()
        print("Query starting..")
        df = pd.read_sql(query,conn)
        end = time.time()
        print("Finished Query: elapsed query time of {} secs".format(round(end-start,1)))
        df = pd.DataFrame(df)
        return df 

if __name__ == '__main__':
    Table = SQL('YOUR_ODS')
    file_path = os.path.dirname(os.path.abspath(__file__)) + '/query.sql'
    data = Table.get_query_df(file = file_path)
    print(data.head())

