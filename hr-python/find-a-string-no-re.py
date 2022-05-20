# To time the speed of function.
from time import time

def count_substring(string,sub_string):
    ''' Find the number of occurrences of a given substring in a given string.

    Args:
        string: Original string that we want to search.
        sub_string: The substring we want to search the original string for.

    Returns:
        Number of occurrences of the substring in the given string.
    '''

    matchlst = ([i for i in range(len(string) - len(sub_string) + 1) 
                            if sub_string == string[i:i+len(sub_string)]])

    return len(matchlst)

if __name__ == '__main__':
    string = input('Please enter the original string: ').strip()
    sub_string = input('Please enter the substring: ').strip()
    
    strt = time()
    count = count_substring(string, sub_string)
    end = time()

    print(f"Number of occurences of the substring {sub_string} in {string} is {count}.")
    print('\n########################################\n########################################\n')
    print(f'Time take: {end-strt}s')
    print('\n########################################\n########################################\n')