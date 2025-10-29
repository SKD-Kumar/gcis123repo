'''
Details of Group Members:
Student Name - Student Number
Dhruv Mer - 433006076
Mohamad Moukayed - 462445278
Sarvagnya Kumar Dandala - 432009415

Manifesto / Students Contributions:
Dhruv Mer - (Tasks 3 and Task 4)
Mohamad Moukayed - (Tasks 1 and Task 2)
Sarvagnya Kumar Dandala - (Task 5 and Documentation)'''

# Task 1
def check_limit(borrowed):
    """Checks the number of borrowed books against the limits and returns the appropriate status
    Input: Int, number of books borrowed
    Output: String, status"""
    if borrowed < 0: # Checks if the number is valid first
        return "Error: Invalid number of books for"
    elif borrowed <= 3: # Checks if number of books borrowed is between 0 and 3
        return "Within Limit"
    elif borrowed > 3 and borrowed <= 6: # Fine if the number is between 4 and 6
        return "Over limit: Fine $5"
    elif borrowed > 6: # Bigger fines for number of borrowed books above 6
        return "Over Limit: Fine $10"
    
# Task 2
def process_borrowers(filename):
    """Iterates through the csv file of students books borrowed and prints them. Also checks if all the data is valid or not
    Input: String, filename of the csv file"""
    with open(filename, 'r') as f: # Open the file
        next(f) # Skip header in the csv file
        for line in f: # Start iteration
            student = line.strip().split(',') # Split each row into the student name and the books borrowed by the student
            try: # try check to make sure that the books borrowed field is an integer and to print an error if it isnt
                books_borrowed = int(student[1]) # Get books borrowed data from csv
                status = check_limit(books_borrowed) # Check the limit status for number of books borrowed
                if "Error" in status: # Checks if the check_limit function returned an error to ensure proper formatting for errors
                    print(status, student[0]) # Print raw error
                else:
                    print("Student name: " + student[0] + ", Status: " + status) # Prints results
            except:
                print("Error: Non-numeric value for", student[0]) # If the books borrowed column had a non int value, then this will execute letting the user know that their is invalid data

# Task 3
def calculate_average_books(filename):
    """Calculate the average number of books borrowed from everybody in total
    Input: String, file path of the csv"""
    with open(filename,"r") as f: # Open the file
        # Initialize variables
        Student_count=0
        Books_count=0
        next(f) # Skip header
        for line in f: # iterate through every row
            list_readfile=line.strip().split(",") # Clear trailing and leading whitespaces and split commas into list of tokens
            try: # Make sure that the 2nd column is an int otherwise print error
                if int(list_readfile[1])>0: # Check if number of books borrowed is above 0
                    Books_count=Books_count+int(list_readfile[1]) # Add number of books borrowed
                    Student_count+=1 # Increment student count
            except:
                pass # If the 2nd column is not an int, just skip it
        Total_average=Books_count/Student_count # Calculate average number of books

        print("The average number of books borrowed is:",round(Total_average,2)) # Print result



# Task 4
def count_over_limit(filename): 
    """Count the number of students with more books borrowed than the allowed amount
    Input: String, file path of the csv"""
    with open(filename, "r") as f: # Opening the file
        #initializing variable
        Total_greater_than_3=0
        next(f) #skip the header of the file to go to the data
        for line in f: #iterate through the data
            list_readfile=line.strip().split(",") #strip - to remove trailing spaces, split - to split the line into a list of tokens according to delimiter
            try:
                if int(list_readfile[1])>3: # Check if number of books borrowed is above 3
                    Total_greater_than_3+=1
            except:
                pass # If the 2nd column is not an int, just skip it

        print("Number of students with more than 3 books borrowed:",Total_greater_than_3)

#Task 5
def main():
    """Main function to run all the tasks
    No input or return statements"""
    while True: # Loop until a valid file name is given
        filename = input("Enter the file name: ") #take input from user
        try: # to check if file exists
            with open(filename, 'r') as file: # Open to check if file exists
                pass # If it exists, do nothing with the file, just move on
            break # If file exists, break out of the loop
        except FileNotFoundError: # If file does not exist, print error and go to next iteration
            print("File not found. Please try again.")
    print() # a seperation line
    process_borrowers(filename) # Call process borrowers function
    print() # a seperation line
    calculate_average_books(filename) # Call average calculation function
    count_over_limit(filename) # Call count over limit function

main()# Call main to run the program