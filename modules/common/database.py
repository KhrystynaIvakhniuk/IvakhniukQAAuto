import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(
            r"C:\\Users\\user\\IvakhniukQAAuto" + r"\\become_qa_auto.db"
        )
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        querty = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(querty)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        querty = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(querty)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
                VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_new_user(self, customer_id, name, address, city, postal_code, county):
        querty = f"INSERT OR REPLACE INTO customers \
                (id, name, address, city, postalCode, country) \
                VALUES ({customer_id}, '{name}', '{address}', '{city}', '{postal_code}', '{county}')"
        self.cursor.execute(querty)
        self.connection.commit()

    def get_user_by_id(self, customer_id):
        querty = f"SELECT name, address, city, postalCode, country \
                FROM customers WHERE id = {customer_id}"
        self.cursor.execute(querty)
        record = self.cursor.fetchall()
        return record
    
    def get_product_by_id(self, product_id):
        querty = f"SELECT name, description, quantity \
                FROM products WHERE id = {product_id}"
        self.cursor.execute(querty)
        record = self.cursor.fetchall()
        return record
    
    def update_user_address_by_name(self, name, address, city, postal_code, country):
        querty = f"UPDATE customers \
                SET address = '{address}', city = '{city}', postalCode = '{postal_code}', country = '{country}' \
                WHERE name = '{name}'"
        self.cursor.execute(querty)
        self.connection.commit()


    def add_new_order(self, order_id, customer_id, product_id, date):
        query = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) \
                VALUES ({order_id}, '{customer_id}', '{product_id}', '{date}')"
        self.cursor.execute(query)
        self.connection.commit()
    
