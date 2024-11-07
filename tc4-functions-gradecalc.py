############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: 

# main() FUNCTION
def main():
    def baseNumericCalculation (letterGrade):
            if letterGrade == "A":
                numericGrade = 4.0
            elif letterGrade == "B":
                numericGrade = 3.0
            elif letterGrade == "C":
                numericGrade = 2.0
            elif letterGrade == "D":
                numericGrade = 1.0
            elif letterGrade == "F":
                numericGrade = 0.0
            else:
                #If an invalid entry is made
                return 0.0
            
            if modifier == "+":
                if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
                    numericGrade += 0.3
            elif modifier == "-":
                if letterGrade != "F":     # Minus is not valid on F
                    numericGrade -= 0.3
            return numericGrade
    
    def errorCheck(letterGrade):
         if letterGrade == "A" or letterGrade == "B" or letterGrade == "C" or letterGrade == "D" or letterGrade == "F":
            return False
         else:
              return True
   
    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

    numericGrade = 0.0
    grades = [0.0,0.0,0.0,0.0,0.0,0.0] #list of grades curently empty 
    classes = ["PROG1700", "NETW1700", "OSYS1200", "WEBD1000", "COMM1700", "DBAS1007"] #list of classes that correspond to the grades
    error = True

    #Gather user inputs loop
    for i in range(6):
        error = True
        while error:
            letterGrade = input("Please enter a letter grade for {0}: ".format(classes[i])).upper() #asks you for grade for a specific class
            error = errorCheck(letterGrade) #error checking sequence
            modifier = input("Please enter a modifier (+, - or nothing) : ") # asks for if your grade has a plus or minus modifier
        grades[i] = baseNumericCalculation(letterGrade) #adds numeric grade to grades list 

    # Output final message and result, with formatting
    for i in range(6):
        print("The numeric value for {0}: {1:.1f}".format(classes[i],grades[i]))
        numericGrade += grades[i] #making numericGrade a variable that will now store the cumulative of all our numeric grades for our gpa calculation
    
    print("************************************")
    print("Your grade point average for the semester is: {0:.1f}".format(numericGrade / 6)) #gpa is calculated in format()

#PROGRAM EXECUTION STARTS HERE
main()
#after doing this i realize i probably could of made my function return the entire array of numeric values instead of individual values
