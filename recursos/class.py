#  [Programa]
#
#  Domm
#  Progama para extraer codigo HTML de paginas web
#
#  [Author]
#
#  JTGS | Memphis Menace
#  JTGS | [ADV] No es un exploit ni una herramienta de crackeo 
#
#  [Uso]
# progama gratis, son 2 herramientas una para extraer un codigo html en espesifico mediante un id y el otro mediante una clae, tambien esta la funcion de extraer todo el codigo html.
# usa el progama a tu gusto (no me hago responsable del uso que le puedes dar).


import requests
import os
from colorama import init, Fore, Style
from bs4 import BeautifulSoup

init()



# Define una función para imprimir el texto con animación de colores
def imprimir_texto_animado():
            print(Fore.RED + r'''
                                                                            
     _____           _____         ______  _______        ______  _______   
 ___|\    \     ____|\    \       |      \/       \      |      \/       \  
|    |\    \   /     /\    \     /          /\     \    /          /\     \ 
|    | |    | /     /  \    \   /     /\   / /\     |  /     /\   / /\     |
|    | |    ||     |    |    | /     /\ \_/ / /    /| /     /\ \_/ / /    /|
|    | |    ||     |    |    ||     |  \|_|/ /    / ||     |  \|_|/ /    / |
|    | |    ||\     \  /    /||     |       |    |  ||     |       |    |  |
|____|/____/|| \_____\/____/ ||\____\       |____|  /|\____\       |____|  /
|    /    | | \ |    ||    | /| |    |      |    | / | |    |      |    | / 
|____|____|/   \|____||____|/  \|____|      |____|/   \|____|      |____|/  
  \(    )/        \(    )/        \(          )/         \(          )/     
   '    '          '    '          '          '           '          '      
                                                                           
                           Memphis Menace | JTGS                             
                    EXTRAER CODIGO ESPECIFICO POR CLASE


''' + Style.RESET_ALL)


# Llama a la función para imprimir el texto con animación de colores
imprimir_texto_animado()


def obtener_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(Fore.RED +r"Error al obtener el HTML:", response.status_code + Style.RESET_ALL)
            return None
    except requests.exceptions.RequestException as e:
        print(Fore.RED +r"Error de conexión:", e + Style.RESET_ALL)
        return None

def guardar_html_en_txt(html, ruta_archivo):
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as file:
            file.write(html)
        print("                                                                            ")
        print(Fore.GREEN + r"HTML guardado exitosamente en", ruta_archivo + Style.RESET_ALL)
        print("                                                                            ")
    except IOError as e:
        print(Fore.GREEN + r"Error al escribir en el archivo:", e + Style.RESET_ALL)

def extraer_por_clase(html, clase):
    soup = BeautifulSoup(html, 'html.parser')
    elementos = soup.find_all(class_=clase)
    if elementos:
        return '\n'.join(str(elem) for elem in elementos)
    else:
        return "No se encontraron elementos con la clase especificada."

def extraer_de_archivo(links_file, nombre_base_archivo, ubicacion, extract_part, clase_elemento=None):
    with open(links_file, 'r') as file:
        urls = file.readlines()
    for i, url in enumerate(urls, start=1):
        url = url.strip()
        html = obtener_html(url)
        if html:
            if extract_part == "si":
                parte_html = extraer_por_clase(html, clase_elemento)
                if parte_html:
                    nombre_archivo = f"{nombre_base_archivo}_{i}.html"  
                    ruta_archivo = os.path.join(ubicacion, nombre_archivo)
                    guardar_html_en_txt(parte_html, ruta_archivo)
                else:
                    print(f"No se encontraron elementos con la clase especificada en {url}")
            else:
                nombre_archivo = f"{nombre_base_archivo}_{i}.html"  
                ruta_archivo = os.path.join(ubicacion, nombre_archivo)
                guardar_html_en_txt(html, ruta_archivo)
        else:
            print(f"No se pudo obtener el HTML de {url}")

if __name__ == "__main__":
    links_option = input("¿Desea extraer solo un link o serán varios? (uno/varios): ").lower()
    if links_option == "uno":
        url = input("Introduce la URL de la página web: ")
        html = obtener_html(url)
        if html:
            ubicacion = input("Introduce la ubicación donde deseas guardar el archivo : ")
            nombre_archivo = input("Introduce el nombre del archivo para guardar el HTML (sin extensión): ")
            nombre_archivo = nombre_archivo.strip() + ".html"  
            ruta_archivo = os.path.join(ubicacion, nombre_archivo)
            
            extract_part = input("¿Deseas extraer solo una parte del código HTML? (si/no): ").lower()
            if extract_part == "si":
                clase_elemento = input("Introduce la clase del elemento que deseas extraer: ")
                parte_html = extraer_por_clase(html, clase_elemento)
                if parte_html:
                    guardar_html_en_txt(parte_html, ruta_archivo)
                else:
                    print("No se encontraron elementos con la clase especificada.")
            else:
                guardar_html_en_txt(html, ruta_archivo)
    elif links_option == "varios":
        links_file = input("Introduce la ruta del archivo de texto que contiene los links (cada link en una línea y sin espacios en los lados): ")
        nombre_base_archivo = input("Introduce el nombre base para los archivos HTML: ")
        ubicacion = input("Introduce la ubicación donde deseas guardar los archivos (solo ruta hcia la carpeta donde se guardara): ")
        extract_part = input("¿Deseas extraer solo una parte del código HTML? (si/no): ").lower()
        if extract_part == "si":
            clase_elemento = input("Introduce la clase del elemento que deseas extraer: ")
        else:
           clase_elemento = None
        extraer_de_archivo(links_file, nombre_base_archivo, ubicacion, extract_part, clase_elemento)
    else:
        print("Opción no válida, se asumirá que se desea extraer solo un link.")