def apply_discount(cart, discount):
    list = []
    for item in cart:
        novo_item = {}
        novo_item['produto'] = item['produto']
        novo_item['preco'] = item['preco'] - (item['preco'] * (discount/100))
        list.append(novo_item)
    return list