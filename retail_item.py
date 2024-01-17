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
    """
    Receives user input for item description
    :return: retail item description as string
    """
    retail_item_description = input("Enter retail item description: ")
    return retail_item_description


def get_number_purchased_items():
    """
    Receives user input for number of purchased items
    :return: number of purchased items as int
    """
    item_quantity_sold = int(input("Enter quantity sold: "))
    return item_quantity_sold


def get_price_usd_per_unit():
    """
    Receives user input for unit price in usd
    :return: unit price in usd as float
    """
    item_price_usd = float(input("Enter item price: "))
    return item_price_usd


def get_tax_rate():
    """
    Receives user input for tax rate
    :return:tax rate as float
    """
    tax_rate = float(input("Enter tax rate: "))
    return tax_rate


def calculate_subtotal_usd(usd_price, quantity_sold):
    """
    Calculates the sale subtotal
    :param usd_price: unit price in usd
    :param quantity_sold: total quantity of items sold
    :return: sale subtotal as float
    """
    return usd_price*quantity_sold


def calculate_tax_amount(usd_subtotal, tax_rate):
    """
    Calculates amount of tax due in USD
    :param usd_subtotal: sale subtotal in USD as float
    :param tax_rate: tax rate as float
    :return:subtotal as float
    """
    return usd_subtotal*tax_rate


def calculate_total_usd(usd_subtotal, usd_tax_amount):
    """
    Calculates sale total in USD
    :param usd_subtotal: sale subtotal in USD as float
    :param usd_tax_amount: tax amount in USD as float
    :return: Sale total as float
    """
    usd_total = usd_tax_amount + usd_subtotal
    return usd_total


def display_sales_receipt(item_description, quantity,
                          price_per_unit, tax_rate, subtotal,
                          tax_amount, total):
    """
    Displays sale receipt in the required format
    :param item_description: item description as string
    :param quantity: item quantity as int
    :param price_per_unit: unit price in usd as float
    :param tax_rate: tax rate as float
    :param subtotal: sale subtotal
    :param tax_amount: tax amount in usd as float
    :param total: sale total in usd as float
    :return: None
    """
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


