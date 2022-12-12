# Input
# •	The possible commands are:
# o	"End"
# o	"Deliver {DistributorName} {MoneySpend}"
# o	"Return {DistributorName} {MoneyReturned}"
# o	"Sell {ClientName} {MoneyEarned}"
# Output
# •	The possible outputs are:
# o	"{ClientName1}: {TotalMoneyEarnedFromThatCustomer1}
# {ClientName2}: {TotalMoneyEarnedFromThatCustomer2}
#  …
# {ClientNameN}: {TotalMoneyEarnedFromThatCustomer3}
# -----------
# {Distributor1}: {TotalMoneySpentToThatDistributor1}
# {Distributor2}: {TotalMoneySpentToThatDistributor2}
# …
# {DistributorM}: {TotalMoneySpentToThatDistributorM}
# -----------
# Total Income: {TotalMoneyEarnedFromCustomers}"

report = {}
total_income = 0

while True:
    command = input()
    if command == "End":
        break
    command = command.split()
    if command[0] == "Deliver":
        if command[1] not in report:
            report[command[1]] = [0, 0]
        report[command[1]][0] += float(command[2])
        
    elif command[0] == "Return":
        if command[1] not in report:
            # report[command[1]] = [0, 0]
            continue
        report[command[1]][0] -= float(command[2])
        
        if report[command[1]][0] <= 0:
            del report[command[1]]
    elif command[0] == "Sell":
        if command[1] not in report:
            report[command[1]] = [0, 0]
        report[command[1]][1] += float(command[2])
        total_income += float(command[2])


# print clients
# for key, value in report.items():
#     print(f"{key}: {value[1]}")
for key in report:
    if report[key][1] == 0:
        continue
    print(f"{key}: {report[key][1]:.2f}")

print("-----------")

# print distributors

for key in report:
    if report[key][0] == 0:
        continue
    print(f"{key}: {report[key][0]:.2f}")

print("-----------")

# print total income
print(f"Total Income: {total_income:.2f}")
