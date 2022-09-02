#// Converter uma temperatura de Graus Celsius para Kelvin.

def converter_temperatura (a,b:float):
    a=b+273
    return (a)

temperatura=input("Digite uma temperatura (Celsius): ")
celsius=float(temperatura)
result=0.0

kelvin=converter_temperatura(result,celsius)

print(" A temperatura convertida em Kelvin é:",kelvin)