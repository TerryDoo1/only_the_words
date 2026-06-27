def is_function(char):
    puncuation = [",", ".", "'", "?", "-", "!", ":", ";"]
    for i in puncuation:
        if char == i:
            return False
            break
    return True
