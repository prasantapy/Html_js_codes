import csv
import os
from datetime import date

FILE_NAME = "data.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Name", "Lunch", "Dinner"])

def add_meal():
    today = date.today()
    name = input("Enter Name: ").strip()

    lunch = input("Lunch (P/A): ").upper()
    dinner = input("Dinner (P/A): ").upper()

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([today, name, lunch, dinner])

    print("✅ Meal entry added successfully")

def view_all():
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def view_by_name():
    search = input("Enter Name: ").strip().lower()
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1].lower() == search:
                print(row)
                found = True

    if not found:
        print("❌ No record found")

def view_by_date():
    search_date = input("Enter date (YYYY-MM-DD): ")

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == search_date:
                print(row)

def menu():
    while True:
        print("\n===== MEALS MANAGEMENT SYSTEM =====")
        print("1. Add Meal Entry")
        print("2. View All Records")
        print("3. View By Name")
        print("4. View By Date")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_meal()
        elif choice == "2":
            view_all()
        elif choice == "3":
            view_by_name()
        elif choice == "4":
            view_by_date()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")

create_file()
menu()
