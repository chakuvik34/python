def get_largest_smallest_sum(numbers):
    if not numbers:
        return None, None, 0
    
    largest = smallest = numbers[0]
    total_sum = 0
    
    for num in numbers:
        total_sum += num
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    
    return largest, smallest, total_sum

number_list = [12, 5, 8, 27, 3, 15]

largest_num, smallest_num, sum_of_all = get_largest_smallest_sum(number_list)

print("Largest Number:", largest_num)
print("Smallest Number:", smallest_num)
print("Sum of All Numbers:", sum_of_all)
