
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: servicios.py
# DESCRIPCION: Gestion de servicios especializados.
# =====================================================

from abc import abstractmethod

from entidades import Entidad
from excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError
)
from logs import registrar_evento


class Servicio(Entidad):
    """
    Clase abstracta que representa los servicios
    ofrecidos por la empresa Software FJ.
    """

    def __init__(self, identificador, nombre, tarifa_base):

        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre del servicio es obligatorio."
            )

        if not isinstance(tarifa_base, (int, float)) or isinstance(tarifa_base, bool) or tarifa_base <= 0:
            raise DatosInvalidosError(
                "La tarifa base debe ser un numero positivo."
            )

        self._nombre = nombre.strip()
        self._tarifa_base = float(tarifa_base)
        self._disponible = True

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @property
    def disponible(self):
        return self._disponible

    def cambiar_disponibilidad(self, estado):
        """Permite habilitar o deshabilitar un servicio."""

        if not isinstance(estado, bool):
            raise DatosInvalidosError(
                "El estado debe ser verdadero o falso."
            )

        self._disponible = estado

        registrar_evento(
            f"Disponibilidad del servicio {self._nombre}: {estado}"
        )

    def validar_disponibilidad(self):
        """Comprueba que el servicio pueda utilizarse."""

        if not self._disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self._nombre} no esta disponible."
            )

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """
        Metodo que sera sobrescrito por los servicios derivados.
        Permite calcular costos con impuestos y descuentos.
        """
        raise NotImplementedError

    @abstractmethod
    def describir(self):
        """Describe las caracteristicas del servicio."""
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        """Valida los parametros del servicio."""
        pass

    def mostrar_informacion(self):
        """Muestra la informacion general del servicio."""

        return (
            f"ID: {self.identificador}\n"
            f"Servicio: {self._nombre}\n"
            f"Tarifa base: ${self._tarifa_base:,.2f}\n"
            f"Disponible: {'Si' if self._disponible else 'No'}"
        )


class ReservaSala(Servicio):
    """Servicio especializado en reserva de salas."""

    def __init__(self, identificador, nombre, tarifa_base, capacidad):

        super().__init__(identificador, nombre, tarifa_base)

        if not isinstance(capacidad, int) or isinstance(capacidad, bool) or capacidad <= 0:
            raise DatosInvalidosError(
                "La capacidad debe ser un entero positivo."
            )

        self.__capacidad = capacidad

    def validar_parametros(self, duracion):

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError(
                "La duracion de la reserva debe ser positiva."
            )

        self.validar_disponibilidad()

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar_parametros(duracion)
        validar_cargos(impuesto, descuento)

        subtotal = self._tarifa_base * duracion

        total = subtotal + (subtotal * impuesto / 100)
        total -= subtotal * descuento / 100

        registrar_evento(
            f"Costo calculado para reserva de sala: ${total:.2f}"
        )

        return round(total, 2)

    def describir(self):

        return (
            f"Reserva de sala: {self._nombre}. "
            f"Capacidad maxima: {self.__capacidad} personas."
        )


class AlquilerEquipo(Servicio):
    """Servicio especializado en alquiler de equipos."""

    def __init__(self, identificador, nombre, tarifa_base, tipo_equipo):

        super().__init__(identificador, nombre, tarifa_base)

        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise DatosInvalidosError(
                "Debe especificar el tipo de equipo."
            )

        self.__tipo_equipo = tipo_equipo.strip()

    def validar_parametros(self, duracion):

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError(
                "La duracion del alquiler debe ser positiva."
            )

        self.validar_disponibilidad()

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar_parametros(duracion)
        validar_cargos(impuesto, descuento)

        subtotal = self._tarifa_base * duracion

        total = subtotal + (subtotal * impuesto / 100)
        total -= subtotal * descuento / 100

        registrar_evento(
            f"Costo calculado para alquiler de equipo: ${total:.2f}"
        )

        return round(total, 2)

    def describir(self):

        return (
            f"Alquiler de equipo: {self._nombre}. "
            f"Tipo de equipo: {self.__tipo_equipo}."
        )


class AsesoriaEspecializada(Servicio):
    """Servicio especializado en asesoria profesional."""

    def __init__(self, identificador, nombre, tarifa_base, especialidad):

        super().__init__(identificador, nombre, tarifa_base)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError(
                "Debe especificar la especialidad de la asesoria."
            )

        self.__especialidad = especialidad.strip()

    def validar_parametros(self, duracion):

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError(
                "La duracion de la asesoria debe ser positiva."
            )

        self.validar_disponibilidad()

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar_parametros(duracion)
        validar_cargos(impuesto, descuento)

        subtotal = self._tarifa_base * duracion

        total = subtotal + (subtotal * impuesto / 100)
        total -= subtotal * descuento / 100

        registrar_evento(
            f"Costo calculado para asesoria: ${total:.2f}"
        )

        return round(total, 2)

    def describir(self):

        return (
            f"Asesoria especializada: {self._nombre}. "
            f"Especialidad: {self.__especialidad}."
        )


def validar_cargos(impuesto, descuento):
    """
    Valida los porcentajes de impuestos y descuentos.
    """

    for nombre, valor in (
        ("Impuesto", impuesto),
        ("Descuento", descuento)
    ):

        if (
            not isinstance(valor, (int, float))
            or isinstance(valor, bool)
            or not 0 <= valor <= 100
        ):
            raise DatosInvalidosError(
                f"El porcentaje de {nombre.lower()} "
                "debe estar entre 0 y 100."
            )
