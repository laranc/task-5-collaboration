# datahandler.py
import os
import json
import sqlite3 as sql
import tools.database as db
import tools.user as u


def create_datafile(year: str) -> None:
    # filepath = os.path.join(os.curdir, f"/json/{year}.json")
    # print(filepath)
    # assuming that file doesent exist, based on prequisites for function call:
    try:
        datafile_primary = open(f"./json/{year}.json", 'w')
    except:
        print("Couldnt make file!")
    
def new_data_entry():
    pass

def pull_data(year: str) -> list[str]:
    if os.stat(f"./json/{year}.json").st_size == 0:
        return []
    else:
        datafile_primary = open(f"./json/{year}.json", 'r')
        data = json.load(datafile_primary)
        month = data['month']
        user_id = data['user-id']
        total_expenses = data['total-monthly-expenses']
        total_income = data['total-monthly-income']
        local_expenses = {}
        local_incomes = {}
        for expense_name in data['expenses']:
            local_expenses[f"{expense_name}"] = data['expenses'][expense_name]
        for income_name in data['incomes']:
            local_incomes[f"{income_name}"] = data['incomes'][income_name]

        print(local_expenses)
        print(local_incomes)

        data_out: list[str] = [str(month), str(user_id), str(total_expenses), str(total_income), local_expenses, local_incomes]
        return data_out

def push_data() -> None:
    pass

def push_new_data(time_data: list[str]) -> None:
    # create db connection
    conn = db.connect_to_database("user_data.db")
    cursor = db.create_database_cursor(conn)

    # get database data
    cursor.execute("SELECT * FROM UserData")
    db_data = cursor.fetchall()

    # collect time data

    json_expenses = []
    json_incomes = []

    # essentially the schmatic for what will be reresented in the json
    # i.e :


    # {

    # construct dictionary
    json_entry = { # need to add expense data here?
        "userid": f"",
        "totalmonthexpenses": f"",
        "totalmonthincome": f"",
        "expenses": f"{json_expenses}", # this wont push as expected!!!
        "incomes": f"{json_incomes}",
    }

    # } 