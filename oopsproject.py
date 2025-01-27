class PasswordManager:
    def _init_(self, username, unique_id):
        self.username = username
        self.unique_id = unique_id
        self.passwords = {}  # Dictionary to store website-password pairs

    def authenticate(self, entered_id):
        if entered_id == self.unique_id:
            print(f"Access granted. Welcome, {self.username}!")
            return True
        else:
            print("Access denied. Invalid unique ID code.")
            return False

    def view_password(self):
        website = input("Enter the website you want to view the password of: ")
        if website in self.passwords:
            print(f"Website: {website}\nPassword: {self.passwords[website]}")
        else:
            print("No password found for the given website.")

    def add_password(self):
        website = input("Enter the website: ")
        password = input("Enter the password: ")
        self.passwords[website] = password
        print("Password added successfully!")

    def edit_password(self):
        website = input("Enter the website whose password you want to edit: ")
        if website in self.passwords:
            new_password = input("Enter the new password: ")
            self.passwords[website] = new_password
            print("Password updated successfully!")
        else:
            print("No password found for the given website.")

    def remove_password(self):
        website = input("Enter the website whose password you want to remove: ")
        if website in self.passwords:
            del self.passwords[website]
            print("Password removed successfully!")
        else:
            print("No password found for the given website.")

# Main program
def main():
    print("Welcome to Password Manager!")
    id_input = input("Kindly enter your unique ID to access the application (press 0 to create a new user): ")

    if id_input == "0":
        # Creating a new user
        username = input("Enter your username: ")
        unique_id = input("Set your unique ID: ")
        user = PasswordManager(username, unique_id)
        print("User created successfully! Please restart the application to log in.")
    else:
        # Authenticating an existing user
        username = input("Enter your username: ")
        user = PasswordManager(username, id_input)
    if user.authenticate(id_input):
        while True:
            option = int(
                input(
                    "\nKindly select from the options below:\n"
                    "1. View password\n"
                    "2. Add password\n"
                    "3. Edit password\n"
                    "4. Remove password\n"
                    "5. Exit\n\n"
                )
            )
            # Corrected indentation for the following blocks:
            if option == 1:
                user.view_password()
            elif option == 2:
                user.add_password()
            elif option == 3:
                user.edit_password()
            elif option == 4:
                user.remove_password()
            elif option == 5:
                print("Exiting...")
                break
            else:
                print("Invalid option selected.")


if __name__ == "__main__":
    main()
