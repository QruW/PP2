import psycopg2

# Database connection
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Tr3301du",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# 1. Search by pattern
def search_by_pattern(pattern):
    print(f"\nSearching for pattern: '{pattern}'")
    cursor.execute("SELECT * FROM search_contacts(%s);", (pattern,))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(f"Name: {row[0]}, Phone: {row[1]}")
    else:
        print("No matches found.")

# 2. Insert or update user
def insert_or_update(name, phone):
    cursor.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    conn.commit()
    print(f"User '{name}' inserted or updated with phone '{phone}'.")

# 3. Delete contact
def delete_contact(value):
    cursor.execute("CALL delete_contact(%s);", (value,))
    conn.commit()
    print(f"User with name or phone '{value}' has been deleted (if existed).")

# Menu
def main():
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Search by pattern")
        print("2. Insert or update user")
        print("3. Delete user")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            pattern = input("Enter search pattern: ")
            search_by_pattern(pattern)
        elif choice == '2':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            insert_or_update(name, phone)
        elif choice == '3':
            value = input("Enter name or phone to delete: ")
            delete_contact(value)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

    cursor.close()
    conn.close()
    print("Goodbye!")

if __name__ == "__main__":
    main()
