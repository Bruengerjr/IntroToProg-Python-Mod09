# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Bruenger,6.5.21,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
import IOClasses as IO
import DataClasses as DC
import ProcessingClasses as PC
choice = ""

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
list_of_rows = [PC.FileProcessor.read_data_from_file(file_name="EmployeeData.txt")]


while(True):
    # Show the Menu
    IO.EmployeeIO.print_menu_items()
    # Ask user to choose an option 1-4
    choice = IO.EmployeeIO.input_menu_options()

    # Option 1 Show user current data in the list of employee objects
    if choice.strip() == '1':  # Add a new Task
        IO.EmployeeIO.print_current_list_items(list_of_rows)
        continue  # to show the menu

    elif choice == '2':  # Let user add data to the list of employee objects
        emp = IO.EmployeeIO.input_employee_data()
        list_of_rows.append(emp)
        print(list_of_rows)
        continue  # to show the menu

    elif choice == '3':   # let user save current data to file
        #if choice.lower() == "y":
        PC.FileProcessor.save_data_to_file(file_name="EmployeeData.txt",list_of_objects=[list_of_rows])
        #else:
        #    print("Save Cancelled!")
        continue  # to show the menu

    elif choice == '4':  #  Exit Program
        print("Goodbye!")
        break   # and Exit

# Main Body of Script  ---------------------------------------------------- #
