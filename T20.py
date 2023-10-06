def reverse_string_if_multiple_of_4(input_string):
   
    if len(input_string) % 4 == 0:
        
        reversed_string = input_string[::-1]
        return reversed_string
    else:
    
        return input_string


input_string = input("Enter a string: ")


result = reverse_string_if_multiple_of_4(input_string)

print("Result:", result)
