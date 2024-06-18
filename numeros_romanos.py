def decimal_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def decimal_to_roman_extended(num):
    if num < 4000:
        return decimal_to_roman(num)
    
    roman_num = ''
    while num >= 1000:
        num, remainder = divmod(num, 1000)
        if num > 0:
            roman_num = '(' + decimal_to_roman(num) + ')' + decimal_to_roman(remainder)
        else:
            roman_num = decimal_to_roman(remainder)
        return roman_num

def roman_to_decimal(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    def parse_roman(roman):
        decimal_num = 0
        prev_value = 0
        for char in reversed(roman):
            value = roman_values[char]
            if value >= prev_value:
                decimal_num += value
            else:
                decimal_num -= value
            prev_value = value
        return decimal_num

    # Manejo de números con paréntesis
    total = 0
    parts = roman.split(')')
    for part in parts:
        if '(' in part:
            inside_parentheses = part.split('(')[1]
            total += 1000 * parse_roman(inside_parentheses)
        else:
            total += parse_roman(part)
    
    return total

def menu():
    while True:
        print("Seleccione una opción:")
        print("1. Convertir de decimal a romano")
        print("2. Convertir de romano a decimal")
        print("3. Salir")
        choice = input("Ingrese su opción: ")

        if choice == '1':
            num = int(input("Ingrese un número decimal: "))
            if num < 0:
                print("Por favor, ingrese un número positivo.")
            else:
                if num < 4000:
                    print(f"El número romano es: {decimal_to_roman(num)}")
                else:
                    print(f"El número romano extendido es: {decimal_to_roman_extended(num)}")
        elif choice == '2':
            roman = input("Ingrese un número romano: ")
            try:
                print(f"El número decimal es: {roman_to_decimal(roman)}")
            except KeyError:
                print("Número romano no válido. Inténtelo de nuevo.")
        elif choice == '3':
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecución del menú
menu()
