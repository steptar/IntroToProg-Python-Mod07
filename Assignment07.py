# ------------------------------------------------- #
# Title: Assignment07
# Description: A program designed to demonstrate Python error handling and pickling information
# ChangeLog: (STarczynski, 11/30/2020, File Created)
#(STarczynski, 12/1/2020, Code added to complete assignment)
# ------------------------------------------------- #

# Part 1: Error Handling Example-------------------------------------------- #
# Processing-------------------------------------------- #

def SnackDivider(numPeople, numSnack): #This function's purpose is to divide the snacks evenly amongst all people
    try:
        snackPerPerson= numSnack/numPeople
        if numSnack%numPeople != 0: #if/else statement to raise an error
            raise TypeError
        else:
            pass
    except TypeError:
        print("The snacks cannot be divided evenly.") #The snackPerPerson result was not an integer
    except ZeroDivisionError: #standard Python exception error
        print("Zero Division Error: No people, no snacks needed")
    finally:
        print("Each person can have ", snackPerPerson, " snacks!")
# Main Part 1-------------------------------------------- #
#Collects the number of people and number of snacks available from the user and runs SnackDivider

intPeople = int(input("Please enter the number of people: "))
intSnacks= int(input("Please enter the number of snacks available: "))
SnackDivider(intPeople, intSnacks)

#------------------------------------------------ #

# Part 2: Pickling Example-------------------------------------------- #
import pickle
strFileName = 'SnackData.dat'
lstSnacks = []

# Processing -------------------------------------- #

def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "wb")
    pickle.dump(list_of_data, objFile)
    objFile.close()
    print ("Success")

def read_data_from_file(file_name):
    objFile = open(file_name, "rb")
    objFileData = []
    while True:
        try:
            objFileData.append(pickle.load(objFile))
        except EOFError:
            break
    objFile.close()
    print(objFileData)

# Main Part 2-------------------------------------------- #
print("Now we will store the snack data in a binary file.")

i=0
while i < intPeople: #while loop iterates until each person's snack amount is captured
    str_Name = input("Enter the name: ")
    str_Snacks = input("Enter the number of snacks: ")
    row = {"Name":str_Name, "Snacks": str_Snacks}
    lstSnacks.append(row)
    i+=1

save_data_to_file(strFileName, lstSnacks) #Store the list into a binary file
read_data_from_file(strFileName) # Read the data from the file into a new list object and display the contents