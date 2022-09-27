def celsius_kelvin (a:float):
   k=a+273
   return (k)

def kelvin_celsius (b:float):
    c=b-273
    return(c)

def kelvin_fahrenheit (c:float):
    f=(c-273)*1.8+32
    return(f)

def fahrenheit_kelvin (d:float):
    k=(d-32)*5/9+273
    return(k)

def celsius_fahrenheit (e:float):
    f=e*1.8+32
    return(f)
    
def fahrenheit_celsius (f:float):
    c=(f-32)/1.8
    return(c)

temp=input("Digite aqui uma temperatura: ")
temperatura=float(temp)

print("-"*30)
print("     Convertor de Temperaturas     ")
print("-"*30)
print(" [1] Celsius para Kelvin ")
print(" [2] Kelvin para Celsius ")
print(" [3] Fahrenheit para Kelvin ")
print(" [4] Kelvin para Fahreinheit ")
print(" [5] Fahrenheit para Celsius ")
print(" [6] Celsius para Fahrenheit ")
print(" [7] Sair ")

resp=input("Opção: ")

if resp=="1":
    conver_result=celsius_kelvin(temperatura)
    print(" A temperatura",temp,f"°C convertida em Kelvin é: {conver_result:.2f}K")
elif resp=="2":
    conver_result=kelvin_celsius(temperatura)
    print(" A temperatura",temp,f"K convertida em Celsius é: {conver_result:.1f}°C ")
elif resp=="3":
    conver_result=fahrenheit_kelvin(temperatura)
    print(" A temperatura",temp,f"F convertida em Kelvin é: {conver_result:.1f}K")    
elif resp=="4":
    conver_result=kelvin_fahrenheit(temperatura)
    print(" A temperatura",temp,f"K convertida em Fahrenheit é: {conver_result:.1f}F") 
elif resp=="5":
    conver_result=fahrenheit_celsius(temperatura)
    print(" A temperatura",temp,f"F convertida em Celsius é: {conver_result:.1f}°C ")   
elif resp=="6":
    conver_result=celsius_fahrenheit(temperatura)
    print(" A temperatura",temp,f"°C convertida em Fahrenheit é: {conver_result:.1f}F")
else:
    print("Obrigada por usar o nosso aplicativo.")