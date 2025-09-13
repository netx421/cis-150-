#This is intended to compute and display 
#the average grade of three tests for any number of students. 
#The program executes until the user enters a negative value 
#for the first test score.

def main():
  print("Enter score for test 1 or a negative number to quit")
  test1 = float(input("Test 1: "))

# Loop until a negative value is entered

  while test1 >= 0:
    test2 = float(input("Enter score for test 2: "))
    test3 = float(input("Enter score for test 3: "))

    average = (test1 + test2 + test3) / 3
    print("Average is", average)

    print("\nEnther score for test 1 or a negative number to quit")  
    test1 = float(input("Test 1:  "))

  print("End of program")

#Run the program
main()
