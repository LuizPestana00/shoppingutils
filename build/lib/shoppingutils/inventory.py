def check_availability(cart, inventory):
    for item in cart:
        if inventory[item['produto']] == 0:
            return False
    return True

            