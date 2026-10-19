from decimal import Decimal, getcontext

dinero_neo = 0.1
dinero_trinity = 0.2
total_falso = dinero_neo + dinero_trinity

print(f'\n con float 0.1 + 0.2 es {total_falso} ("Error en el banco matrix)')

cuenta_neo = Decimal('0.1')
cuenta_trinity = Decimal('0.2')
total_real = cuenta_neo + cuenta_trinity
print(f'Con Decimal 0.1 + 0.2 es {total_real} (bum pum kapao)')

getcontext().prec = 4
num1 = Decimal('1.12345')
num2 = Decimal('2.0')

print(f'Resultado con precion de 3 {num1 * num2}')

print('-------------------------------------')


# Casting: de int a float y viceversa 🔥
nivel_bateria = 42
bateria_decimal = float(nivel_bateria)
print(f"\nBatería de la nave: {bateria_decimal}")  # Imprime 42.0
codigo_matriz = 3.999
codigo_entero = int(codigo_matriz)


# ⚠️ Ojo aquí: int() NO redondea, simplemente corta (trunca) los decimales
print(f"Código truncado: {codigo_entero}")  # Imprime 3, no 4



# Números Complejos (Tienen una parte real y una imaginaria)
# En Python la parte imaginaria se marca con una 'j' (no con 'i' como en matemáticas)
frecuencia_transmision = 2 + 3j
print(
    f"Frecuencia secreta: {frecuencia_transmision}, tipo: {type(frecuencia_transmision)}"
)
