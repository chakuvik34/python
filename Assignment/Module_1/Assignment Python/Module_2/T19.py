def find_longest_word(l):
    if not l:
        return 0  
    
    longest_length = len(l[0])  
    
    for word in l :
        if len(word) > longest_length:
            longest_length = len(word)
    
    return longest_length


input_words = input("Enter a list of words separated by commas: ")


l = input_words.split(',')


l = [word.strip() for word in l]


longest_length = find_longest_word(l)


print(f"The length of the longest word is: {longest_length}")

