'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # If the word length is < 2 characters:
    
    if len(word) < 2:
        return 0
   
    # for  the first two characters , if it is not  'th', recurse count_th.
    if word[:2] != 'th':
        return count_th(word[1:])
    # if  it is 'th', count "1"      .
    else:
        return count_th(word[1:]) + 1
    
    
