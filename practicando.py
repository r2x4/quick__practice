# estructuras de control

edad = 15

if edad < 18:
    print("Es menor de edad")

elif edad >= 18 and edad < 60:
    print("Eres un Adulto")

elif edad > 15:  # esta afecta la secuencia
    print("Mayor de 15 Anos ")

elif edad == 60:
    print("Feliz cumple 60")

else:
    print("Eres un adulto Mayor")
    
 # otro ejercicio
 
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)