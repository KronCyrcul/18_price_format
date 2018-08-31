import sys


def format_price(price):
    price = str(price).replace(" ", "")
    if not price.replace(".", "", 1).isdigit():
        return None
    integer_part, *fractional_part = str.split(price, ".")
    fractional_part = fractional_part[0] if fractional_part else ""
    first_rank_counter = len(integer_part) % 3
    integer_part_digits = [i if (index+1) % 3 != first_rank_counter or
        index+1 == len(integer_part) else
        "{} ".format(i) for index, i in enumerate(integer_part)]
    integer_part = "".join(integer_part_digits)
    discard_count = 0
    for number in fractional_part[::-1]:
        if number is "0":
            discard_count += 1
        else:
            break
    fractional_part = fractional_part[:len(fractional_part)-discard_count]
    full_price = (".".join((integer_part, fractional_part)) if
        fractional_part is not "" else integer_part)
    return full_price


if __name__ == "__main__":
    price = sys.argv[1]
    formated_price = format_price(price)
    if formated_price is None:
        sys.exit("Wrong price")
    else:
        sys.exit(formated_price)
