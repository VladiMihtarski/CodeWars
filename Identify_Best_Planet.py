REQUIRED_ELEMENTS = ['H', 'C', 'N', 'O', 'P', 'Ca']

def best_planet(solar_system, max_size):
    max_planet = ""
    max_area = float("-inf")

    for planet in solar_system:
        elements, area = planet.split("_")[0], int(planet.split("_")[1])

        # Създаваме списък, в който ще събираме разделените елементи
        combined_elements = []
        current_element = ""

        # Итерираме през всеки символ на планетата
        for char in elements:
            if char.islower():
                # Текущият символ е малка буква, затова го комбинираме с предишния елемент
                current_element += char
            else:
                # Текущият символ е главна буква, затова добавяме предишния елемент към списъка
                if current_element:
                    combined_elements.append(current_element)
                # Започваме нов елемент с текущия символ
                current_element = char

        # Добавяме последния елемент към списъка
        if current_element:
            combined_elements.append(current_element)

        # Проверяваме дали всички необходими елементи са включени в комбинираните елементи
        if all(element in combined_elements for element in REQUIRED_ELEMENTS):
            # Проверка дали планетата е по-голяма от максималната до момента
            if area <= max_size and area > max_area:
                max_planet = planet
                max_area = area

    return max_planet

# Примерно използване
planets = ['HCaPCPrN_128', 'AlOgGaRuErPaTbOFe_51', 'CCaTiHPOIN_265', 'GdNHBaCaOPAlC_193', 'NOHCPCa_130', 'OCaHNPZr_227', 'ThCaTcTbSbPHTlN_111', 'SiNePYbCaNAsHeGd_184']
max_size = 263

result = best_planet(planets, max_size)
print(result)
