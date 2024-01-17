# author: Jose Tellez and Joey Tran
def main():
    item_description = get_retail_item_description()
    number_purchased_items = get_number_purchased_items()
    usd_price = get_price_usd_per_unit()
    tax_rate = get_tax_rate()
    usd_subtotal = calculate_subtotal_usd(usd_price, number_purchased_items)
    usd_tax_amount = calculate_tax_amount(usd_subtotal, tax_rate)
    usd_total = calculate_total_usd(usd_subtotal, usd_tax_amount)
    display_sales_receipt(item_description, number_purchased_items, usd_price,
                          tax_rate, usd_subtotal, usd_tax_amount, usd_total)


def get_retail_item_description():
    retail_item_description = input("Enter retail item description: ")
    return retail_item_description


def get_number_purchased_items():
    item_quantity_sold = int(input("Enter quantity sold: "))
    return item_quantity_sold


def get_price_usd_per_unit():
    item_price_usd = float(input("Enter item price: "))
    return item_price_usd


def get_tax_rate():
    tax_rate = float(input("Enter tax rate: "))
    return tax_rate


def calculate_subtotal_usd(usd_price, quantity_sold):
    return usd_price*quantity_sold


def calculate_tax_amount(usd_subtotal, tax_rate):
    return usd_subtotal*tax_rate


def calculate_total_usd(usd_subtotal, usd_tax_amount):
    usd_total = usd_tax_amount + usd_subtotal
    return usd_total


def display_sales_receipt(item_description, quantity,
                          price_per_unit, tax_rate, subtotal,
                          tax_amount, total):
    print("Sales Receipt")
    print(f"Item Description: {item_description}")
    print(f"Number of Purchased Items: {quantity}")
    print(f"Unit Price (usd): {price_per_unit}")
    print(f"Tax Rate: {tax_rate}")
    print(f"Subtotal: {subtotal} (usd)")
    print(f"Subtotal: {tax_amount}(usd)")
    print(f"Total: {total}(usd)")


if __name__ == "__main__":
    main()


