## FUNCTIONS/CLASES IMPLEMENTATIONS
line = '------------------------------------------------------------------------------'
def menu():
    print("-------------------------Unit Testing for Algorithms-------------------------")
    print('Options')
    print('\t1. New Test\n\t2. See registers\n\t3. Quit')
    print(line)
    while True:
        fchoice = int(input('Your choice: '))
        if fchoice == 1:
            newTestW()
            break
        elif fchoice == 2:
            dispRegistersW()
            break
        elif fchoice == 3:
            print(line)
            print("\t\tThank you for testing with us!")
            print(line)
            break
        else:
            print('\n'+line)
            print('\tMake sure you select a valid option number.\n')
    

def newTestW():
    print('\n\n'+line)
    print('----------------------------- New Algortihm Testing ---------------------------')
    usrName = input("\tEnter tester name: ")
    print('\tWhat algorithm do you want to test?...')
    funcs_to_test = ['Sum of first n numbers', 'Reverse a linked list', 'Merge two linked lists', 'Insertion sort',
                    'Quick sort', 'Merge sort', 'Factorial', 'Fibonacci']
    for i, func in enumerate(funcs_to_test):
        print('\t\t'+str(i+1)+'. '+func)
    print(line)
    while True:
        topt = int(input('Your choice: '))
        if topt == 1:
            ## Sum of first n numbers
            break
        elif topt == 2:
            ## Reverse a linked list
            break
        elif topt == 3:
            ## Merge two linked lists
            break
        elif topt == 4:
            ## Insertion sort
            break
        elif topt == 5:
            ## Quick sort
            break
        elif topt == 6:
            ## Merge sort
            break
        elif topt == 7:
            ## Factorial
            break
        elif topt == 8:
            ## Fibonacci
            break
        else:
            print('\n'+line)
            print('\tMake sure you select a valid option number.\n')

def dispRegistersW():
    print('\n\n'+line)
    print('---------------------------------- Registers ------------------------------------')
    print("\tHow do you want to get the registers?")
    print('\tBy date:\n\t\t1. Recent to Oldest\n\t\t2. Oldest to Recent')
    print('\t3. By author')
    print(line)
    
    while True:
        ropt = int(input('Your choice: '))
        if ropt == 1:
            ## Show registers by date recent to oldest
            break
        elif ropt == 2:
            ## Show registers by date oldest to recent
            break
        elif ropt == 3:
            ## Show registers by author name
            break
        else:
            print('\n'+line)
            print('\tMake sure you select a valid option number.\n')


if __name__ == '__main__':
    #To-run code. 
    menu()
        
