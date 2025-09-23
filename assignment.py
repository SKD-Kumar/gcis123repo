def take_num():
    '''
    This function takes an input from the user
    '''
    num = int(input("Enter number: "))
    return num # the number is returning to the identifier calling this function via return statement

def check_evenodd(num):
    '''
    This function checks if the number it receives as an argument is an even number or an odd number
    '''
    if num%2 == 0: #if the number is divisible by 2(no remainder), then it is even
        print('Even')
    else: # else it is odd number
        print("Odd")

def square_num(num):
    '''
    This function prints the square of the numebr it receives as an argument, it does this by multiplying num to itself
    '''
    print('Square of number: ',num, '=', num*num)

def cube_num(num):
    '''
    This function prints the cube of the number it receives as argument, it does this by exponenting num to 3
    '''
    print('Cube of number:',num,'=', num**3)

def main():
    '''
    This is the main function of this code, only this must be called to start the whole code
    '''
    print("Hello! ")

    input_num = take_num()

    #now check if it is even or odd
    check_evenodd(input_num)

    #now print its square
    square_num(input_num)

    #now print its cube
    cube_num(input_num)

main()