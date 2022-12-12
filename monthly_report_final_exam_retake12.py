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



def print_report(total_income):
    for key in report:
        if report[key][1] == 0:
            continue
        print(f"{key}: {report[key][1]:.2f}")
    print("-----------")
    for key in report:
        if report[key][0] == 0:
            continue
        print(f"{key}: {report[key][0]:.2f}")
    print("-----------")
    print(f"Total Income: {total_income:.2f}")



def deliver(distributor, money):
    if distributor not in report:
        report[distributor] = [0, 0]
    report[distributor][0] += float(money)


def return_(distributor, money):
    if distributor not in report:
        # report[command[1]] = [0, 0]
        return
    report[distributor][0] -= float(money)
    if report[distributor][0] <= 0:
        del report[distributor]
    return report


def sell(client, money):
    total_income = 0
    if client not in report:
        report[client] = [0, 0]
    if report[client][0] < 0:
        return
    report[client][1] += float(money)
    total_income += float(money)
    return report, total_income


def get_command():
    command = input()
    if command == "End":
        print_report()
        return False
    command = command.split()
    if command[0] == "Deliver":
        deliver(command[1], command[2])
    elif command[0] == "Return":
        return_(command[1], command[2])
    elif command[0] == "Sell":
        sell(command[1], command[2])
    return True


def main():
    while get_command():
        pass
    return 0

if __name__ == "__main__":
    main()
