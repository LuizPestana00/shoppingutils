pip install git+https://github.com/LuizPestana00/shoppingutils.git

O package shoppingutils tem como propósito fornecer operações básicas de gestão de compras de clientes. 

O package possui 3 ficheiros:
- cart.py:
      Este ficheiro possui a 'calculate_total_price(cart)' que recebe como parâmetro uma lista de itens do carrinho (cart) que retorna o preço total dos itens, onde a estrutura é um dicionário que possui as chaves 'produto' e 'preco'.
- discount.py:
      Este ficheiro possui uma função chamada 'apply_discount(cart, discount)' que recebe como parâmetro uma lista dos itens do carrinho de compra (a estrutura dos itens é a mesma utilizada no calculate_total_price) e o desconto que será aplicado a todos os itens, e devolve a lista dos itens com os descontos aplicados.
- inventory.py:
      Este ficheiro possui uma função chamada 'check_availability(cart, inventory)' que recebe como parâmetro uma lista dos itens do carrinho de compra (a estrutura dos itens é a mesma utilizada no calculate_total_price) e um dicionário com os produtos e a quantidade disponível em stock, a estrutura deste dicionário é composta pelos nomes dos produtos como chave e a quantidade de produtos disponíveis. Esta função retorna se os produtos estão disponíveis ou não.

Ex: 
from shoppingutils.cart import calculate_total_price
from shoppingutils.discount import apply_discount
from shoppingutils.inventory import check_availability

inventory = {'teste' : 1, 'caneta' : 2, 'lapis' : 0}
lista = [{'produto' : 'teste', 'preco' : 100}, {'produto' : 'caneta', 'preco' : 10}, {'produto' : 'lapis', 'preco' : 20}]

print(calculate_total_price(lista))
print(apply_discount(lista, 10))
print(check_availability(lista, inventory))