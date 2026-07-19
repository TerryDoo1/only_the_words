import function

#separates words and stores them in a list
sentence = input("what is your sentence? ")
words = function.get_words(sentence)

#Remove punctuation from the beginning and end of each word
for i in range(len(words)):
    if not function.is_char(words[i][0]):
        words[i] = words[i][1:]
    if not function.is_char(words[i][-1]):
        words[i] = words[i][:-1]

#converts list into a string and prints
final = ""
for i in words:
    final = final + i + " "

print(f'{final} ')
