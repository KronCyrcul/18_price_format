import sys


def format_price(price):
    price = str(price).replace(" ", "")
    if not price.replace(".", "", 1).isdigit():
        return None
    try:
        price = round(float(price), 2)
    except ValueError:
        return None

    #if price has zero fractional part
    if price-round(price) == 0:
        price = round(price)

    #if price has tenth part
    elif price-round(price, 1) == 0:
        price = round(price, 1)
    full_price = str("{:,}".format(price)).replace(",", " ")
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
        sys.exit(formated_price)
