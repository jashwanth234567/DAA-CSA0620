def unique_elements(lst):
    unique = []

    for i in lst:
        if i not in unique:
            unique.append(i)

    return unique


data = [3,7,3,5,2,5,9,2]
print(unique_elements(data))
