import httpx
import asyncio

async def download_image(url):
    # Descargar la imagen desde la URL proporcionada
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
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

async def main():
    # Leer las URLs de las imágenes desde el archivo
    urls = []
    with open("img_url.txt", "r") as file:
        urls = file.readlines()

    tasks = []
    for url in urls:
        # Eliminar espacios en blanco y saltos de línea
        url = url.strip()
        
        # Crear una tarea para descargar cada imagen
        task = asyncio.create_task(download_image(url))
        tasks.append(task)

    # Esperar a que todas las tareas terminen
    await asyncio.gather(*tasks)

    # Imprimir mensaje de finalización
    print("Programa finalizado")

if __name__ == "__main__":
    asyncio.run(main())
