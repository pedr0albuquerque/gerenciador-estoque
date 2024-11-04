from classes.Product import Product 
from classes.ProductDAO import ProductDAO

nome = str(input("insira o nome do produto"))   
preco = float(input("insira o preço do produto"))
quantidade = int(input("insira quantidade do produto"))

produto = Product(nome, preco, quantidade)
produtoDAO = ProductDAO()

'''produtoDAO.inserir(produto)
produtoDAO.ler
produtoDAO.deletar("")'''