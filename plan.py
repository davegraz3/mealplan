import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

sql_host = os.getenv('sql_host')
sql_user = os.getenv('sql_user')
sql_pw = os.getenv('sql_password')
sql_database = os.getenv('sql_database')

def create_meal_plan(max_calories):
    conn = mysql.connector.connect(
        host = sql_host,
        user = sql_user,
        password = sql_pw,
        database = sql_database
        )
    cursor = conn.cursor()

    meal_plan = []

    for meal_type in ['breakfast', 'lunch', 'dinner']:
        cursor.execute(f"SELECT * FROM {meal_type} ORDER BY RAND() LIMIT 1")
        meal = cursor.fetchone()

        if meal is not None and meal[2] <= max_calories:
            meal_plan.append(meal[1])
            max_calories -= meal[2]

    for meal_type in meal_plan:
        print(meal_type)
    conn.close()

create_meal_plan(2000) # 2000 is the max calories for the day
