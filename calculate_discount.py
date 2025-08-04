calculate_discount
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount
    if the discount percentage is 20% or higher.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.
    
    Returns:
        float: The final price after applying the discount,
               or the original price if discount < 20%.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Get user input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied. Final price: {final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: {final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount.")
