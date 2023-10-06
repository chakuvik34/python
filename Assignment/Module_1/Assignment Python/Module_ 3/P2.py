def count_strings_with_same_first_last_character(string_list):
    count = 0
    
    for string in string_list:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    
    return count


input_strings = input("Enter a list of string: ")


string_list = input_strings.split(',')


string_list = [string.strip() for string in string_list]


count = count_strings_with_same_first_last_character(string_list)

print("Number of strings with the same first and last character:", count)
