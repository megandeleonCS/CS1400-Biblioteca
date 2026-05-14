from weather_wizard.utils import celsius_to_fahrenheit

def test_conversion_celsius_a_fahrenheit():
    # Caso simple: punto de congelación
    assert celsius_to_fahrenheit(0) == 32
    # Caso simple: punto de ebullición
    assert celsius_to_fahrenheit(100) == 212

def test_nombre_ciudad_invalido():
    from weather_wizard.utils import is_valid_city_name
    assert is_valid_city_name("A") == False  # Muy corto
    assert is_valid_city_name("Madrid") == True