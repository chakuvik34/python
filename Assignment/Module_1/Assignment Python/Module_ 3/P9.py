def find_second_smallest(numbers):
    if len(numbers) < 2:
        print("List must two elements")
        return

    smallest = float('inf')
    second_smallest = float('inf')

    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    if second_smallest == float('inf'):
        print(" no second smallest element list")
    else:
        print("second smallest number is:", second_smallest)

my_list = [12, 45, 2, 41, 31, 10, 8]
find_second_smallest(my_list)
