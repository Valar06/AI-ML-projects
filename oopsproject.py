import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root')
cursor=mycon.cursor()
class PasswordManager:
    def _init_(self, username, unique_id):
        self.username = username
        self.unique_id = unique_id

    def authenticate(self, entered_id):
        if entered_id == self.unique_id:
            print("Access granted. Welcome,", self.username)
            return True
        else:
            print("Access denied. Invalid unique ID code.")
            return False
def viewpassword():
    a = input("Enter the website you want to view the password of: ")
    query = "SELECT * FROM websites WHERE id = %s AND web_name = %s"
    values = (id_input, a)
    cursor.execute(query, values)
    
def _init_(self,username):
    self.connection=mysql.connector.connect(host='localhost',user='root',database='password_manager')
    self.cursor=self.connection.cursor()
    self.username=username
  def close_connection(self):
    self.connection.close()
  def get_password(self):
    try:
      self.cursor.execute("Select password FROM users WHERE username=?",(self.username,))
      result=self.cursor.fetchone()
      if result:
        return result[0]
      else:
        return "User not found"

    # Fetch and display the result
    result = cursor.fetchall()
    if result:
        for row in result:
            print("ID:", row[0], "\nWebsite:", row[1], "\nPassword:", row[2])  # Adjust indices
    else:
        print("No password found for the given ID and website.")
# Main program
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
    user = PasswordManager("Kavya", "1234")  # Example user
    if user.authenticate(id_input):
        option = int(input("\nKindly select from the options below:\n1. View password\n2. Edit password\n3. Remove password\n4. Add password\n5. Exit \n\n"))
        if option == 1:
            print("Viewing password...")
            viewpassword()
        elif option == 2:
            print("Editing password...")
        elif option == 3:
            print("Removing password...")
        elif option == 4:
            print("Adding password.....")
        elif option==5:
            print("Exiting....")
        else:
            print("Invalid option selected.")
