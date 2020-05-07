import doctest

def palindromic_squares(n = 100000000):
    """ 
    creates a list of all the palindromical 
    square numbers less than n

    >>> {1, 4, 9, 121, 484, 676, 10201} <= set(palindromic_squares(1000000000000))
    True
    """

    counter = 1
    squared = 1
    palindrome_list = []
    while squared < n:
        s = str(squared)
        if s == s[::-1]:
            palindrome_list.append(squared)
        counter += 1
        squared = counter * counter

    return palindrome_list

def find_even_len_palindromes(plist):
    """
    returns a list of all the pallindromes of
    plist, which have an even number of digits

    >>> find_even_len_palindromes(palindromic_squares(1000000000)) == [698896]
    True
    >>> 
   
    """
    even_len_list = []
    for i in plist:
        if not len(str(i)) % 2:
             even_len_list	.append(i)
    return even_len_list  


if __name__ == "__main__": 
    doctest.testmod()

