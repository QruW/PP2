import psycopg2
import csv

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Tr3301du",
    host="localhost", 
    port="5432"
)
cur = conn.cursor()

# Create PhoneBook table
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)
    conn.commit()
    print("Table created or already exists.")

# Insert data from CSV
def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile: # define csv file
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute(
                "INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", # %s is a placeholder for the values
                (row['name'], row['phone']) # it searches for the name and phone rows in the csv file
            )
    conn.commit()
    print("Data inserted from CSV.")

# Insert data from console
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute(
        "INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Data inserted from console.")

# Update data
def update_data():
    choice = input("Update (1) name or (2) phone? ")
    if choice == '1':
        old_name = input("Old name: ")
        new_name = input("New name: ")
        cur.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (new_name, old_name))
    elif choice == '2':
        name = input("Name to update phone for: ")
        new_phone = input("New phone: ")
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    print("Data updated.")

# Query data with filter
def query_data():
    filter_type = input("Filter by (1) name or (2) phone: ")
    if filter_type == '1':
        name = input("Enter name: ")
        cur.execute("SELECT * FROM PhoneBook WHERE name = %s", (name,))
    elif filter_type == '2':
        phone = input("Enter phone: ")
        cur.execute("SELECT * FROM PhoneBook WHERE phone = %s", (phone,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Delete data
def delete_data():
    method = input("Delete by (1) name or (2) phone: ")
    if method == '1':
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
    elif method == '2':
        phone = input("Enter phone to delete: ")
        cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
    conn.commit()
    print("Data deleted.")

# Show all data
def show_data():
    cur.execute("SELECT * FROM PhoneBook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Main menu where we can choose the options
# The menu is displayed until the user chooses to exit
def main():
    create_table()
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update data")
        print("4. Query data")
        print("5. Delete data")
        print("6. Show all data")
        print("7. Exit")
        print("8. Clear all data")
        choice = input("Choose an option: ")

        if choice == '1':
            insert_from_csv("contacts.csv")
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            show_data()
        elif choice == '7':
            break
        elif choice == '8':
            cur.execute("DELETE FROM PhoneBook")
            conn.commit()
            print("All data cleared.")
        else:
            print("Invalid option.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
