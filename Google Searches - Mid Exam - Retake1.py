# first line of input is the google income from a single search of a user
# second line of input is the number of users n
# next n lines are the number of searches of each user


# For the first user, we have one search, so we ignore the search. 
# We double the money from the second user: 10 * 5.5 * 2 = 110
# For the third user, we have 5 searches, so we triple the money per search (82.5).
# In the end, we get total money of 192.50.
# Output
# The possible outputs are:
# •	"Total money earned: {totalMoney}"

income = float(input())
number_users = int(input())
total_income = 0
count_users = 0

for i in range(number_users):
    count_users += 1
    counts = int(input())
    if counts==1:
        continue 
    # if i%3==0 and counts[i]>5
    if count_users%3==0 and counts>5:
        total_income += income * counts * 2 * 3
    elif count_users%3==0 and counts<5:
        total_income += income * counts * 3
    elif count_users%3==0 and counts==1:
        continue
    elif count_users%3==0:
        total_income += income * counts * 3
    elif counts>5:
        total_income += income * counts * 2
    else:
        total_income += income * counts

print(f"Total money earned: {total_income:.2f}")


# def income_calculation(counts):
#     if count_users%3==0 and counts>=5:
#         total_income += income * counts * 2 * 3
#     elif count_users%3==0 and counts<5:
#         total_income += income * counts * 3
#     elif count_users%3==0 and counts==1:
#         continue
#     elif count_users%3==0:
#         total_income += income * counts * 3
#     elif counts>5:
#         total_income += income * counts * 2
#     else:
#         total_income += income * counts

# def count_users_calculation():
#     count_users += 1
#     counts = int(input())
#     if counts==1:
#         continue 
#     else:
#         income_calculation(counts)

# def main():
#     while count_users < number_users:
#         count_users_calculation()
#     print(f"Total money earned: {total_income:.2f}")

# main()

# while count_users < number_users:
#     count_users += 1
#     counts = int(input())
#     if counts==1:
#         continue 
#     # if i%3==0 and counts[i]>5
#     if count_users%3==0 and counts>=5:
#     # if counts.index[i]%3==0 and counts[i]>=5:
#         total_income += income * counts * 2 * 3
#     if count_users%3==0 and counts<5:
#         total_income += income * counts * 3
#     if count_users%3==0 and counts==1:
#         continue
    
#     # every third user gets tripled income
#     if count_users%3==0:
#         total_income += income * counts * 3
#     if counts>5:
#         total_income += income * counts * 2
#     else:
#         total_income += income * counts

# print(f"Total money earned: {total_income:.2f}")

# for i in range(number_users):
#     count_users += 1
#     counts = int(input())
#     if counts==1:
#         continue 
#     # if i%3==0 and counts[i]>5
#     if count_users%3==0 and counts>=5:
#     # if counts.index[i]%3==0 and counts[i]>=5:
#         total_income += income * counts * 2 * 3
#     if count_users%3==0 and counts<5:
#         total_income += income * counts * 3
#     if count_users%3==0 and counts==1:
#         continue
    
#     # every third user gets tripled income
#     if count_users%3==0:
#         total_income += income * counts * 3
#     if counts>5:
#         total_income += income * counts * 2
#     else:
#         total_income += income * counts

# print(f"Total money earned: {total_income:.2f}")

# for i in range(count_users):
#     counts = int(input())
#     if counts==1:
#         continue 
#     # if i%3==0 and counts[i]>5
#     if i%3==0 and counts>=5:
#     # if counts.index[i]%3==0 and counts[i]>=5:
#         total_income += income * counts * 2 * 3
#     if i%3==0 and counts<5:
#         total_income += income * counts * 3
#     if i%3==0 and counts==1:
#         continue
    
#     # every third user gets tripled income
#     if i%3==0:
#         total_income += income * counts * 3
#     if counts>=5:
#         total_income += income * counts * 2
#     else:
#         total_income += income * counts
        
# print(f"Total money earned: {total_income:.2f}")



# for i in range(count_users):
#     counts.append(int(input()))
#     if counts[i]==1:
#         continue 
#     # if i%3==0 and counts[i]>5
#     if counts.index(i+1)%3==0 and counts[i]>=5:
#     # if counts.index[i]%3==0 and counts[i]>=5:
#         total_income += income * counts[i] * 2 * 3
#     if counts.index(i+1)%3==0 and counts[i]<5:
#         total_income += income * counts[i] * 3
#     if counts.index(i+1)%3==0 and counts[i]==1:
#         continue
    
#     # every third user gets tripled income
#     if counts.index(i+1)%3==0:
#         total_income += income * counts[i] * 3
#     if counts[i]>=5:
#         total_income += income * counts[i] * 2
#     else:
#         total_income += income * counts[i]

# print(f"Total money earned: {total_income:.2f}")

# for i in range(count_users):
#     counts.append(int(input()))
#     if counts[i]==1:
#         continue 
#     # if i%3==0 and counts[i]>5
#     if counts.index(i)%3==0 and counts[i]>=5:
#     # if counts.index[i]%3==0 and counts[i]>=5:
#         total_income += income * counts[i] * 2 * 3
#     if counts.index(i)%3==0 and counts[i]<5:
#         total_income += income * counts[i] * 3
#     if counts.index(i)%3==0 and counts[i]==1:
#         continue
    
#     # every third user gets tripled income
#     if counts.index(i)%3==0:
#         total_income += income * counts[i] * 3
#     if counts[i]>=5:
#         total_income += income * counts[i] * 2
#     else:
#         total_income += income * counts[i]

print(f"Total money earned: {total_income:.2f}")
