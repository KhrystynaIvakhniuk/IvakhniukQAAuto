import pytest
import sqlite3
from modules.common.database import Database
from datetime import datetime


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    assert users[0][0] == 'Sergii'
    assert users[1][0] == 'Stepan'


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)
    
    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    new_product_qnt = db.select_product_qnt_by_id(4)

    assert new_product_qnt[0][0] == 30
    

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'
    

@pytest.mark.database
def test_add_new_user():
    db = Database()
    db.insert_new_user(3, 'Khrystyna', 'Shevchenka 2', 'Warsaw', '21466', 'Poland')
    new_user = db.get_user_by_id(3)

    assert new_user[0][0] == 'Khrystyna'
    assert new_user[0][1] == 'Shevchenka 2'
    assert new_user[0][2] == 'Warsaw'
    assert new_user[0][3] == '21466'
    assert new_user[0][4] == 'Poland'



@pytest.mark.database
def test_get_nonexistent_user_by_id():
    db = Database()
    user = db.get_user_by_id(999) 
    assert user == []


@pytest.mark.database
def test_add_product_without_some_information():
    db = Database()
    db.insert_product(5, 'chocolate', '', 0)
    product = db.get_product_by_id(5)

    assert product[0][0] == 'chocolate'
    assert product[0][1] == ''
    assert product[0][2] == 0


@pytest.mark.database
def test_update_user_address_by_name():
    db = Database()
    db.update_user_address_by_name('Stepan', 'Dobra 19', 'Lviv', '56745', 'Ukraine')
    new_address = db.get_user_address_by_name('Stepan')

    assert new_address[0][0] == 'Dobra 19'
    assert new_address[0][1] == 'Lviv'
    assert new_address[0][2] == '56745'
    assert new_address[0][3] == 'Ukraine'


@pytest.mark.database
def test_add_new_order():
    db = Database()
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.add_new_order(2, 2, 3, date)
    order = db.get_detailed_orders()
    print(order)

    assert order[1][0] == 2
    assert order[1][1] == 'Stepan'
    assert order[1][2] == 'молоко'
    assert order[1][3] == 'натуральне незбиране'
