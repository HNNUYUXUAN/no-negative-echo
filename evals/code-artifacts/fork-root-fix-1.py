def price(total, discount):
    if (
        not isinstance(total, int)
        or total < 0
        or not isinstance(discount, int)
        or not 0 <= discount <= 100
    ):
        raise ValueError()
    return total * (100 - discount) / 100
