
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: gestor.py
# DESCRIPCION: Administrador central del sistema.
# =====================================================

from cliente import Cliente
from servicios import Servicio
from reserva import Reserva

from excepciones import (
    DatosInvalidosError,
    ClienteNoEncontradoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError,
    OperacionNoPermitidaError,
    ParametroFaltanteError
)

from logs import (
    registrar_evento,
    registrar_error,
    registrar_exception
)


class GestorSoftwareFJ:
    """
    Clase encargada de administrar los clientes,
    servicios y reservas de Software FJ.

    Toda la informacion se almacena en listas
    internas, sin utilizar bases de datos.
    """

    def __init__(self):

        # Listas internas del sistema.
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

        registrar_evento(
            "Administrador de Software FJ iniciado."
        )

    # ==============================================
    # REGISTRAR CLIENTES
    # ==============================================

    def registrar_cliente(self, cliente):

        try:

            if not isinstance(cliente, Cliente):
                raise DatosInvalidosError(
                    "El objeto proporcionado no es un cliente valido."
                )

            if any(
                c.identificador == cliente.identificador
                for c in self.__clientes
            ):
                raise DatosInvalidosError(
                    "Ya existe un cliente con ese identificador."
                )

            if any(
                c.documento == cliente.documento
                for c in self.__clientes
            ):
                raise DatosInvalidosError(
                    "Ya existe un cliente con ese documento."
                )

            self.__clientes.append(cliente)

            registrar_evento(
                f"Cliente {cliente.nombre} registrado."
            )

            return True

        except DatosInvalidosError as error:

            registrar_error(
                f"Error al registrar cliente: {error}"
            )

            raise

    # ==============================================
    # REGISTRAR SERVICIOS
    # ==============================================

    def registrar_servicio(self, servicio):

        try:

            if not isinstance(servicio, Servicio):
                raise DatosInvalidosError(
                    "El objeto proporcionado no es un servicio valido."
                )

            if any(
                s.identificador == servicio.identificador
                for s in self.__servicios
            ):
                raise DatosInvalidosError(
                    "Ya existe un servicio con ese identificador."
                )

            self.__servicios.append(servicio)

            registrar_evento(
                f"Servicio {servicio.nombre} registrado."
            )

            return True

        except DatosInvalidosError as error:

            registrar_error(
                f"Error al registrar servicio: {error}"
            )

            raise

    # ==============================================
    # BUSCAR CLIENTES
    # ==============================================

    def buscar_cliente(self, identificador):

        if not identificador:
            raise ParametroFaltanteError(
                "Debe proporcionar el identificador del cliente."
            )

        for cliente in self.__clientes:

            if cliente.identificador == identificador:
                return cliente

        raise ClienteNoEncontradoError(
            f"No existe el cliente con ID {identificador}."
        )

    # ==============================================
    # BUSCAR SERVICIOS
    # ==============================================

    def buscar_servicio(self, identificador):

        if not identificador:
            raise ParametroFaltanteError(
                "Debe proporcionar el identificador del servicio."
            )

        for servicio in self.__servicios:

            if servicio.identificador == identificador:
                return servicio

        raise ServicioNoDisponibleError(
            f"No existe el servicio con ID {identificador}."
        )

    # ==============================================
    # CREAR RESERVAS
    # ==============================================

    def crear_reserva(
        self,
        identificador,
        id_cliente,
        id_servicio,
        duracion
    ):

        try:

            if not identificador:
                raise ParametroFaltanteError(
                    "El identificador de la reserva es obligatorio."
                )

            if any(
                r.identificador == identificador
                for r in self.__reservas
            ):
                raise ReservaInvalidaError(
                    "Ya existe una reserva con ese identificador."
                )

            cliente = self.buscar_cliente(id_cliente)

            servicio = self.buscar_servicio(id_servicio)

            reserva = Reserva(
                identificador,
                cliente,
                servicio,
                duracion
            )

            self.__reservas.append(reserva)

            registrar_evento(
                f"Reserva {identificador} creada en el sistema."
            )

            return reserva

        except (
            ParametroFaltanteError,
            ClienteNoEncontradoError,
            ServicioNoDisponibleError,
            ReservaInvalidaError,
            DatosInvalidosError
        ) as error:

            registrar_error(
                f"Error al crear reserva: {error}"
            )

            raise

        except Exception as error:

            registrar_exception(
                "Error inesperado durante la creacion de una reserva."
            )

            raise ReservaInvalidaError(
                "No fue posible crear la reserva."
            ) from error

    # ==============================================
    # BUSCAR RESERVAS
    # ==============================================

    def buscar_reserva(self, identificador):

        if not identificador:
            raise ParametroFaltanteError(
                "Debe proporcionar el identificador de la reserva."
            )

        for reserva in self.__reservas:

            if reserva.identificador == identificador:
                return reserva

        raise ReservaInvalidaError(
            f"No existe la reserva con ID {identificador}."
        )

    # ==============================================
    # CONFIRMAR RESERVAS
    # ==============================================

    def confirmar_reserva(self, identificador):

        reserva = self.buscar_reserva(identificador)

        return reserva.confirmar()

    # ==============================================
    # CANCELAR RESERVAS
    # ==============================================

    def cancelar_reserva(self, identificador):

        reserva = self.buscar_reserva(identificador)

        return reserva.cancelar()

    # ==============================================
    # PROCESAR RESERVAS
    # ==============================================

    def procesar_reserva(
        self,
        identificador,
        impuesto=0,
        descuento=0
    ):

        reserva = self.buscar_reserva(identificador)

        return reserva.procesar(
            impuesto,
            descuento
        )

    # ==============================================
    # LISTAR CLIENTES
    # ==============================================

    def listar_clientes(self):

        return list(self.__clientes)

    # ==============================================
    # LISTAR SERVICIOS
    # ==============================================

    def listar_servicios(self):

        return list(self.__servicios)

    # ==============================================
    # LISTAR RESERVAS
    # ==============================================

    def listar_reservas(self):

        return list(self.__reservas)

    # ==============================================
    # MOSTRAR INFORMACION GENERAL
    # ==============================================

    def mostrar_resumen(self):

        return (
            "\n========== SOFTWARE FJ ==========\n"
            f"Total de clientes: {len(self.__clientes)}\n"
            f"Total de servicios: {len(self.__servicios)}\n"
            f"Total de reservas: {len(self.__reservas)}\n"
            "================================="
        )
