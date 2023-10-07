
file_path = 'your_file.txt' 
n = int(input("Enter the number of lines to read: "))

try:
    
    with open(file_path, 'r') as file:
    
        for _ in range(n):
            line = file.readline()
            if not line:
                break  
            print(line, end='')

except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
