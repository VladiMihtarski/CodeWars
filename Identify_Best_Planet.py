REQUIRED_ELEMENTS = ('H', 'C', 'N', 'O', 'P', 'Ca')

def best_planet(solar_system, max_size):
    max_planet = ""
    max_area = 0

    for planet in solar_system:
        elements, area = planet.split("_")
        area = int(area)

        # Проверка дали планетата съдържа всички необходими елементи
        if all(element in elements for element in REQUIRED_ELEMENTS):
            # Проверка дали планетата е по-голяма от максималната до момента
            if area <= max_size and area > max_area:
                max_planet = planet
                max_area = area

    return max_planet


# Входни данни
planets = ["OHNCCaP_100", "OHC_200", "OCa_50", "OHCCaP_400", "OHNCCaP_225", "OHCa_250"]
max_size = 250

# Намиране на планетата с най-голямата площ, която съдържа всички необходими елементи
result = best_planet(planets, max_size)
print(result)
