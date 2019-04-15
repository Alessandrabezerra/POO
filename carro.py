class Car:
  def __init__(self):
    self.passageiros = 0
    self.km = 0
    self.gasolina = 0
    self.limite_Pas = 2
    self.limite_Gas = 10
    
  def embarcar(self):
    if self.passageiros < self.limite_Pas:
      self.passageiros = self.passageiros + 1
    else:
     print("fail: limite de passageiros atingido")


  def tirar(self):
    if self.passageiros > 0:
      self.passageiros = self.passageiros - 1
    else:
      print("fail: nao ha ninguem no carro")
  
  def abastecer(self,qtd):
    self.gasolina = self.gasolina + qtd
    if (self.gasolina > self.limite_Gas):
      self.gasolina = self.limite_Gas
    
  def andar(self,distancia):
    if self.passageiros == 0:
      print("fail: nao ha ninguem no carro")
      return

    gas_necessario = distancia/10
    if (self.gasolina >= gas_necessario):
      self.km = self.km + distancia
      self.gasolina = self.gasolina - gas_necessario

    else:
      print("fail: gasolina insuficiente")          

  def __str__(self):
    return "passageiros: " + str (self.passageiros) + ", gasolina: " + str (self.gasolina) + ", km: " + str (self.km)

carro = Car ()
line = ""

print ("mostrar, embarcar, tirar, abastecer _quantidade, dirigir _distancia, fim")
while (line != "fim"):
  line = input()
  ui = line.split(" ")

  if ui[0] == "end":
    break
  elif ui[0] == "mostrar":
    print (carro)
  elif ui[0] == "embarcar":
    carro.embarcar()
  elif ui[0] == "tirar":
    carro.tirar() 
  elif ui[0] == "abastecer":
    carro.abastecer(int(ui[1]))
  elif ui[0] == "dirigir":
    carro.andar(int(ui[1]))
  else:
    print ("comando invalido!")    
