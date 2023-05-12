
#return the sum of all numbers in the list values
def add(values):
    total = (sum(values))
    return total


#return the difference of all the numbers in the list values
def subtract(values):
    total = values[0]
    for n in values[1:]:
        total -= n
    return total


#return the product of all the numbers in the list values
def multiply(values):
    total = values[0]
    for n in values[1:]:
        total *= n
    return total


#return the result of dividing all the numbers in the list values.

def divide(values):
    if values[0] == 0 and 0 not in values[1:]:
        total = 0
    elif 0 in values[1:]:
        print('Cannot divide by 0')
    else:
        total = values[0]
        for n in values[1:]:
            total /= n
    return total

