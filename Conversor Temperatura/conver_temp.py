#// Converter uma temperatura de Graus Celsius para Kelvin.
def converter_temperatura (a:float):
    result=a+273
    return (result)

temperatura=input("Digite uma temperatura (Celsius): ")
celsius=float(temperatura)

kelvin=converter_temperatura(celsius)

print(" A temperatura convertida em Kelvin é:",kelvin)