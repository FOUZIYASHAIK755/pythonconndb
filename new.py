import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",        
    user="root",             
    password="1234",        
    database="cm"          
)
cursor = db_connection.cursor()
while True:
    print("\nSelect an option:")
    print("1. Insert customer details")
    print("2. Delete customer details")
    print("3. Update customer flavour")
    print("4. Display all customers")
    print("5. Display all customers in ascending order of name")
    print("6. Display customers based on amount between 40 and 50")
    print("7. Display customers whose city is 'hyd'")
    print("8. Exit")
    
    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

    if choice == '1':
        # Insert customer details
        cname = input("Enter name: ")
        address = input("Enter address: ")
        pastry = input("Select flavour: ")
        amount = float(input("Enter amount: "))  
        # SQL query to insert data into bakery_cart table
        insert_query = """
        INSERT INTO bakery_cart (cname, address, pastry, amount)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (cname, address, pastry, amount))
        db_connection.commit()
        print("Data inserted successfully!")

    elif choice == '2':
        # Delete customer details
        cid = int(input("Enter customer ID to delete: "))  
        delete_query = "DELETE FROM bakery_cart WHERE cid = %s"
        cursor.execute(delete_query, (cid,))
        db_connection.commit()
        print(f"Customer with ID {cid} has been deleted successfully!")

    elif choice == '3':
        # Update the flavour of a customer's order
        cid_to_update = int(input("Enter customer ID to update flavour: "))
        new_flavour = input("Enter new flavour: ")
        # SQL query to update the flavour of a specific customer
        update_query = "UPDATE bakery_cart SET pastry = %s WHERE cid = %s"
        cursor.execute(update_query, (new_flavour, cid_to_update))
        db_connection.commit()

        print(f"Flavour for customer with ID {cid_to_update} has been updated to {new_flavour}.")

    elif choice == '4':
        # Display all customers
        cursor.execute("SELECT * FROM bakery_cart")
        customers = cursor.fetchall()
        print("\nAll Customers:")
        for customer in customers:
            print(customer)

    elif choice == '5':
        # Display all customers in ascending order of name
        cursor.execute("SELECT * FROM bakery_cart ORDER BY cname ASC")
        customers = cursor.fetchall()
        print("\nCustomers in Ascending Order of Name:")
        for customer in customers:
            print(customer)

    elif choice == '6':
        # Display customers based on amount between 40 and 50
        cursor.execute("SELECT * FROM bakery_cart WHERE amount BETWEEN 40 AND 50")
        customers = cursor.fetchall()
        print("\nCustomers with Amount Between 40 and 50:")
        for customer in customers:
            print(customer)

    elif choice == '7':
        # Display customers whose city is 'hyd'
        cursor.execute("SELECT * FROM bakery_cart WHERE address LIKE '%hyd%'")
        customers = cursor.fetchall()
        print("\nCustomers from 'hyd' city:")
        for customer in customers:
            print(customer)

    elif choice == '8':
        # Exit the program
        break
    else:
        print("Invalid choice. Please try again.")

# Close the cursor and connection
cursor.close()
db_connection.close()
