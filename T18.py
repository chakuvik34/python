
input_string = input("Enter a string: ")


index_not = input_string.find('not')
index_poor = input_string.find('poor')


if index_not != -1 and index_poor != -1 and index_poor < index_not:

    modified_string = input_string[:index_poor] + 'good' + input_string[index_not + 3:]
else:
    modified_string = input_string
print(f"The modified string is: {modified_string}")

