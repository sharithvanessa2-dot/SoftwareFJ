
# ============================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: main.py
# DESCRIPCION: Programa principal del sistema.
# ============================================================

from cliente import Cliente

from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from gestor import GestorSoftwareFJ

from excepciones import DatosInvalidosError

from logs import (
    registrar_evento,
    registrar_error,
    registrar_exception
)


# ============================================================
# INICIALIZACION DEL SISTEMA
# ============================================================

sistema = GestorSoftwareFJ()


# ============================================================
# FUNCION PARA REGISTRAR CLIENTES
# ============================================================

def crear_cliente():

    try:

        print("\n========== REGISTRO DE CLIENTE ==========")

        identificador = input("Identificador: ")
        nombre = input("Nombre completo: ")
        documento = input("Documento: ")
        telefono = input("Telefono: ")
        correo = input("Correo electronico: ")

        cliente = Cliente(
            identificador,
            nombre,
            documento,
            telefono,
            correo
        )

        sistema.registrar_cliente(cliente)

        print("\nCliente registrado correctamente.")

    except Exception as error:

        registrar_error(
            f"Error durante el registro de cliente: {error}"
        )

        print("\nNo fue posible registrar el cliente:", error)


# ============================================================
# FUNCION PARA CREAR RESERVAS
# ============================================================

def crear_reserva():

    try:

        print("\n========== CREAR RESERVA ==========")

        identificador = input("ID de la reserva: ")
        id_cliente = input("ID del cliente: ")
        id_servicio = input("ID del servicio: ")
        duracion = float(input("Duracion en horas: "))

        reserva = sistema.crear_reserva(
            identificador,
            id_cliente,
            id_servicio,
            duracion
        )

        print("\nReserva creada correctamente.")
        print(reserva.mostrar_informacion())

    except Exception as error:

        registrar_error(
            f"Error durante la creacion de reserva: {error}"
        )

        print("\nError controlado:", error)


# ============================================================
# FUNCION PARA CONFIRMAR RESERVAS
# ============================================================

def confirmar_reserva():

    try:

        identificador = input(
            "\nIngrese el ID de la reserva: "
        )

        sistema.confirmar_reserva(identificador)

        print("\nReserva confirmada correctamente.")

    except Exception as error:

        registrar_error(
            f"Error al confirmar reserva: {error}"
        )

        print("\nNo se pudo confirmar la reserva:", error)


# ============================================================
# FUNCION PARA CANCELAR RESERVAS
# ============================================================

def cancelar_reserva():

    try:

        identificador = input(
            "\nIngrese el ID de la reserva: "
        )

        sistema.cancelar_reserva(identificador)

        print("\nReserva cancelada correctamente.")

    except Exception as error:

        registrar_error(
            f"Error al cancelar reserva: {error}"
        )

        print("\nNo se pudo cancelar la reserva:", error)


# ============================================================
# FUNCION PARA PROCESAR RESERVAS
# ============================================================

def procesar_reserva():

    try:

        identificador = input(
            "\nIngrese el ID de la reserva: "
        )

        impuesto = float(
            input("Porcentaje de impuesto (0 si no aplica): ")
        )

        descuento = float(
            input("Porcentaje de descuento (0 si no aplica): ")
        )

        total = sistema.procesar_reserva(
            identificador,
            impuesto,
            descuento
        )

        print("\nReserva procesada correctamente.")
        print(f"Costo final: ${total:,.2f}")

    except Exception as error:

        registrar_error(
            f"Error al procesar reserva: {error}"
        )

        print("\nNo se pudo procesar la reserva:", error)


# ============================================================
# FUNCION PARA LISTAR INFORMACION
# ============================================================

def listar_clientes():

    print("\n========== CLIENTES REGISTRADOS ==========")

    clientes = sistema.listar_clientes()

    if not clientes:
        print("No existen clientes registrados.")
        return

    for cliente in clientes:
        print("\n", cliente.mostrar_informacion())


def listar_servicios():

    print("\n========== SERVICIOS DISPONIBLES ==========")

    servicios = sistema.listar_servicios()

    if not servicios:
        print("No existen servicios registrados.")
        return

    for servicio in servicios:
        print("\n", servicio.mostrar_informacion())
        print(servicio.describir())


def listar_reservas():

    print("\n========== RESERVAS REGISTRADAS ==========")

    reservas = sistema.listar_reservas()

    if not reservas:
        print("No existen reservas registradas.")
        return

    for reserva in reservas:
        print(reserva.mostrar_informacion())


# ============================================================
# DEMOSTRACION DE LAS 10 OPERACIONES EXIGIDAS
# ============================================================

def ejecutar_demostracion():

    print("\n")
    print("=" * 60)
    print(" DEMOSTRACION AUTOMATICA - SOFTWARE FJ")
    print("=" * 60)

    # OPERACION 1: Registro de cliente valido.

    print("\nOPERACION 1: Registro de cliente valido")

    try:

        cliente1 = Cliente(
            "C001",
            "Carlos Perez",
            "1090123456",
            "3001234567",
            "carlos@gmail.com"
        )

        sistema.registrar_cliente(cliente1)

        print("Cliente registrado correctamente.")

    except Exception as error:

        registrar_error(str(error))
        print("Error:", error)

    # OPERACION 2: Registro de cliente con nombre invalido.

    print("\nOPERACION 2: Registro de cliente invalido")

    try:

        cliente_invalido = Cliente(
            "C002",
            "Jo",
            "1090123457",
            "3001234568",
            "juan@gmail.com"
        )

        sistema.registrar_cliente(cliente_invalido)

        print("Cliente registrado.")

    except Exception as error:

        registrar_error(
            f"Operacion 2: {error}"
        )

        print("Error controlado correctamente:", error)

    # OPERACION 3: Registro de segundo cliente valido.

    print("\nOPERACION 3: Segundo cliente valido")

    try:

        cliente2 = Cliente(
            "C003",
            "Maria Rodriguez",
            "1090123458",
            "3001234569",
            "maria@gmail.com"
        )

        sistema.registrar_cliente(cliente2)

        print("Segundo cliente registrado.")

    except Exception as error:

        registrar_error(str(error))
        print("Error:", error)

    # OPERACION 4: Registro de reserva de sala.

    print("\nOPERACION 4: Registro de sala")

    try:

        sala = ReservaSala(
            "S001",
            "Sala de conferencias",
            50000,
            20
        )

        sistema.registrar_servicio(sala)

        print("Sala registrada correctamente.")

    except Exception as error:

        registrar_error(str(error))
        print("Error:", error)

    # OPERACION 5: Registro de alquiler de equipos.

    print("\nOPERACION 5: Registro de equipos")

    try:

        equipo = AlquilerEquipo(
            "S002",
            "Computador portatil",
            30000,
            "Portatil"
        )

        sistema.registrar_servicio(equipo)

        print("Equipo registrado correctamente.")

    except Exception as error:

        registrar_error(str(error))
        print("Error:", error)

    # OPERACION 6: Registro de asesoria especializada.

    print("\nOPERACION 6: Registro de asesoria")

    try:

        asesoria = AsesoriaEspecializada(
            "S003",
            "Asesoria tecnologica",
            80000,
            "Desarrollo de software"
        )

        sistema.registrar_servicio(asesoria)

        print("Asesoria registrada correctamente.")

    except Exception as error:

        registrar_error(str(error))
        print("Error:", error)

    # OPERACION 7: Creacion de reserva correcta.

    print("\nOPERACION 7: Creacion de reserva")

    try:

        sistema.crear_reserva(
            "R001",
            "C001",
            "S001",
            2
        )

        print("Reserva creada correctamente.")

    except Exception as error:

        registrar_error(str(error))
        print("Error:", error)

    # OPERACION 8: Confirmacion de reserva.

    print("\nOPERACION 8: Confirmacion de reserva")

    try:

        sistema.confirmar_reserva("R001")

        print("Reserva confirmada correctamente.")

    except Exception as error:

        registrar_error(str(error))
        print("Error:", error)

    # OPERACION 9: Procesamiento de reserva.

    print("\nOPERACION 9: Procesamiento de reserva")

    try:

        total = sistema.procesar_reserva(
            "R001",
            19,
            10
        )

        print("Reserva procesada correctamente.")
        print(f"Costo final: ${total:,.2f}")

    except Exception as error:

        registrar_error(str(error))
        print("Error:", error)

    # OPERACION 10: Reserva con cliente inexistente.

    print("\nOPERACION 10: Reserva con cliente inexistente")

    try:

        sistema.crear_reserva(
            "R002",
            "C999",
            "S001",
            2
        )

        print("Reserva creada.")

    except Exception as error:

        registrar_error(
            f"Operacion 10: {error}"
        )

        print("Error controlado correctamente:", error)

    # Uso de ELSE: se ejecuta cuando no hay excepciones.

    else:

        print("La operacion finalizo sin errores.")

    # Uso de FINALLY: se ejecuta siempre.

    finally:

        print("\nDemostracion automatica finalizada.")

        registrar_evento(
            "Demostracion automatica completada."
        )


# ============================================================
# MENU PRINCIPAL
# ============================================================

def mostrar_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("       SOFTWARE FJ")
        print(" SISTEMA DE GESTION INTEGRAL")
        print("=" * 50)

        print("1. Registrar cliente")
        print("2. Crear reserva")
        print("3. Confirmar reserva")
        print("4. Cancelar reserva")
        print("5. Procesar reserva")
        print("6. Listar clientes")
        print("7. Listar servicios")
        print("8. Listar reservas")
        print("9. Mostrar resumen")
        print("0. Salir")

        print("=" * 50)

        try:

            opcion = input("Seleccione una opcion: ").strip()

            if opcion == "1":
                crear_cliente()

            elif opcion == "2":
                crear_reserva()

            elif opcion == "3":
                confirmar_reserva()

            elif opcion == "4":
                cancelar_reserva()

            elif opcion == "5":
                procesar_reserva()

            elif opcion == "6":
                listar_clientes()

            elif opcion == "7":
                listar_servicios()

            elif opcion == "8":
                listar_reservas()

            elif opcion == "9":
                print(sistema.mostrar_resumen())

            elif opcion == "0":

                print("\nGracias por utilizar Software FJ.")

                registrar_evento(
                    "Sistema cerrado por el usuario."
                )

                break

            else:

                print("\nOpcion incorrecta. Intente nuevamente.")

        except Exception as error:

            registrar_exception(
                "Error inesperado en el menu principal."
            )

            print("\nError controlado:", error)

        finally:

            # El menu continua disponible despues
            # de cada operacion.

            pass


# ============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================

def main():

    try:

        print("\nIniciando sistema Software FJ...")

        registrar_evento(
            "Aplicacion principal iniciada."
        )

        ejecutar_demostracion()

        print(sistema.mostrar_resumen())

        mostrar_menu()

    except KeyboardInterrupt:

        print("\nEjecucion interrumpida por el usuario.")

        registrar_evento(
            "Ejecucion interrumpida manualmente."
        )

    except Exception as error:

        registrar_exception(
            "Error critico en el programa principal."
        )

        print("\nError general del sistema:", error)

    finally:

        print("\nSoftware FJ ha finalizado su ejecucion.")

        registrar_evento(
            "Aplicacion principal finalizada."
        )


# Ejecutar el programa principal.

if __name__ == "__main__":
    main()
