MONTHS_IN_YEAR = 12
def happy_birthday():
    name = input("Enter your name: ")
    month = input("Enter birth month: ")
    day = input("Enter birth day: ")
    year = input("Enter birth year: ")

    print(name, "your birthday is on", month, day + ",", year)

def main():
    happy_birthday()
    happy_birthday()
    happy_birthday()

main()