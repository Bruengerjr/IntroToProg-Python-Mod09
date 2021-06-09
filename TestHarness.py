# ---------------------------------------------------------- #
# Title: Listing 08
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Bruenger,6.5.2021, Added code necessary to Test DataClasses
# Bruenger,6.5.2021, Added code necessary to test ProcessingClasses
# Bruenger,6.5.2021, Added code necessary to test IOClasses
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    import IOClasses as I
else:
    raise Exception("This file was not created to be imported")
# Test data module
objP1 = D.Person("Bob", "Smith")
objP2 = D.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))


objE1 = D.Employee("0","Kevin","Malone")
objE2 = D.Employee("1","Jim","Halpert")

lstEmployeeTable = [objE1, objE2]
for row in lstEmployeeTable:
    print(row.to_string(), type(row))

# Test processing module
P.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("PersonData.txt")
for row in lstFileData:
    p = D.Person(row[0], row[1])
    print(p.to_string().strip(), type(p))

# Test IO classes
# TODO: create and test IO module
I.EmployeeIO