

def order_totally(a,b):
    
    if order == 'coffee':
        total = count * 1.5

    elif order == 'water':
        total = count * 1

    elif order == 'coke':
        total = count * 1.4

    elif order == 'snacks':
        total = count * 2

    return total


order = input()
count = int(input())

print(order_totally(order,count))
