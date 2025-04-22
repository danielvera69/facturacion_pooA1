class Comprehension:
  def __init__(self,car):
    self.caracteres=car
  def recorrido(self):
    lista = [valor for valor in 'examenrecuperacion' if valor not in self.caracteres] 
    diccionario = {ind:valor for ind,valor in enumerate(lista) if ind%2 ==0} 
    return diccionario
  
comp = Comprehension("aceious")
print(comp.recorrido())

tupla = (( 'POO', 50,20 ),( 'Logica', 10,30 ),( 'Calculo', 15,20 ),( 'Integral', 13,15 ))
print (tupla[2: 3] [-1]) 


