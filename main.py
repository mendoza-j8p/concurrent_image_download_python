import requests
import threading

def download_image(url):
    # Descargar la imagen desde la URL proporcionada
    response = requests.get(url)
    
    # Verificar si la descarga fue exitosa
    if response.status_code == 200:
        # Generar el nombre del archivo a partir de la URL
        filename = "downloaded_" + url.split("/")[-1]
        
        # Guardar la imagen descargada en un archivo local
        with open(filename, "wb") as file:
            file.write(response.content)
        
        # Imprimir el nombre del archivo descargado
        print(f"Imagen descargada: {filename}")
    else:
        # Imprimir un mensaje de error si la descarga falló
        print(f"No se pudo descargar la imagen: {url}")

def main():
    # Leer las URLs de las imágenes desde el archivo
    urls = []
    with open("img_url.txt", "r") as file:
        urls = file.readlines()

    threads = []
    for url in urls:
        # Eliminar espacios en blanco y saltos de línea
        url = url.strip()
        
        # Crear un hilo para descargar cada imagen
        thread = threading.Thread(target=download_image, args=(url,))
        thread.start()
        threads.append(thread)

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()

    # Imprimir mensaje de finalización
    print("Programa finalizado")

if __name__ == "__main__":
    main()
