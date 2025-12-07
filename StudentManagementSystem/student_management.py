import csv
import os

FILE_NAME = "students.csv"
FIELDS = ["id", "name", "department", "age"]


def init_file():
    """Create file with header if not exists."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


def add_student():
    print("\n--- Add New Student ---")
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    age = input("Enter Age: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow({
            "id": sid,
            "name": name,
            "department": dept,
            "age": age
        })

    print("✅ Student added successfully!")


def view_students():
    print("\n--- All Students ---")
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        data_found = False
        for row in reader:
            data_found = True
            print(f"ID: {row['id']} | Name: {row['name']} | Dept: {row['department']} | Age: {row['age']}")
        if not data_found:
            print("No records found.")


def search_student():
    print("\n--- Search Student ---")
    search_id = input("Enter Student ID to search: ")
    found = False

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["id"] == search_id:
                print(f"✅ Found: ID: {row['id']} | Name: {row['name']} | Dept: {row['department']} | Age: {row['age']}")
                found = True
                break

    if not found:
        print("❌ No student found with that ID.")


def update_student():
    print("\n--- Update Student ---")
    update_id = input("Enter Student ID to update: ")
    rows = []
    updated = False

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["id"] == update_id:
                print(f"Current Name: {row['name']}, Dept: {row['department']}, Age: {row['age']}")
                row["name"] = input("Enter new Name (leave blank to keep same): ") or row["name"]
                row["department"] = input("Enter new Dept (leave blank to keep same): ") or row["department"]
                row["age"] = input("Enter new Age (leave blank to keep same): ") or row["age"]
                updated = True
            rows.append(row)

    if updated:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        print("✅ Student updated successfully!")
    else:
        print("❌ No student found with that ID.")


def delete_student():
    print("\n--- Delete Student ---")
    del_id = input("Enter Student ID to delete: ")
    rows = []
    deleted = False

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["id"] == del_id:
                deleted = True
                continue
            rows.append(row)

    if deleted:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        print("✅ Student deleted successfully!")
    else:
        print("❌ No student found with that ID.")


def menu():
    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    init_file()
    menu()
