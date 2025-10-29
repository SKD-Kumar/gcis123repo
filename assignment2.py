def main():
    while True:
        filename = input("Enter the file name: ")
        try:
            with open(filename, 'r') as file:
                pass
            break
        except FileNotFoundError:
            print("File not found. Please try again.")
    process_borrowers(filename)
    calculate_average_books(filename)
    count_over_limit(filename)