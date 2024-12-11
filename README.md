# FurEver-Home
# Project Overview
**FurEver Home** project is a database-driven system designed to streamline and enhance the adoption process for animals. 
It acts as a centralized platform where users can register, search, and manage information about animals available for adoption while also maintaining records of users and their interactions. 

**Key Features** <br> 
- **User Registration System** - Allows users to create profiles with personal information like name, email, phone number, and address.<br> 
- **Animal Records Management** - Maintain a database of animals with details such as name, breed, age, gender, health status, and adoption status.<br> 
- **Adoption Tracking** - Tracks the adoption process by associating users with specific animals.<br> 
- **Search Pet** - Enables potential adopters to search for animals.<br> 
- **User Features** - User can add, update, or remove animal profiles and oversee user activities. Reports can be generated for the adoption statistics and user activity.<br> 
- **Database-Driven System** -Uses MySQL for storing and managing user and animal data. Ensures data integrity and security with parameterized queries and role-based access.<br> 

FurEver Home simplify the process of finding loving homes for animals.

# Python Concepts
1. **OOP-Conept** <br> Classes and Objects - The project is organized into classes, such as FurEverHome, which encapsulate functionality for user registration, data interaction, and navigation. <br>
Methods- Functions like registerUser, registeredUser, and mainmenu are defined as methods within the class. <br>
Encapsulation - operations like database interactions are encapsulated within specific methods, ensuring better modularity and security.  <br>

2. **Exception Handling**<br> Database Errors - Catches mysql.connector.Error exceptions during query execution.<br>
Graceful Failures - Error messages are displayed to inform users about database connection or query issues. <br>

3. **Libraries**<br> mysql.connector - This library is used to connect a Python application to a MySQL database. It provides a set of methods and functionalities to perform CRUD
   (Create, Read, Update, Delete) operations on the database. <br>
   Tabulate - This library is used to format tabular data into visually appealing tables that can be displayed in the terminal or output. <br>
  OS - This library provides a way to interact with the operating system. It is used to handle system-level tasks such as clearing the terminal, managing files and directories,
  and retrieving environment variables.<br>

4. **Loops and Recursion** <br>Recursive Function Calls - Functions like registerUser are called recursively when invalid inputs are provided, ensuring user inputs are revalidated. <br>
Loop for Menu Navigation - Functions like mainmenu allow users to navigate through the system repeatedly until they choose to exit.

# Sustainable Project Goals
**SDG 15: Life on Land** Protect, restore, and promote sustainable use of terrestrial ecosystems and halt biodiversity loss.<br>
- The FurEver Home project promotes animal adoption, reducing stray populations and minimizing the risk of harm to local wildlife caused by stray animals.<br>
- Encourages responsible pet ownership, which contributes to better care for domestic animals and prevents them from negatively impacting ecosystems.

**SDG 11: Sustainable Cities and Communities** Make cities inclusive, safe, resilient, and sustainable. <br>
- The project helps reduce the number of stray animals in urban and rural communities, contributing to safer and cleaner environments.<br>
- By facilitating pet adoptions, the project fosters a sense of community responsibility toward animal welfare.

**SDG 3: Good Health and Well-being** Ensure healthy lives and promote well-being for all at all ages.<br>
- Owning pets has proven physical and mental health benefits, including stress reduction and increased physical activity through pet care.<br>
- Encouraging adoption over breeding ensures better care for abandoned or neglected animals, reducing health hazards caused by stray animals in communities.

# Instructions for running the program
Requirements before running the program<br>
1. Install Python <br>
2. Install Required libraries <br> - mysql.connector <br> - Tabulate <br> - OS<br>
3. Install XAMPP or mysql server <br> - Make sure that it is running before starting the program

**Running the Program:**
1. Open the Program:<br>
Open the FinalFur.py file in a code editor like VS Code.<br>
2. Interact with the Program:<br>
You will be presented with options in the terminal.<br>
Follow the instructions displayed to:<br>
Register a user.<br>
View or manage user data.<br>
Adopt animals.<br>
Example menu options include:<br>
1: Pet<br>
2. User<br>
3: Adoption Data<br>
4:Shelter<br>
5: Exit<br>
