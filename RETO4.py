from datetime import date
from itertools import product

class User:
  def __init__(self, id: int, user_name: str, balance: float):
    self.id= id
    self.name= user_name
    self.balance= balance
    self.order_list= []
    self.product_list=[]

  def add_product_to_car(self, product):
    self.product_list.append(product)       

  def consolidate_order(self, total):
    total= 0
    for i in self.product_list:
      total += i.price

    if self.balance >= total:
      print("Puede realizar el pago")
      total.product_list.append(self.product_list)
      self.order_list.append(total)
      total.status= True
        ##Crear orden, instanciar orden

    else:
      Answer= input("No le alcanza, ¿Desea agregar mas valor? SI/NO ")
      if Answer == "SI":
        Question= int(input("ingrese el valor: "))
        self.add_to_balance(Question)
        self.consolidate_order()
      else:
          print("Hasta la proxima compra :)")

  def add_to_balance(self, new_value):
    self.balance += new_value
                                  
  def plot_order_history(self, product):
    x=[]
    y=[]
    plt.style.use(['dark_background'])
    for i in product.price_history:
        x.append(i)
        y.append(product.price_history[i])

    if len(product.price_history)>1:
        plt.plot(x,y,linestyle="--",color="g",label=product.name)

    else:
        plt.bar(x,y,linestyle="--",color="g",label=product.name)
 
class Order:
  def __init__(self, id:int, date, total:float, status:bool):
    self.id= id
    self.date= date   #x
    self.total= total   #y
    self.status= status
    self.product_list= []


class Product:
  def __init__(self, id:int, name: str, price:float):
    self.id= id
    self.name= name
    self.price= price
    self.price_history= {date.today():price}

  def update_price(self, new_price:float, date):
    self.new_price= new_price
    self.price_history[date] = new_price

Producto1= Product(47466,"Arroz",5000)
Producto1.update_price(2500,date(2022,8,21))
Producto2= Product(64788,"TV",5000)
Producto2.update_price(6000,date(2022,6,11))
Producto3= Product(78388,"Azucar",2500)
Producto1.update_price(7000,date(2022,4,4))

Usuario1= User(7383,"Marco",2.8)
Usuario1.add_product_to_car(Producto1)
Usuario2= User(9292,"Laura",2.4)
Usuario3= User(9999,"Juan",4.5)


Usuario1.consolidate_order(200)


##Graficar fechas de la lista de orden, con el total de pago


