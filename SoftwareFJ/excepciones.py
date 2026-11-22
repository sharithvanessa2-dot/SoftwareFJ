
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: excepciones.py
# DESCRIPCION: Excepciones personalizadas del sistema.
# =====================================================


class ErrorSoftwareFJ(Exception):
    """Clase base para los errores del sistema."""
    pass


class DatosInvalidosError(ErrorSoftwareFJ):
    """Error cuando los datos ingresados no son validos."""
    pass


class ClienteNoEncontradoError(ErrorSoftwareFJ):
    """Error cuando un cliente no existe."""
    pass


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """Error cuando un servicio no esta disponible."""
    pass


class ReservaInvalidaError(ErrorSoftwareFJ):
    """Error cuando una reserva presenta inconsistencias."""
    pass


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    """Error cuando se intenta realizar una operacion prohibida."""
    pass


class ParametroFaltanteError(ErrorSoftwareFJ):
    """Error cuando falta un parametro obligatorio."""
    pass
