# =====================================================================
# EJERCICIO 3 - CICLOS: Cola de tickets pendientes
# =====================================================================
# Contexto: Hay una lista de tickets pendientes que deben procesarse en
# orden durante la jornada laboral (8 horas = 480 minutos).
#
# TAREA:
# Recorre la lista `tickets_pendientes` (ya definida abajo) e imprime cada
# ticket con su id y minutos estimados. Ve acumulando el tiempo total
# usado en una variable (ejemplo: tiempo_acumulado).
# Al final, imprime el tiempo total acumulado.
#
# RETO EXTRA:
# Si en algún momento el tiempo acumulado supera 480 minutos, detén el
# procesamiento con `break` e imprime cuántos tickets quedaron sin atender.
 
print("\n" + "=" * 60)
print("EJERCICIO 3: Cola de tickets pendientes")
print("=" * 60)
 
tickets_pendientes = [
    {"id": 101, "minutos": 45},
    {"id": 102, "minutos": 90},
    {"id": 103, "minutos": 60},
    {"id": 104, "minutos": 120},
    {"id": 105, "minutos": 100},
    {"id": 106, "minutos": 80},
    {"id": 107, "minutos": 30},
]
 
# TU CÓDIGO AQUÍ
tiempo_acumulado = 0

for ticket in tickets_pendientes:
    tiempo_acumulado += ticket["minutos"]
    print(f"tickets ID: {ticket['id']}), minutos estimados: {ticket['minutos']}")

    if tiempo_acumulado > 480:
            print("tiempo acumulado excede 480 minutos. Deteniendo procedimiento")
            break