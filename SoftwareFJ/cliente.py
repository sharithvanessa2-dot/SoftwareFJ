
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: cliente.py
# DESCRIPCION: Gestion y validacion de clientes.
# =====================================================

import re

from entidades import Entidad
from excepciones import DatosInvalidosError
from logs import registrar_evento


class Cliente(Entidad):
    """
    Clase que representa a los clientes de Software FJ.
    Hereda de la clase abstracta Entidad.
    """

    def __init__(self, identificador, nombre, documento,
                 telefono, correo):

        # Inicializar los atributos de la clase padre.
        super().__init__(identificador)

        # Validar el nombre del cliente.
        if not isinstance(nombre, str) or len(nombre.strip()) < 3:
            raise DatosInvalidosError(
                "El nombre debe tener minimo 3 caracteres."
            )

        # Validar el documento.
        if not str(documento).isdigit():
            raise DatosInvalidosError(
                "El documento debe contener solo numeros."
            )

        # Validar el telefono.
        if not str(telefono).isdigit() or not 7 <= len(str(telefono)) <= 15:
            raise DatosInvalidosError(
                "El telefono debe contener entre 7 y 15 digitos."
            )

        # Validar el correo electronico.
        patron_correo = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

        if not isinstance(correo, str) or not re.match(patron_correo, correo):
            raise DatosInvalidosError(
                "El correo electronico no es valido."
            )

        # Aplicar encapsulacion a los datos personales.
        self.__nombre = nombre.strip()
        self.__documento = str(documento)
        self.__telefono = str(telefono)
        self.__correo = correo.strip().lower()

        # Registrar el evento exitoso.
        registrar_evento(
            f"Cliente registrado: {self.__nombre} "
            f"- Documento: {self.__documento}"
        )

    # Propiedades para consultar los datos de forma controlada.

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def telefono(self):
        return self.__telefono

    @property
    def correo(self):
        return self.__correo

    def mostrar_informacion(self):
        """
        Muestra la informacion general del cliente.
        Implementa el metodo abstracto de Entidad.
        """

        return (
            f"ID: {self.identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Documento: {self.__documento}\n"
            f"Telefono: {self.__telefono}\n"
            f"Correo: {self.__correo}"
        )
