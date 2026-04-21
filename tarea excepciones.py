#validar correo 
import re

def validar_correo():
    try:
        correo = input("Ingresa un correo electrónico: ")
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if re.match(patron, correo):
            print("El correo es valido.")
        else:
            raise ValueError("correo no valido.")
            
    except ValueError as e:
     print(f"Error: {e}") 
    except Exception as e: 
     print(f"Error inesperado: {e}") 

validar_correo()

#inventario 
inventario = {
    "deportivo": {
        "negro": {40: 5, 38: 10}
    }
}
def verificar_zapatos():
    try:
        talla_input = input("Ingresa la talla: ")
        talla = int(talla_input) 
        
        modelo = inventario["deportivo"]["negro"][talla]
        print(f"Disponibles: {modelo}")
        
    except ValueError:
        print("Error: La talla debe ser un numero entero.")
        
    except KeyError:
        print("Error: Esa talla no existe en el inventario.")
    finally:
        print("Operacion completada")
verificar_zapatos()

#calcular edad 
from datetime import date

def calcular_edad():
    try:
        dia = int(input("Dia de nacimiento: "))
        mes = int(input("Mes de nacimiento: "))
        año = int(input("Año de nacimiento: "))
        nacimiento = date(año, mes, dia)
        hoy = date.today()
        edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
        print(f"La edad es: {edad} años")
    except ValueError:
        print("Error: Ingresa números validos o una fecha que exista")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")
    finally:
        print("Proceso de calculo de edad finalizado")
calcular_edad()

#Calculo nomina, quincena y axulio de transporte
def calcular_quincena():
    try:
        sueldo_mensual = float(input("Ingrese su sueldo mensual: "))
        dias_trabajados = int(input("Ingrese dias trabajados (maximo 15): "))
        AUX_TRANSPORTE_MES = 162000
        pago_base = (sueldo_mensual / 30) * dias_trabajados
        if sueldo_mensual <= (1300000 * 2):
            auxilio = (AUX_TRANSPORTE_MES / 30) * dias_trabajados
        else:
            auxilio = 0
            
        total = pago_base + auxilio
    except ValueError:
        print("Error: Por favor ingresa solo numeros en el sueldo y los dias.")
    except ZeroDivisionError:
        print("Error: Los dias trabajados no pueden ser cero.")
    except Exception as e:

        print(f"Error inesperado: {e}")
    else:
        print(f"Auxilio de transporte: {auxilio}")
        print(f"Total a pagar en la quincena: {total}")
    finally:
        print("Cálculo de nomina finalizado.")
calcular_quincena()

#Guardar palabras en txt 
def guardar_palabras():
    try:
        palabras = []
        print("Ingresa 10 palabras:")
        
        for i in range(10):
            palabra = input(f"Palabra {i+1}: ")
            palabras.append(palabra)
        with open("palabras.txt", "w") as archivo:
            for p in palabras:
                archivo.write(p + "\n")
                
    except PermissionError:
        print("Error: No tienes permisos para escribir en esta carpeta.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
    else:
        print("Archivo 'palabras.txt' guardado con exito")
    finally:
        print("Proceso de guardado completado.")
guardar_palabras()