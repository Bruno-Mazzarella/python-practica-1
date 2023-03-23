from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-","*","/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
cont_1=0 #inicializo el contador para las respuestas correctas
cont_2=0 #inicializo el contador para las respuestas incorrectas 
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    operator = choice(operators)
    number_2 = randrange(10)
    #veo el resultado correcto en cada caso
    if operator == "+": 
        result_correcto=number_1+number_2
    elif operator == "-" : 
        result_correcto=number_1-number_2
    elif operator == "*":
        result_correcto=number_1*number_2
    elif operator == "/": #aca miro que no sea una divicion por cero
        number_2 = randrange(1,10)
        result_correcto=number_1/number_2
    #ahora pido el resultado del jugador 
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    result = float(input("resultado: "))
    #comparo los resultados
    if result_correcto == result :
            print ("el resultado es correcto")
            cont_1 += 1 #contador para las respuestas correctas
    else:
            print ("el resultado es incorrecto")
            cont_2 += 1 #contador para las respuestas incorrectas
#aca imprimo los resultados
print("RESULTADOS:")
print("cantidad de aciertos:", cont_1, " :)")
print("cantidad de errores:", cont_2, " :(")
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")

