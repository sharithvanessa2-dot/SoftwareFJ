
# =====================================================
# PROYECTO: SOFTWARE FJ
# ARCHIVO: logs.py
# DESCRIPCION: Registro de eventos y errores.
# =====================================================

import logging
from pathlib import Path

# Ruta donde se almacenara el archivo de registros.
RUTA_LOGS = Path(__file__).resolve().parent / "logs.txt"

# Configuracion del sistema de registro.
logging.basicConfig(
    filename=RUTA_LOGS,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)


def registrar_evento(mensaje):
    """Registra eventos importantes del sistema."""
    logging.info(mensaje)


def registrar_error(mensaje):
    """Registra errores detectados."""
    logging.error(mensaje)


def registrar_excepcion(mensaje):
    """Registra errores junto con sus detalles."""
    logging.exception(mensaje)
