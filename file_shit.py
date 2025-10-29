'''f1 = open("hello.py","rt")
print(f1.read())
f1.close()'''


def print_lines(file_name):
    f1 = open(file_name, "rt")
    for line in f1:
        print(line.strip())
    f1.close()

def word_search(filename):
    word = input("Enter word: ")
    with open(filename,"rt") as f1:
        while True: #error cause readline doesn't raise error if it reaches end of file, it just returns empty string
            line = f1.readline()
            if line == '':
                print(word, "not found")
                break
            words = line.split()
            print(line)
            if word in words:
                print(word)
                break

def longest_word(filename):
    with open(filename,"rt") as f1:
        longest_in_file = ''
        for line in f1:
            words = line.split(' ')
            longest_word = ''
            for word in words:
                if len(word) > len(longest_word):
                    longest_word = word
            print(longest_word, len(longest_word), 'in the line')
            if len(longest_word) > len(longest_in_file):
                longest_in_file = longest_word
        print(longest_in_file, len(longest_in_file), 'in the file')

def print_name_from_CSV(filename):
    with open(filename,"rt") as f1:
        next(f1) #skips the first line which is header
        for line in f1:
            parts_of_name = line.split(',')
            firstname = parts_of_name[0]
            lastname = parts_of_name[1]
            print(firstname, lastname)

def check_file_exists(filename):
    try:
        f1 = open(filename,"rt")
        f1.close()
        return True
    except FileNotFoundError:
        print("File not found")
        return False

def prompt_and_write(filename):
    file_check = check_file_exists(filename)
    if file_check:
        with open(filename,"at") as f1: #cause a = append mode which adds to the end of file, and doesn't truncate the file
            while True:
                name = input("Enter name (Just press enter to stop): ")
                if name == '':
                    break
                f1.write(name + '\n') #important to add newline character
    else:
        with open(filename,"wt") as f1:
            while True:
                name = input("Enter name (Just press enter to stop): ")
                if name == '':
                    break
                f1.write(name + '\n') #important to add newline character
    print("Written to file")

def sum_of_files():
    sum_of_num_of_files = 0
    for i in range(3):
        filename = input("Enter filename: ")
        with open(filename) as f1: #here error if file doesn't exist
            content = f1.read()
            all_num = content.split('\n')
            print("Sum of numbers =",sum(all_num))
            sum_of_num_of_files+=sum(all_num)
    print("Total Sum =",sum_of_num_of_files)
        
def sum_of_files_replica():
    sum_of_num_of_files = 0
    for i in range(3):
        filename = input("Enter filename: ")
        try:
            with open(filename) as f1: #here error if file doesn't exist
                content = f1.read()
                all_num = content.split('\n')
                print("Sum of numbers =",sum(all_num))
                sum_of_num_of_files+=sum(all_num)
        except FileNotFoundError:
            print("File not found, skipping to next file")
            continue
    print("Total Sum =",sum_of_num_of_files)

def class_avg():
    """
    This function reads student names and their marks from a CSV file,
    calculates the average marks for each student, and also computes the class average for each subject."""
    
    '''example csv file content:
    Student, GCIS, Calc, NSSA
    John, 85, 90, 78
    Jane, 88, 92, 80
    Doe, 90, 85, 88
    '''
    filename = input("Enter filename: ")
    with open(filename) as f1:
        next(f1)
        total_students = 0
        marks_gcis = 0
        marks_calc = 0
        marks_nssa = 0
        bool_check = True
        while bool_check == True:
            line = f1.readline()
            if line == '':
                bool_check = False
                break
            student_marks = line.strip().split(',') #important to strip newline character
            #sum_marks_student = sum(student_marks[1:]) #error if we don't convert to int
            for i in range(1,len(student_marks)):
                student_marks[i] = int(student_marks[i])
            sum_marks_student = sum(student_marks[1:])
            avg_marks_student = sum_marks_student/(len(student_marks)-1)
            print("Average makrs of",student_marks[0],"is",avg_marks_student)
            marks_gcis += int(student_marks[1]) #important to convert to int
            marks_calc += int(student_marks[2])
            marks_nssa += int(student_marks[3])
            total_students += 1
        avg_gcis = marks_gcis/total_students
        avg_calc = marks_calc/total_students
        avg_nssa = marks_nssa/total_students
        print("Class average of GCIS is",avg_gcis)
        print("Class average of Calc is",avg_calc)
        print("Class average of NSSA is",avg_nssa)

longest_word("prime.txt")
        