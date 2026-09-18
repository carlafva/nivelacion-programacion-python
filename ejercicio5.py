# =====================================================================
# EJERCICIO 5 - INTEGRADOR: Mini sistema de tickets
# =====================================================================
# Contexto: Ahora vas a combinar variables, condicionales, ciclos y
# funciones en un solo mini-sistema.
#
# TAREA:
# Completa la función procesar_tickets(lista_tickets) que:
#   1. Recorra la lista de tickets (cada uno es un diccionario con
#      "id" y "usuarios_afectados")
#   2. Para cada ticket, calcule su prioridad reutilizando la misma
#      lógica del Ejercicio 2 (puedes copiar/adaptar el código en una
#      función auxiliar clasificar_prioridad(usuarios))
#   3. Imprima cada ticket con su prioridad calculada
#   4. Al final, imprima un resumen con cuántos tickets hay de cada
#      prioridad (Baja, Media, Alta, Crítica)
 
print("\n" + "=" * 60)
print("EJERCICIO 5: Mini sistema de tickets")
print("=" * 60)
 
tickets_del_dia = [
    {"id": 201, "usuarios_afectados": 1},
    {"id": 202, "usuarios_afectados": 5},
    {"id": 203, "usuarios_afectados": 25},
    {"id": 204, "usuarios_afectados": 80},
    {"id": 205, "usuarios_afectados": 3},
]
 
 
def clasificar_prioridad(usuarios):
    # TU CÓDIGO AQUÍ (reutiliza la lógica del Ejercicio 2)
    if usuarios == 1:
        prioridad = "Baja"
    elif usuarios >= 2 and usuarios <= 10:
        prioridad = "Media"
    elif usuarios >= 11 and usuarios <= 50:
        prioridad = "Alta"
    elif usuarios > 50:
        prioridad = "Crítica"
    else:
        prioridad = "Número de usuarios no válido"
    return prioridad
 
 
def procesar_tickets(lista_tickets):
    resumen = {
        "Baja": 0,
        "Media": 0,
        "Alta": 0,
        "Crítica": 0
    }
 
    for ticket in lista_tickets:
        prioridad = clasificar_prioridad(ticket["usuarios_afectados"])
 
        print(f"Ticket ID: {ticket['id']}, Prioridad: {prioridad}")
 
        resumen[prioridad] += 1
 
    print("\nResumen de tickets:")
    for prioridad, cantidad in resumen.items():
        print(f"{prioridad}: {cantidad}")
 
 
procesar_tickets(tickets_del_dia)
 