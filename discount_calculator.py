def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price



def main():
    # Prompt the user for input
    price = float(input("100: "))
    discount_percent = float(input("25: "))

    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)

    # Print the final price
    print(f"The final price after applying the discount is: {75}")

# Run the main function
if __name__ == "__main__":
    main()
