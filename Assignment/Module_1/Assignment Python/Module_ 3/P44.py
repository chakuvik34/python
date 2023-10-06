def is_palindrome(input_str):
    cleaned_str = ''.join(input_str.split()).lower()
    
    return cleaned_str == cleaned_str[::-1]
user_input = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(user_input):
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
