

# Write a program that prints you a receipt for your new computer. 
# You will receive the parts' prices (without tax) until you receive what type of customer this is - special or regular. 
# Once you receive the type of customer you should print the receipt.
# The taxes are 20% of each part's price you receive. 
# If the customer is special, he has a 10% discount on the total price with taxes.
# If a given price is not a positive number, you should print "Invalid price!" on the console and continue with the next price.
# If the total price is equal to zero, you should print "Invalid order!" on the console.

# •	The receipt should be in the following format: 
# "Congratulations you've just bought a new computer!
# Price without taxes: {total price without taxes}$
# Taxes: {total amount of taxes}$
# -----------
# Total price: {total price with taxes}$"
# Note: All prices should be displayed to the second digit after the decimal point! 
# The discount is applied only on the total price. Discount is only applicable to the final price!

def receipt():
    total_price = 0
    command = input()
    while command != "special" and command != "regular":
        price = float(command)
        if price < 0:
            print("Invalid price!")
        else:
            total_price += price
        command = input()
    taxes = total_price * 0.2
    total_price += taxes
    if total_price == 0:
        print("Invalid order!")
    else:
        if command == "special":
            total_price *= 0.9
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_price:.2f}$")

result = receipt()


