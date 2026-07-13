# Function to create dictionary
# arr is list of tuple. tuple contain name and marks.


def create_dict(arr):
    d = {}

    for name, marks in arr:
        d[name] = marks

    return d