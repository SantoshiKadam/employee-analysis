import csv
from functools import reduce
import matplotlib.pyplot as plt
import os

# Load CSV file and clean whitespace
def load_csv(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Error: File not found -> {file_path}")
        return []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [{k.strip(): v.strip() for k, v in row.items()} for row in reader]

# Display all employees
def display_employees(data):
    print("\n--- All Employees ---")
    for emp in data:
        print(emp)

# Filter employees by designation (case-insensitive)
def filter_by_designation(data, designation='Manager'):
    return list(filter(lambda e: e['Designation'].lower() == designation.lower(), data))

# Convert Salary to int safely
def get_salary(emp):
    try:
        return int(emp['Salary'])
    except:
        return 0

# Sort employees by salary
def sort_by_salary(data, descending=True):
    return sorted(data, key=get_salary, reverse=descending)

# Calculate total and average salary
def total_and_average_salary(data):
    total = sum(get_salary(e) for e in data)
    average = total / len(data) if data else 0
    return total, average

# Plot salary distribution
def plot_salaries(data):
    names = [e['Name'] for e in data]
    salaries = [get_salary(e) for e in data]
    plt.bar(names, salaries, color='green')
    plt.xlabel('Employee Name')
    plt.ylabel('Salary')
    plt.title('Employee Salary Distribution')
    plt.tight_layout()
    plt.show()

# Menu-driven CLI
def run_menu(file_path):
    employees = load_csv(file_path)
    if not employees:
        return  # Exit if file not found or empty

    while True:
        print("\n==== EMPLOYEE DATA ANALYSIS MENU ====")
        print("1. Show all employees")
        print("2. Filter by Designation (Manager)")
        print("3. Sort by Salary (High to Low)")
        print("4. Total and Average Salary")
        print("5. Show Graph: Salary Distribution")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        if choice == '1':
            display_employees(employees)
        elif choice == '2':
            filtered = filter_by_designation(employees)
            display_employees(filtered)
        elif choice == '3':
            sorted_employees = sort_by_salary(employees)
            display_employees(sorted_employees)
        elif choice == '4':
            total, average = total_and_average_salary(employees)
            print(f"\nTotal Salary: {total}, Average Salary: {average:.2f}")
        elif choice == '5':
            plot_salaries(employees)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# ✅ Use the correct path to your data.csv file
run_menu('D:/fastapi_crud/assignment1/data.csv')
