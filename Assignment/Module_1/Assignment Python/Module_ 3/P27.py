def list_of_tuples_to_dict(tuple_list):
    return {key: value for key, value in tuple_list}

# Example usage:
tuple_list = [('a', 1), ('b', 2), ('c', 3)]
result = list_of_tuples_to_dict(tuple_list)
print(result)
