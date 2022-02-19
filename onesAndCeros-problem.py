def binary_array_to_number(arr):
    string = []
    for char in arr:
        string.append(str(char))
        
    string = "".join(string)
    return int(string,2)