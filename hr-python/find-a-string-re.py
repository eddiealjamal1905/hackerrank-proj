# To time the speed of function.
from time import time
import re

def count_substring(string,sub_string):
    ''' Find the number of occurrences of a given substring in a given string.

    Args:
        string: Original string that we want to search.
        sub_string: The substring we want to search the original string for.

    Returns:
        Number of occurrences of the substring in the given string.
    '''

    matchlst = re.findall('(?=' + sub_string + ')', string)

    return len(matchlst)

print(count_substring('ABCDCDC', 'CDC'))