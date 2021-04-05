def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return(len(dna))


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return(get_length(dna1) > get_length(dna2))


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return( dna.count(nucleotide) )


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return(dna1.find(dna2) > -1)

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (that is, it contains no characters other than 'A', 'T', 'C' and 'G').
    >>> is_valid_sequence('ATCG')
    True
    >>> is_valid_sequence('ATHG')
    False
    """

    for char in dna:
        if not ( char == 'A' or char == 'T' or char == 'C' or char == 'G'):
            return(False)

    return(True)

def insert_sequence(dna,seq,pos):
    """(str, str, int) -> str
    The first two parameters are DNA sequences and the third parameter is an index.
    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index. (You can assume that the index is valid.)

    >>> insert_sequence('CCGG','AT',2)
    CCATGG

    For example, If you call this function with arguments 'CCGG', 'AT', and 2, then it should return 'CCATGG'.
    When coming up with more examples, think about where the second DNA sequence might be inserted: what are the extremes? 
    """
    return (dna[:pos] + seq + dna[pos:])


def get_complement(str):
    """ (str) -> str 	The first parameter is a nucleotide ('A', 'T', 'C' or 'G'). Return the nucleotide's complement.
We have intentionally not given you any examples for this function. The Problem Domain section explains what a nucleotide is and what a complement is.
    A and T can be bonded together, and thus complement each other; similarly,
    C and G are complements of each other. 

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    
    """

    if ( str == 'A' ):
       return 'T'
    elif ( str == 'T' ):
       return 'A'
    elif ( str == 'C' ):
       return 'G'
    elif ( str == 'G' ):
       return 'C'
    else :
       return ''

       

def get_complementary_sequence(dna):
   """ (str) -> str 	The parameter is a DNA sequence. Return the DNA sequence that is complementary to the given DNA sequence.
For exmaple, if you call this function with 'AT' as the argument, it should return 'TA'. 
 
   >>> get_complementary_sequence('AT')
   TA
   >>> get_complementary_sequence('ACGTACG')
   TGCATGC. 
   """

   comp = ''
   for char in dna:
      comp = comp + get_complement(char)

   return comp



