
import random 
with open('file_name.txt') as fr: 
    lines = fr.readlines() 
    random_line = random.choice(lines) if lines else None 
print(random_line)
