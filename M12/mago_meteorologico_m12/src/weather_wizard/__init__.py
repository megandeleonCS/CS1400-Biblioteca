"""
Este archivo expone las funciones principales para que sean fáciles de importar.
"""

from .motor import obtener_clima_ciudad

# Solo importa esto si realmente tienes api.py
try:
    from .api import fetch_weather_from_provider
except ImportError:
    fetch_weather_from_provider = None

# Qué se exporta al usar: from weather_wizard import *
__all__ = ["obtener_clima_ciudad", "fetch_weather_from_provider"]

__version__ = "0.1.0"
__author__ = "Thais Medina"