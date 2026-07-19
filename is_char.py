def get_words(string):
    """Return a list of words from the input string, splitting at spaces."""
    words = []
    temp = ""
    # a space marks the end of a word
    for i in string:
        if i == " ":
            if temp != " " and temp != "":
                words.append(temp)
            temp = ""
        else:
            temp += i
    #adds last word as the loop ends without a space
    if temp != " " and temp != "":
        words.append(temp)
    
    return words
    
def is_char(char):
    """Returns False if the character is punctuation, True otherwise"""
    punctuation = [",", ".", "'", "?", "-", "!", ":", ";"]
    return char not in punctuation
