import psycopg2

db_params = { 'dbname' : 'new_db',
              'password' : '123',
              'host' : 'localhost',
              'port' : 5432,
              'user' : 'postgres'}

conn = psycopg2.connect(**db_params)

class ConnectDB:
    def __init__(self,db_params: dict):
        self.db_params = db_params

    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_params)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
        if self.conn:
            self.cursor.close()
            self.conn.close()

    def commit(self):
        self.conn.commit()

class Product:
    def __init__(self,product_name: str):
        self.product_name = product_name

    def save_product(self):
        with ConnectDB(db_params) as db:
            create_table = """create table self.product_name (
            
            id serial primary key,
            product_name varchar (250)
            );"""

product = Product('Telefon')
product.save_product()





