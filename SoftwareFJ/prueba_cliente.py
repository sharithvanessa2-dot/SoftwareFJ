
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: prueba_cliente.py
# DESCRIPCION: Pruebas de registro de clientes.
# =====================================================

from cliente import Cliente
from excepciones import DatosInvalidosError


print("======================================")
print("     SISTEMA SOFTWARE FJ")
print("       PRUEBAS DE CLIENTES")
print("======================================")


# PRUEBA 1: Registro de cliente valido.

print("\nPRUEBA 1: Registro de cliente valido")

try:
    cliente1 = Cliente(
        "C001",
        "Carlos Perez",
        "1090123456",
        "3001234567",
        "carlos@gmail.com"
    )

    print("Cliente registrado correctamente.")
    print(cliente1.mostrar_informacion())

except DatosInvalidosError as error:
    print("Error de validacion:", error)


# PRUEBA 2: Registro con nombre invalido.

print("\nPRUEBA 2: Registro con nombre invalido")

try:
    cliente2 = Cliente(
        "C002",
        "Jo",
        "1090123457",
        "3001234568",
        "juan@gmail.com"
    )

except DatosInvalidosError as error:
    print("Error controlado correctamente:", error)


# PRUEBA 3: Registro con correo invalido.

print("\nPRUEBA 3: Registro con correo invalido")

try:
    cliente3 = Cliente(
        "C003",
        "Andres Gomez",
        "1090123458",
        "3001234569",
        "correo_incorrecto"
    )

except DatosInvalidosError as error:
    print("Error controlado correctamente:", error)


print("\n======================================")
print("      PRUEBAS FINALIZADAS")
print("======================================")
