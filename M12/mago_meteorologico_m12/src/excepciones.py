class WeatherWizardError(Exception):
    """Error base para el proyecto."""

class CityNotFoundError(WeatherWizardError):
    """Se lanza cuando la API no encuentra la ciudad."""

class APIConnectionError(WeatherWizardError):
    """Se lanza cuando falla el internet o el servidor."""