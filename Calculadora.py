class Calculadora():
    def __init__(self, batmax):
        self.bateria = 0
        self.batmax = batmax
    
    def soma(self, a,b):
        if(self.bateria > 0):
            self.bateria -= 1
            return a+b
        else: 
            return "Bateria insuficiente"
        
    def div(self, a, b):
        if(self.bateria > 0):
            self.bateria -= 1
            if (b == 0):
                return "Divisão por 0"
            return a/b
        else: 
            return "Bateria insuficiente"
    
    def mult(self, a, b):
        if self.bateria > 0:
            self.bateria -= 1
            return a*b
        else: 
            return "Bateria insuficiente"
    
    def recarga(self, m):
        if (m<= self.batmax):
            self.bateria += m
    
    def __str__(self):
      return "bateria: " + str(self.bateria) + "/" + str(self.batmax)


calc = Calculadora(0)

print ("Digite inicio _batmax, recarga _valor, soma, div, mult, mostrar ou fim")
line = " "
while line != "fim":
  line = input()
  ui = line.split(" ")
  
  if ui[0] == "fim":
    break
  elif ui[0] =="mostrar":
    print(calc)
  elif ui[0] == "inicio":
    calc.batmax = int(ui[1])
  elif ui[0] == "recarga":
    calc.recarga(int(ui[1]))
  elif ui[0] == "soma":
    a = (int(ui[1]))
    b = (int(ui[2]))
    print(calc.soma(a,b))
  elif ui[0] == "div":
    a = (int(ui[1]))
    b = (int(ui[2]))
    print(calc.div(a,b))
  elif ui[0] == "mult":
    a = (int(ui[1]))
    b = (int(ui[2]))
    print(calc.mult(a,b))
  else:
    print ("Comando invalido") 
    
