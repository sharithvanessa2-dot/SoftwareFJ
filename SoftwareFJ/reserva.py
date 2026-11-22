
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: reserva.py
# DESCRIPCION: Gestion integral de reservas.
# =====================================================

from entidades import Entidad

from excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError,
    OperacionNoPermitidaError,
    ServicioNoDisponibleError,
    ParametroFaltanteError
)

from logs import (
    registrar_evento,
    registrar_error,
    registrar_exception
)


class Reserva(Entidad):
    """
    Representa una reserva realizada por un cliente
    para utilizar uno de los servicios de Software FJ.
    """

    ESTADOS_VALIDOS = (
        "Pendiente",
        "Confirmada",
        "Cancelada",
        "Procesada"
    )

    def __init__(
        self,
        identificador,
        cliente,
        servicio,
        duracion
    ):

        super().__init__(identificador)

        # Validar que se proporcione un cliente.
        if cliente is None:
            raise ParametroFaltanteError(
                "La reserva requiere un cliente."
            )

        # Validar que se proporcione un servicio.
        if servicio is None:
            raise ParametroFaltanteError(
                "La reserva requiere un servicio."
            )

        # Validar la duracion.
        if (
            not isinstance(duracion, (int, float))
            or isinstance(duracion, bool)
            or duracion <= 0
        ):
            raise DatosInvalidosError(
                "La duracion debe ser un numero positivo."
            )

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__costo = 0.0

        registrar_evento(
            f"Reserva {identificador} creada correctamente."
        )

    # ==============================================
    # PROPIEDADES
    # ==============================================

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    # ==============================================
    # CONFIRMAR RESERVA
    # ==============================================

    def confirmar(self):
        """
        Confirma una reserva pendiente.
        """

        try:

            if self.__estado != "Pendiente":
                raise OperacionNoPermitidaError(
                    "Solo se pueden confirmar reservas pendientes."
                )

            # Verificar disponibilidad del servicio.
            self.__servicio.validar_parametros(
                self.__duracion
            )

            self.__estado = "Confirmada"

            registrar_evento(
                f"Reserva {self.identificador} confirmada."
            )

            return True

        except ServicioNoDisponibleError as error:

            registrar_error(
                f"No se pudo confirmar la reserva "
                f"{self.identificador}: {error}"
            )

            raise

        except Exception as error:

            registrar_exception(
                f"Error al confirmar reserva "
                f"{self.identificador}."
            )

            raise ReservaInvalidaError(
                "No fue posible confirmar la reserva."
            ) from error

    # ==============================================
    # CANCELAR RESERVA
    # ==============================================

    def cancelar(self):
        """
        Cancela una reserva pendiente o confirmada.
        """

        if self.__estado not in ("Pendiente", "Confirmada"):

            raise OperacionNoPermitidaError(
                "No se puede cancelar una reserva "
                "que ya fue procesada o cancelada."
            )

        self.__estado = "Cancelada"

        registrar_evento(
            f"Reserva {self.identificador} cancelada."
        )

        return True

    # ==============================================
    # PROCESAR RESERVA
    # ==============================================

    def procesar(
        self,
        impuesto=0,
        descuento=0
    ):
        """
        Procesa una reserva confirmada y calcula
        el costo final del servicio.
        """

        try:

            if self.__estado != "Confirmada":
                raise OperacionNoPermitidaError(
                    "La reserva debe estar confirmada "
                    "antes de procesarse."
                )

            self.__costo = self.__servicio.calcular_costo(
                self.__duracion,
                impuesto,
                descuento
            )

            self.__estado = "Procesada"

            registrar_evento(
                f"Reserva {self.identificador} procesada. "
                f"Costo: ${self.__costo:.2f}"
            )

            return self.__costo

        except (OperacionNoPermitidaError, DatosInvalidosError):
            raise

        except Exception as error:

            registrar_exception(
                f"Error al procesar reserva "
                f"{self.identificador}."
            )

            raise ReservaInvalidaError(
                "Ocurrio un error durante el procesamiento."
            ) from error

    # ==============================================
    # INFORMACION DE LA RESERVA
    # ==============================================

    def mostrar_informacion(self):
        """
        Presenta los datos completos de la reserva.
        """

        return (
            f"\n========== RESERVA ==========\n"
            f"Identificador: {self.identificador}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duracion: {self.__duracion} horas\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.__costo:,.2f}\n"
            f"============================="
        )
