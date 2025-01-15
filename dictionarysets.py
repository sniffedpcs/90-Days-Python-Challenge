def manage_users():
    users = {}  # Empty dictionary to store user information
    
    while True:
        print("\n1. Add user")
        print("2. Look up user")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            users[name] = age
            print(f"Added {name} to the system.")
            
        elif choice == "2":
            name = input("Enter name to look up: ")
            if name in users:
                print(f"Name: {name}, Age: {users[name]}")
            else:
                print("User not found.")
                
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the program
manage_users()