def secret(s):
    i = 0
    result = ''

    while s[i].isdigit():
        result = result + s[i]
        i = i + 1

    return result

#secret('abc123')
#secret('abc')
#secret('123abc')
#secret('123')

def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

values = [1, 2, 3]
#print(increment_items(values, 2))
#print(values)


def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
        result = result + s[i]
        i = i + 1

    return result

#mystery('123')
#mystery('123abc')
##mystery('abc')
#mystery('abc123')

playlist = ['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola']

def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.
    '''
    while playlist.count(song) >= 3:
        playlist.remove(song)
        
    print (playlist)

cap_song_repetition(playlist,"Lola")


    


