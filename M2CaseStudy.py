# Author: Landon Ernst
# File name: M2CaseStudy.py
# Description: This app accepts a student's name and GPA, and checks if they qualify for the Dean's List, Honor Roll, and neither.

def main():
    while True:
        #Asks for the student's last name
        l_name = input("Enter student's last name (or 'ZZZ' to quit): ")
        #If the last name entered is 'ZZZ' it will end the program
        if l_name == 'ZZZ':
            break
        
        #Asks for the student's first name
        f_name = input(f"Enter {l_name}'s first name: ")

        #Asks for the student's GPA and it changes it to a float
        gpa = float(input(f"Enter {f_name} {l_name}'s GPA: "))
        
        #Checks if the student'ss GPA is 3.5 or higher
        if gpa >= 3.5:
            #If so, they made the Dean's List
            print(f"{f_name} {l_name} made the Dean's List.")

        #Checks if the student's GPA is between 3.25 and 3.49
        elif gpa >= 3.25:
            #If so, they made the Honor Roll. If not then they didn't qualify for either
            print(f"{f_name} {l_name} made the Honor Roll.")
        else:
            print(f"{f_name} {l_name} did not qualify for either.")
    
    #Outputs that the program is finished.
    print("Program finished.")

if __name__ == "__main__":
    main()
