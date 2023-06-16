def increase(price=0, tax=0, format=False):
    res = price + (price * tax / 100)
    if not format:
        return res
    else:
        return currency(res)


def decrease(price=0, tax=0, format=False):
    res = price - (price * tax / 100)
    if not format:
        return res
    else:
        return currency(res)


def double(price=0, format=False):
    res = price * 2
    if not format:
        return res
    else:
        return currency(res)


def half(price=0, format=False):
    res = price / 2
    if not format:
        return res
    else:
        return currency(res)


def currency(price=0, currency='R$'):
    return f'{currency} {price:>.2f}'.replace('.', ',')
