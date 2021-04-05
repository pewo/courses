#def count_vowels(str):
#    for i in range(len(str)):
#        print(i,str[i])
#        if str[i] in 'abcd':
#            print("*")
#
#
#count_vowels("abrakadabra")
#
#x = 2
#y = 3 - x
#x = 3

#def f(y):
#    x = y * 3
#    return y + x
#
#print(f(10))

# 4
#start = 'L'
#middle = 8
#end = 'R'
#start + str(middle) + end

# 5
def larger_of_smallest(L1, L2):
    '''(list of int, list of int) -> int

    Return the larger of the smallest value in L1 and the smallest value in
    L2.

    Precondition: L1 and L2 are not empty.

    >>> larger_of_smallest([1, 4, 0], [3, 2])
    2
    >>> larger_of_smallest([4], [9, 6, 3])
    4
    '''

    return max(min(L1),min(L2))


def same_length(L1, L2):
    '''(list, list) -> bool

    Return True if and only if L1 and L2 contain the same number of elements.
    '''
    return len(L1) == len(L2)
    #if len(L1) == len(L2):
    #    return True
    #else:
    #    return False


def burble(a, b):
    '''(int, float) -> str'''
    return "x"

def snorgle(L):
    '''(list of str) -> float
    Precondition: L has at least one element.'''
    return 3.14

# fel burble( snorgle(['a', 'b', 'c'])    , 8 // 3)
# ok snorgle( [burble(1, 1.0), 'b' ])
# ok burble(8 // 3, snorgle(['a', 'b', 'c']))
# fel burble(burble(1, 1.0), 'b')


def gather_every_nth(L, n):
    '''(list, int) -> list

    Return a new list containing every n'th element in L, starting at index 0.

    Precondition: n >= 1

    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)
    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
    ['a', 'c', 'e', 'g', 'i']
    '''

    result = []
    i = 0
    while i < len(L):
        result.append(L[i])
        i = i + n

    return result

#print(gather_every_nth([0, 1, 2, 3, 4, 5], 3))
#print(gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2))

def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    '''

    result = []
    for k in L:
        if k in d:
            result.append(k)

    return result


#print(get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'}))

def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool

    Return True if and only if all the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    '''

    result = True
    for i in range(len(L1)):
        print(i,L1[i],len(L2[i]))
        if L1[i] != len(L2[i]):
            result = False
    return result

#print(are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef']))

def double_values(collection):
    for v in range(len(collection)):
        print("v=",v," value=",collection[v])
        collection[v] = collection[v] * 2

#d = {0: 10, 1: 20, 2: 30}
#double_values(d)
#
## kass string
##s = '123'
##double_values(s)
#
## kass tuple
##t = (1, 2, 3)
##double_values(t)
#
## kass index out of range no d[0]
##d = {1: 10, 2: 20, 3: 30}
##double_values(d)
#
#L = [1, 2, 3]
#double_values(L)

def get_diagonal_and_non_diagonal(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):
            print("row=",row," col=",col," value=", L[row][col])
            #if row == col:
            #    diagonal.append(L[row][col])
            #if row != col:
            #    non_diagonal.append(L[row][col])

            #if row == col:
            #    diagonal.append(L[row][col])
            #elif row != col:
            #    non_diagonal.append(L[row][col])

            #if row == col:
            #    diagonal.append(L[row][col])
            #
            #non_diagonal.append(L[row][col])

            if row == col:
                diagonal.append(L[row][col])
            else:
                non_diagonal.append(L[row][col])

           
    return (diagonal, non_diagonal)

#print(get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]]))

def count_chars(s):
    '''(str) -> dict of {str: int}

    Return a dictionary where the keys are the characters in s and the values
    are how many times those characters appear in s.

    >>> count_chars('abracadabra')
    {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
    '''
    d = {}
    a = {}

    for c in s:
        if not (c in d):
            d[c] = 1
        else:
            d[c] += 1

    return d

print(count_chars('abracadabra'))
