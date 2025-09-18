import json
import os
from models import Income, Expense
from datetime import date

DATA_DIR = "data"
INCOMES_FILE = os.path.join(DATA_DIR, "incomes.json")
EXPENSES_FILE = os.path.join(DATA_DIR, "expenses.json")


def ensure_data_files():
    os.makedirs(DATA_DIR, exist_ok=True)
    for file_path in [INCOMES_FILE, EXPENSES_FILE]:
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump([], f)


def load_incomes():
    with open(INCOMES_FILE, "r") as f:
        data = json.load(f)
        return [Income(**d) for d in data]


def load_expenses():
    with open(EXPENSES_FILE, "r") as f:
        data = json.load(f)
        return [Expense(**d) for d in data]


def save_incomes(incomes_: list[Income]):
    with open(INCOMES_FILE, "w") as f:
        json.dump([income.__dict__ for income in incomes_], f, indent=2)


def save_expenses(expenses_: list[Expense]):
    with open(EXPENSES_FILE, "w") as f:
        json.dump([expense.__dict__ for expense in expenses_], f, indent=2)


# API do użycia w aplikacji
incomes: list[Income] = []
expenses: list[Expense] = []


def initialize_storage():
    ensure_data_files()
    global incomes, expenses
    incomes = load_incomes()
    expenses = load_expenses()


def add_income(income: Income):
    incomes.append(income)
    save_incomes(incomes)


def add_expense(expense: Expense):
    expenses.append(expense)
    save_expenses(expenses)


def get_incomes():
    return incomes


def get_expenses():
    return expenses


def get_recurring_expenses():
    return [e for e in expenses if e.subscription]
