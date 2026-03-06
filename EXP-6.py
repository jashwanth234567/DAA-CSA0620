def process_list(lst):
    if not lst:
        return None

    lst.sort()
    return lst[-1]


data = [3,3,3,3,3]
print(process_list(data))
