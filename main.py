import random

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[39m'


puntaje= random.randint(0, 10)

print(GREEN+"!!!!!!!(ง︡'-'︠)งBienvenidos al juego de adivina el anime (ง︡'-'︠)ง!!!!!!!")
print("\nPondremos a prueba tu agilidad mental ≧◠ᴥ◠≦✊\n")
print("Comienzas temiendo ", puntaje, " puntos"+RESET)
 

nombre=input("\nIngresa tu nombre o tu apodo ٩(˘◡˘)۶ :\n")

print(RED+"\nHola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)

print (YELLOW+"\n1) ¿Cual es el anime en donde se usa un horno microondas como maquina del tiempo? (¬‿¬)\n"+RESET)
print ("a) Hack")
print ("b) Trigun")
print ("c) Stein Gate")
print ("d) Metabots")

respuesta_1 = input("\nTu respuesta: ")

while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_1 == "a":
  puntaje= puntaje + 5
  print("Incorrecto!", nombre, "Hack no usa un microondas para viajar en el tiempo")
  
  
elif respuesta_1 == "b":
  puntaje= puntaje/2
  print("Incorrecto!", nombre, "Trigun no usa un microondas para viajar en el tiempo")
  
  
elif respuesta_1 == "d":
  puntaje= puntaje/2
  print("Incorrecto!", nombre, "Metabots no usa un microondas para viajar en el tiempo")
 
  
else:
  puntaje= puntaje*2 
  
  print("\nExcelente la alternativa", respuesta_1, "!! es", nombre, "!")
 

print("\n",nombre, "llevas", puntaje, "puntos")




print (YELLOW+"\n2) ¿Cual es el anime en donde hay gigantes que destruyen murallas?  ≧◠ᴥ◠≦✊\n"+RESET)
print ("a) Shingeki no kyojin")
print ("b) Giants killing")
print ("c) kimetsu no yaiba")
print ("d) Inazuma Eleven")

respuesta_2 = input("\nTu respuesta: ")

while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_2 == "b":
  puntaje= puntaje + 5
  print("Incorrecto!", nombre, "Giants killing no hay gigantes que destruyen murallas ")
  
  
elif respuesta_2 == "c":
  puntaje= puntaje/2
  print("Incorrecto!", nombre, "Kimetsu no yaiba no hay gigantes que destruyen murallas ")
  
  
elif respuesta_2 == "d":
  puntaje= puntaje/2
  print("Incorrecto!", nombre, "Inazuma Eleven no hay gigantes que destruyen murallas ")
 
  
else:
  puntaje= puntaje*2 
  
  print("\nExcelente la alternativa", respuesta_2, "!! es", nombre, "!")
 

print("\n",nombre, "llevas", puntaje, "puntos")



print (YELLOW+"\n3) ¿Cual es el anime en donde la cancha de futbol es infinito? XD OK NO ES ASI (͠≖ ͜ʖ͠≖)👌 \n"+RESET)
print ("a) Super campeones")
print ("b) Giants killing")
print ("c) Area no kishi")
print ("d) Inazuma Eleven")

respuesta_3 = input("\nTu respuesta: ")

while respuesta_3 not in ("a", "b", "c", "d"):
  respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_3 == "b":
  puntaje= puntaje + 5
  print("Incorrecto!", nombre, "Giants killing no hay gigantes que destruyen murallas ")
  
  
elif respuesta_3 == "c":
  puntaje= puntaje/2
  print("Incorrecto!", nombre, "Kimetsu no yaiba no hay gigantes que destruyen murallas ")
  
  
elif respuesta_3 == "d":
  puntaje= puntaje/2
  print("Incorrecto!", nombre, "Inazuma Eleven no hay gigantes que destruyen murallas ")
 
  
else:
  puntaje= puntaje*2 
  
  print("\nExcelente la alternativa", respuesta_2, "!! es", nombre, "!")
 

print("\nFelicitaiones",nombre, "terminamos la trivia de anime tu puntaje es de ", puntaje, "puntos")

print("Muchas Gracias por jugar (>‿◠)✌")





 
  
    
