# To time the speed of function.
from time import time

def welcome_mat(length):
    ''' Print a welcome mat of dimension length x 3(length).

    Args:
        length: length of mat, in character size, must be an odd natural number.
    
    Returns:
        Printed version of a welcome mat.
    '''

    width = 3*length
    for  i in range(0,length):
        if i == length//2:
            numdash = int((width-len('WELCOME'))/2)
            print(numdash *'-' + 'WELCOME' + numdash * '-')
        else:
            s = i if i < length//2 else 2*(length//2)-i
            numvert = int(2*s + 1)
            numdash = int((width-3*numvert)/2)
            print(numdash * '-' + numvert*'.|.' + numdash * '-') 


if __name__ == "__main__":
    length = int(input('Please input the length: '))
    
    strt = time()
    welcome_mat(length)
    end = time()
    print('\n########################################\n########################################\n')
    print(f'Time taken: {end-strt}s')
