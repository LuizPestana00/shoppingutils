def calculate_total_price(cart):
    sum = 0
    for item in cart:
        sum += item['preco']
    return sum