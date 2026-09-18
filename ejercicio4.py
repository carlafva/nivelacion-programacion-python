# =====================================================================
# EJERCICIO 4 - FUNCIONES: Validador de contraseña temporal
# =====================================================================
# Contexto: Cuando soporte TI resetea la contraseña de un usuario, la
# contraseña temporal debe cumplir reglas mínimas de seguridad.
#
# TAREA:
# Completa la función validar_password(password) para que retorne:
#   True  -> si la contraseña cumple TODAS las reglas
#   False -> si no cumple alguna
# Reglas:
#   - Longitud mínima de 8 caracteres
#   - Al menos un número
#   - Al menos una letra mayúscula
#
# Pista: puedes recorrer los caracteres del password con un ciclo for,
# o investigar los métodos .isdigit() y .isupper() de los strings.
#
# RETO EXTRA:
# En vez de retornar solo True/False, haz que la función retorne un
# mensaje indicando cuál regla falló primero, por ejemplo:
#   "Error: la contraseña debe tener al menos 8 caracteres"
#   "Error: la contraseña debe incluir al menos un número"
#   "Error: la contraseña debe incluir al menos una mayúscula"
#   "Contraseña válida"
 
print("\n" + "=" * 60)
print("EJERCICIO 4: Validador de contraseña temporal")
print("=" * 60)
 
 
def validar_password(password):
    # TU CÓDIGO AQUÍ
    if len(password) <8:
        return "Error: la contraseña debe tener al menos 8 caracteres"
    elif not any(char.isdigit() for char in password):
        return "Error: la contraseña debe incluir al menos un número"
    elif not any(char.isupper() for char in password):
        return "Error: la contraseña debe incluir al menos una minúscula"
    else:
        return "Contraseña válida"
        pass

# Bloque de prueba (no modificar)
passwords_prueba = ["abc123", "abcdefg1", "Abcdefg1", "ABCDEFG1"]
for pw in passwords_prueba:
    print(f"'{pw}' : {validar_password(pw)}")