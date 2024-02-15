import os
from colorama import init, Fore, Style
import subprocess

init()



# Define una función para imprimir el texto con animación de colores
def imprimir_texto_animado():
            print(Fore.MAGENTA + r'''
                                                                            

▓█████▄  ▒█████   ███▄ ▄███▓ ███▄ ▄███▓     ██████ ▓█████  ██▓    ▓█████  ▄████▄  ▄▄▄█████▓ ▒█████   ██▀███  
▒██▀ ██▌▒██▒  ██▒▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒   ▒██    ▒ ▓█   ▀ ▓██▒    ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
░██   █▌▒██░  ██▒▓██    ▓██░▓██    ▓██░   ░ ▓██▄   ▒███   ▒██░    ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░▓█▄   ▌▒██   ██░▒██    ▒██ ▒██    ▒██      ▒   ██▒▒▓█  ▄ ▒██░    ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░▒████▓ ░ ████▓▒░▒██▒   ░██▒▒██▒   ░██▒   ▒██████▒▒░▒████▒░██████▒░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
 ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░░ ▒░   ░  ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░▓  ░░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░ ▒  ▒   ░ ▒ ▒░ ░  ░      ░░  ░      ░   ░ ░▒  ░ ░ ░ ░  ░░ ░ ▒  ░ ░ ░  ░  ░  ▒       ░      ░ ▒ ▒░   ░▒ ░ ▒░
 ░ ░  ░ ░ ░ ░ ▒  ░      ░   ░      ░      ░  ░  ░     ░     ░ ░      ░   ░          ░      ░ ░ ░ ▒    ░░   ░ 
   ░        ░ ░         ░          ░            ░     ░  ░    ░  ░   ░  ░░ ░                   ░ ░     ░     
 ░                                                                       ░                                   

                                        Memphis Menace | JTGS                             
                              Selector de modo de extracción específico


''' + Style.RESET_ALL)


# Llama a la función para imprimir el texto con animación de colores
imprimir_texto_animado()

def abrir_archivo(opcion):
    ruta_recursos = os.path.join(os.path.dirname(__file__), "recursos")
    
    if opcion == 1:
        archivo = os.path.join(ruta_recursos, "class.py")  # Ruta del archivo 1
    elif opcion == 2:
        archivo = os.path.join(ruta_recursos, "id.py")     # Ruta del archivo 2
    else:
        print("Opción no válida.")
        return

    try:
        # Abre el archivo en el sistema
        os.startfile(archivo)  # Abre el archivo en Windows
        # subprocess.Popen(["xdg-open", archivo])  # En sistemas Linux
    except Exception as e:
        print(f"No se pudo abrir el archivo: {e}")

    # Cierra la terminal actual
    if os.name == "nt":  # Windows
        subprocess.Popen(["taskkill", "/F", "/PID", str(os.getpid())], shell=True)
    else:  # Unix-like systems
        os.system("kill -9 " + str(os.getpid()))


def main():
    print(Fore.GREEN + r"Seleccione una opción:" + Style.RESET_ALL)
    print(Fore.RED + r"1. Extraccion Espesifica por medio de Clase" + Style.RESET_ALL)
    print(Fore.YELLOW + r"2. Extraccion Espesifica por medio de ID" + Style.RESET_ALL)

    opcion = int(input("Opción: "))
    abrir_archivo(opcion)


if __name__ == "__main__":
    main()
