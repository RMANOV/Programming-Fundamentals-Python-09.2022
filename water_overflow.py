
number_lines = int(input())
capacity = 255
water = 0
for i in range(number_lines):
    liters = int(input())
    if water + liters <= capacity:
        water += liters        
    else:
        print('Insufficient capacity!')
print(water)






# while True:
#     water_in = int(input("Enter the amount of water in the bucket: "))
#     if water_in > capacity:
#         print("The bucket is full.")
#         break
#     water += water_in
#     if water > capacity:
#         print("The bucket is full.")
#         break
#     print("The amount of water in the bucket is {}.".format(water))
#     print("The amount of water left in the bucket is {}.".format(capacity - water))
