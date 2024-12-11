import mysql.connector
from tabulate import tabulate
import os

class DatabaseManager:
    def __init__(self, host, user, password, database, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None

    def connect(self):
        """Private method to establish a database connection."""
        if not self.connection:
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                    port=self.port
                )
            except mysql.connector.Error as err:
                print(f"Database Connection Error: {err}")
                raise

    def executequery(self, query, params=None, fetch=False):
        """Encapsulates query execution."""
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            if fetch:
                return cursor.fetchall()
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Query Execution Error: {err}")
            self.connection.rollback()
    def closeconnection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None

class FurEverHome:
    def __init__(self):
        self.db = DatabaseManager(
            host="localhost", user="root", password="", database="fureverhomedb"
        )
    
    def Title(self):
        print("+================================================================================================================================================================================+")
        print("|\t\t\t\t\t\t\t\t\t   FurEver HOME\t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("|\t\t\t\t\t\t\t\tWhere you can find your FURever family!\t\t\t\t\t\t\t\t\t\t\t|")
        print("+================================================================================================================================================================================+")
    
    def clearterminal(self):
        os.system("cls" if os.name == "nt" else "clear")

    def addPet(self):
        """Add a new pet to the database."""
        try:
            name = input("Enter the name of the pet: ")
            age = input("Enter the age of the pet: ")
            species = input("Enter the species of the pet: ")
            breed = input("Enter the breed of the pet: ")
            size = float(input("Enter the size of the pet: "))
            gender = input("Enter the gender of the pet: ")

            query = """
            INSERT INTO pet (Name, Age, Species, Breed, Size, Gender) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (name, age, species, breed, size, gender)
            self.db.executequery(query, values)
        except Exception as e:
            print(f"Error adding pet: {e}")

    def addAdoption(self):
        try:
            pet_id = input("Enter the number ID of the pet: ")
            user_id = input("Enter the number ID of the user: ")
            adoption_date = input("Enter the date when adoption happened (YYYY-MM-DD): ")

            query = """
            INSERT INTO adoption (PetId, UserId, Date)
            VALUES (%s, %s, %s)
            """
            values = (pet_id, user_id, adoption_date)
            self.db.executequery(query, values)    
        except Exception as e:
            print(f"Error adding adoption: {e}")

    def addShelter(self):
        try:
            name = input("Enter the name of the shelter: ")
            location = input("Enter the location of the shelter: ")
            email = input("Enter the email of the shelter: ")
            phone = input("Enter the phone number of the shelter: ")
            address = input("Enter the address of the shelter: ")

            query = """
            INSERT INTO shelter (Name, Location, Email, PhoneNum, Address)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (name, location, email, phone, address)
            self.db.executequery(query, values)
        except Exception as e:
            print(f"Error adding shelter: {e}")

    def deletePet(self):
        try:
            pet_id = input("Enter the PetId to be deleted: ")

            if not pet_id.isdigit():
                print("Invalid PetId. Please enter a numeric value.")
                return

            query = "DELETE FROM pet WHERE PetId = %s"
            self.db.executequery(query, (pet_id,))
            print(f"Pet with PetId {pet_id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting pet: {e}")
    
    def deleteAdoption(self):
        try:
            adoption_id = input("Enter the AdoptionId to be deleted: ")

            if not adoption_id.isdigit():
                print("Invalid AdoptionId. Please enter a numeric value.")
                return

            query = "DELETE FROM adoption WHERE AdoptionId = %s"
            self.db.executequery(query, (adoption_id,))
            print(f"Adoption record with AdoptionId {adoption_id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting adoption: {e}")

    def deleteShelter(self):
        try:
            shelter_id = input("Enter the ShelterId to be deleted: ")

            if not shelter_id.isdigit():
                print("Invalid ShelterId. Please enter a numeric value.")
                return

            query = "DELETE FROM shelter WHERE ShelterId = %s"
            self.db.executequery(query, (shelter_id,))
            print(f"Shelter with ShelterId {shelter_id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting shelter: {e}")

    def countRecords(self, table_name):
        try:
            query = f"SELECT COUNT(*) FROM {table_name}"
            result = self.db.executequery(query)
            count = result[0][0]
            print(f"Total number of records in the {table_name} table: {count}")
        except Exception as e:
            print(f"Error counting records in {table_name}: {e}")

    def updatePet(self):
        try:
            pet_id = input("Enter the PetId of the pet to update: ")
            new_name = input("Enter the new name for the pet: ")

            query = "UPDATE pet SET Name = %s WHERE PetId = %s"
            values = (new_name, pet_id)
            self.db.executequery(query, values)
        except Exception as e:
            print(f"Error updating pet: {e}")
    
    def petinfo(self):
        self.Title()
        print("\t\t\t\t\t★→→→→→★ Pet Data ★→→→→→★")
        try:
            query = "SELECT * FROM pet"
            results = self.db.executequery(query, fetch=True)
            headers = ["Pet ID", "Name", "Age", "Species", "Breed", "Size", "Gender"]

            headers = ["Pet ID", "Name", "Age", "Species", "Breed", "Size" "Gender"]
            print(tabulate(results, headers=headers, tablefmt="grid"))
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        print('+===============================================================================================================================================================================+')  

        edit = input("Would you like edit the data? (Yes or No = Exit): ").strip().lower()
        if edit == 'yes':
            print("╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
            print("|\t  1. Add  \t|\t  2. Delete  \t|\t  3. Update  \t|\t  4. Count  \t|\t   Exit  \t|")
            print("╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
            choice = input("Enter the number of your choice: ").strip()
        
            if choice == '1':
                self.clearterminal()
                self.addPet()
            elif choice == '2':
                self.clearterminal()
                self.deletePet()
            elif choice == '3':
                self.clearterminal()
                self.updatePet()
            else:
                print("Invalid choice. Please try again.")
        else:
            self.clearterminal()
            self.mainmenu()

    def userinfo(self):
        self.Title()
        print("\t\t\t\t\t★→→→→→★ User Data ★→→→→→★")
        try:
            query = "SELECT * FROM userinfo"
            results = self.db.executequery(query, fetch=True)
            headers = ["User ID", "Name", "Email", "Phone Number", "Address"]

            print(tabulate(results, headers=headers, tablefmt="grid"))

        except Exception as e:
            print(f"Error: {e}")

            print('+===============================================================================================================================================================================+')  
    
        choice=input("Would you like to count the users? (Yes or No = Exit ): ").strip().lower()
    
        if choice.strip().lower() == 'Yes':
            self.clearterminal()
            self.countUser()
        else:
            self.clearterminal()
            self.mainmenu()

    def adoptiondata(self):
        self.Title()
        print("\t\t\t\t\t★→→→→→★ Adoption Data ★→→→→→★")
        try:
            query = "SELECT * FROM adoption"
            results = self.db.executequery(query, fetch=True)
            headers = ["Adoption Id", "Pet Id", "User Id", "Date"]

            print(tabulate(results, headers=headers, tablefmt="grid"))

        except mysql.connector.Error as err:
            print(f"Error: {err}")

            print('+===============================================================================================================================================================================+')  
   
        edit=input("Would you like to edit the Data? (Yes or No = Exit ): ").strip().lower()
    
        if edit.strip().lower() == 'yes':
            print("╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗")
            print("|\t  1. Add  \t|\t  2. Delete  \t|\t  3. Count \t|\t   Exit  \t|")
            print("╚══════════════════════════════════════════════════════════════════════════════════════════════════╝")
            print('What action would you like to perform? ')
            choice = input("\nEnter the number of your choice: ").strip()
            
            if choice == '1':
                self.clearterminal()
                self.addAdoption()
            elif choice == '2':
                self.clearterminal()
                self.deleteAdoption()
            elif choice == '3':
                self.clearterminal()
                self.countAdoption()
            else:
                print("Invalid choice. Please try again.")
        else:
            self.clearterminal()
            self.mainmenu()

    def shelter(self):
        self.Title()
        print("\t\t\t\t\t★→→→→→★ Shelter Information ★→→→→→★")
        try:
            query = "SELECT * FROM shelter"
            results = self.db.executequery(query, fetch=True)

            headers = ["Shelter Id", "Name", "Location", "Contact", "Pet Id"]

            print(tabulate(results, headers=headers, tablefmt="grid"))

        except Exception as e:
            print(f"Error counting pets: {e}")
        print('+===============================================================================================================================================================================+')  
   
        edit=input("Would you like to edit the Data? (Yes or No = Exit ): ").strip().lower()
    
        if edit.strip().lower() == 'yes':
            print("╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
            print("|\t  1. Add  \t|\t  2. Delete  \t|\t  3. Count  \t|\t   Exit  \t|")
            print("╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
            print('What action would you like to perform? ')
            choice = input("\nEnter the number of your choice: ").strip()
            
            if choice == '1':
                self.clearterminal()
                self.addShelter()
            elif choice == '2':
                self.clearterminal()
                self.deleteShelter()
            elif choice == '3':
                self.clearterminal()
                self.countShelter()
            else:
                print("Invalid choice. Please try again.")
        else:
            self.clearterminal()
            self.mainmenu()

    def mainmenu(self):
        self.Title()
        print("\t\t\t\t\t\t\t----------------Welcome to FurEver Home!------------------")
        print("\t\t\t\t\t\t\t\t\tPlease select an option:")
        print("\t\t\t\t\t\t\t\t1. Pet Information")
        print("\t\t\t\t\t\t\t\t2. User Information")
        print("\t\t\t\t\t\t\t\t3. Shelter Information")
        print("\t\t\t\t\t\t\t\t4. Adoption Data")
        print("\t\t\t\t\t\t\t\t5. Exit")

        choice = input("\t\t\t\t\t\t\t\tEnter the number of your choice: ").strip()
        if choice == '1':
            self.clearterminal()
            self.petinfo()
        elif choice == '2':
            self.clearterminal()
            self.userinfo()
        elif choice == '3':
            self.clearterminal()
            self.shelter()  
        elif choice == '4':
            self.clearterminal()
            self.adoptiondata()  
        elif choice == '5':
            print("+----------------------------Thank you for using FurEver Home, see you again soon!----------------------------+")
        else:
            self.clearterminal()
            self.mainmenu()
    
    def registeredUser(self):
        self.Title()
        try:
            print('\t\t\t\t\t\t\t•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•.•')
            username = input('\t\t\t\t\t\t\tEnter your Username: ')

            # Query to check if the user exists
            query = "SELECT Name FROM userinfo WHERE Name = %s"
            values = (username,)
            result = self.db.executequery(query, values, fetch=True)

            if result:
                self.clearterminal()
                self.mainmenu()
            else:
                print("\t\t\t\t\t\t\tUser not found. Please register first.")
                self.registerUser()

        except mysql.connector.Error as err:
            print(f"Database error: {err}")
    

    def registerUser(self):
        self.Title()
        print('\t\t\t\t\t★→→→→→★ Please register first and double check if the informations are correct ★→→→→→★')
        
        username = input('\t\t\t\t\t\t\tEnter your Full Name (UserName): ')
        email = input('\t\t\t\t\t\t\tEnter your active Email: ')
        phoneNumber = input('\t\t\t\t\t\t\tEnter an active PhoneNumber: ')
        address = input('\t\t\t\t\t\t\tEnter your current Address: ')

        if not username or not email or not phoneNumber or not address:
            print('\t\t\t\t\t  Error, Information cannot be empty. Please enter valid information to continue.')
            self.registerUser() 
        elif not phoneNumber.isdigit() or not (10 <= len(phoneNumber) <= 12):
            print('\t\t\t\t\tError, Invalid Phone Number. It should be numeric and 11 digits long.')
            self.registerUser() 
        else:
            try:
                query = """
                INSERT INTO userinfo (name, email, phoneNum, address)
                VALUES (%s, %s, %s, %s)
                """
                values = (username, email, phoneNumber, address)
                self.db.executequery(query, values)
                print('\t\t\t\t\t★→→→→→★ Success! Your information has been saved. Welcome to FurEver Home! ★→→→→→★')
            except Exception as e:
                print(f'\t\t\t\t Error during registration: {e}')

            print("\t\t\t\t\t\t\t╔═════════════════════════════^^═══╗")
            print(f"\t\t\t\t\t\t\t  Name: {username}")
            print(f"\t\t\t\t\t\t\t  Email: {email}")
            print(f"\t\t\t\t\t\t\t  Phone Number: {phoneNumber}")
            print(f"\t\t\t\t\t\t\t  Address: {address}")
            print("\t\t\t\t\t\t\t╚═══════v══════════v═══════════════╝")
            done = input("Are the information correct?(yes/no): ").strip().lower()
    
            if done.strip().lower() == 'yes':
                self.clearterminal()
                self.registeredUser()
            else:
                self.clearterminal()
                self.registerUser()

    def entry(self):
        self.Title()
        print("\t\t\t\t\t\t\t\t★→→→→→★ Please select an option ★→→→→→★")
        print("\t\t\t\t\t\t\t\t\t╔═════════════════^^═══╗")
        print("\t\t\t\t\t\t\t\t\t|  1. Registered User  |")
        print("\t\t\t\t\t\t\t\t\t╚════v═══════v═════════╝")
        print("\t\t\t\t\t\t\t\t\t╔═════════════════^^═══╗")
        print("\t\t\t\t\t\t\t\t\t|  2. Register         |") 
        print("\t\t\t\t\t\t\t\t\t╚════v═══════v═════════╝")
        print("\t\t\t\t\t\t\t\t\t╔═════════════════^^═══╗")
        print("\t\t\t\t\t\t\t\t\t|  3. Exit             |")
        print("\t\t\t\t\t\t\t\t\t╚════v═══════v═════════╝")
        print("\t\t\t\t\t\t\t   NOTE: Please register first if not yet registered")

        
        choice = input("\t\t\t\t\t\t\t\t\tEnter your choice (1/2/3): ")

        if choice == '1':
            self.clearterminal()
            self.registeredUser()
        elif choice == '2':
            self.clearterminal()
            self.registerUser()
        elif choice == '3':
            print("\t\t\t\t\t\t\t+---------------------------------------------------------------+")
            print("\t\t\t\t\t\t\t|\t\tThank you for visiting FurEver Home!\t\t|")
            print("\t\t\t\t\t\t\t+---------------------------------------------------------------+")
        else:
            self.clearterminal()
            self.entry()

if __name__ == "__main__":
    app = FurEverHome()
    app.entry()









    


