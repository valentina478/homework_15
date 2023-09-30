import sqlite3
import random

with sqlite3.connect('homework_2_15\\users.db') as db: 
    cr = db.cursor()
    cr.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT
        )
    ''')

    cr.execute('''
        SELECT name FROM users
        WHERE email LIKE '%gmail.com'
    ''')

with sqlite3.connect('homework_2_14\\toys.db') as db: # Підключилася до бази даних з минулого дз, щоб не створювати нову
    cr = db.cursor()
    cr.execute('''
        SELECT * FROM toys
        ORDER BY price
    ''')

    cr.execute('''
        SELECT AVG(price) FROM toys
    ''')

    cr.execute('''
        SELECT MAX(price) FROM toys
    ''')

    cr.execute('''
        SELECT MIN(stock_quantity) FROM toys
    ''')

    cr.execute('''
        SELECT name, price,
            CASE 
               WHEN price < 10 THEN 'Економний'
               WHEN price >= 10 AND price < 20 THEN 'Середній'
               WHEN price >= 20 AND price < 30 THEN 'Високий'
               ELSE 'Дуже високий'
            END AS price_category
        FROM toys
    ''')

    cr.execute('''
        SELECT name, stock_quantity,
            CASE 
                WHEN stock_quantity >= 50 THEN 'знижка 10%'
                WHEN stock_quantity >= 20 AND stock_quantity < 50 THEN 'знижка 5%'
                ELSE 'без знижки'
            END AS discount
        FROM toys
    ''')