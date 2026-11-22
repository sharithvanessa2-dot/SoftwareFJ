
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: entidades.py
# DESCRIPCION: Clase abstracta general del sistema.
# =====================================================

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa las entidades
    generales del sistema Software FJ.
    """

    def __init__(self, identificador):

        # Validar que el identificador exista.
        if not identificador:
            raise ValueError(
                "El identificador es obligatorio."
            )

        # Atributo protegido para aplicar encapsulacion.
        self._identificador = identificador

    @property
    def identificador(self):
        """
        Permite consultar el identificador
        de forma controlada.
        """
        return self._identificador

    @abstractmethod
    def mostrar_informacion(self):
        """
        Metodo abstracto que deben implementar
        las clases que hereden de Entidad.
        """
        pass
