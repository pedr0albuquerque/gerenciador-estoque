#classe pra inserir o produto no banco
class ProductDAO():
  def __init__(self):
    pass

#metodo que vai pegar um produto e seu valores e guardar em um banco de dados
#obs: pode ser que esteja errado a sintaxe
  def insert(self,product):
    self.product = product
    self.name = product.name
    self.price = product.price
    self.quantity = product.quantity