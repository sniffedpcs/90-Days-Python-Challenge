import datetime

fName = input("Enter User's First Name ")
lName = input("Enter User's Last Name ")
age = input("Enter User's Age ")

currYear = datetime.datetime.now()

yearBorn = int(currYear.year) - int(age)
print("Good Day," + fName + " " + lName + " " + "Was Born In" + " " + str(yearBorn))

