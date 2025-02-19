
nested_list = [[1, 2, [3, 4]], [5, 6], [7, [8, 9]]]

def flatten_list(nested):
    flat_list = []
    for element in nested:
        # isinstance is builtin func for true or false
        if isinstance(element, list):
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list

flattened = flatten_list(nested_list)

print(flattened)
