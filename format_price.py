import sys


def format_price(price)
    try:
        price = round(float(price), 2)
    except (ValueError,TypeError):
        return None
    price = int(price) if price.is_integer() else price
    full_price = "{:,}".format(price).replace(",", " ")
    return full_price


if __name__ == "__main__":
    try:
        price = sys.argv[1]
    except IndexError:
        sys.exit("Enter a price")
    formated_price = format_price(price)
    if formated_price is None:
        sys.exit("Wrong price")
    else:
        print(formated_price)
