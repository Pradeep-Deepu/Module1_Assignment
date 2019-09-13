# To prompt a message to give size of list
Size=int(input('Enter list size\n'))
#Declaring List Variable
List=[]
#For loop to iterate the size of list
for x in range(0,Size):
            #Values taken from user
            list_of_numbers=int(input('Enter number \n'))
            #Appending the values to List
            List.append(list_of_numbers)
#Defining function to find out Largest number
def max_in_list(List):
            print("Largest number is :")
            #To print Largest number from list
            print(max(List))
#calling a function
max_in_list(List)
