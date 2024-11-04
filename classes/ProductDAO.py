import mysql.connector

class ProductDAO():
  def __init__(self):
    pass

#colocar os dados do banco
  def conectar(self):
    conexao = mysql.connector.connect(
      host="",
      user="",
      password="",
      database=""
    )

    cursor = conexao.cursor()
    return conexao, cursor

#metodo que vai inserir produto
  def inserir(self,produto):
    self.produto = produto
    self.nome = produto.nome
    self.preco = produto.preco
    self.quantidade = produto.quantidade

    conexao, cursor = self.conectar()

    sql = "INSERT INTO produtos (nome,preco,quantidade) VALUES (%s,%s,%s)"
    valores = (self.nome,self.preco,self.quantidade)

    cursor.execute(sql,valores)

    conexao.commit()

    cursor.close()
    conexao.close()

#metodo para ler
  def ler(self):
    conexao, cursor = self.conectar()

    sql = "SELECT nome, preco, quantidade FROM produtos"
    cursor.execute(sql)
    produtos = cursor.fetchall()
    
    for produto in produtos:
      nome, preco, quantidade = produto 
      print(f"Nome: {nome}, Preço: {preco}, Quantidade: {quantidade}")

    cursor.close()
    conexao.close()

#metodo para deletar produtos(necessario passar o nome do produto)
  def deletar(self,nome):
  
    conexao, cursor = self.conectar()

    sql = "DELETE FROM produtos WHERE nome = %s"
    valores = (nome,)

    cursor.execute(sql,valores)

    conexao.commit()

    cursor.close()
    conexao.close()