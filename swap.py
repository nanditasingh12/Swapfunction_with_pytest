#def swap_without_temp(a, b):
    #a, b = b, a
    #return a, b

# Take user input
def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


