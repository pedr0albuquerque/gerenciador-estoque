from classes.Product import Product 

name = str(input("insira o nome do produto"))    
price = float(input("insira o preço do produto"))
quantity = int(input("insira quantidade do produto"))

product = Product(name, price, quantity)
print(product.getter())