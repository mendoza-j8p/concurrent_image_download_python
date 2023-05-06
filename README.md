# Proyecto descarga de imagenes concurrente en python con THREADS

1. Obtén la lista de URLs de las imágenes que deseas descargar, ya sea desde un archivo, una lista predefinida o una entrada del usuario.

2. Define una función que tome una URL como argumento y descargue la imagen correspondiente utilizando la biblioteca requests u otra biblioteca adecuada para realizar solicitudes HTTP.

3. Crea hilos o procesos para realizar las descargas de forma concurrente. Por cada URL en la lista, crea un hilo o proceso que llame a la función de descarga.

4. Utiliza técnicas de sincronización, como semáforos o bloqueos, para controlar el acceso concurrente a los recursos compartidos, como el contador de descargas finalizadas.

5. Espera a que todos los hilos o procesos terminen utilizando métodos como join().

6. Al finalizar todas las descargas, muestra un mensaje indicando el número total de descargas realizadas.

## Conclusión

En este código, se lee el archivo img_url.txt para obtener la lista de URLs de las imágenes a descargar. Luego, se crean hilos para cada URL y se llama a la función download_image pasando la URL como argumento. Cada hilo realiza la descarga de la imagen correspondiente y guarda el archivo localmente.

Después de iniciar todos los hilos, se utiliza el método join() para esperar a que todos los hilos terminen antes de finalizar el programa.

Este es solo un ejemplo básico y aun es necesario agregar manejo de errores, sincronización adicional y otras mejoras.

## Cambios para usar COROUTINES

Las principales modificaciones son:

- Se ha importado el módulo httpx en lugar de requests ya que httpx es una biblioteca compatible con asyncio.

- La función download_image se ha convertido en una función asíncrona utilizando el prefijo async y se ha usado el objeto httpx.AsyncClient() en lugar de requests.get().

- La función main también se ha convertido en una función asíncrona utilizando el prefijo async y se ha utilizado asyncio.create_task() para crear una tarea para cada descarga de imagen en lugar de crear un hilo para cada descarga.

- En lugar de esperar a que cada hilo termine, se utiliza asyncio.gather() para esperar a que todas las tareas se completen.

En resumen, el código ha sido modificado para utilizar las características de asyncio en lugar de crear y ejecutar múltiples hilos.

## Porque el cambio?

En el código original se utilizaban threads para descargar las imágenes, lo que funciona bien pero tiene algunos inconvenientes como el alto consumo de recursos y la complejidad que puede aumentar a medida que se manejan más hilos.

Al utilizar coroutines con asyncio, se logra una mejor gestión de los recursos al permitir que una tarea sea suspendida temporalmente mientras se espera que una operación de entrada/salida (como una solicitud a un servidor) se complete, liberando así el ciclo de CPU para realizar otras tareas en lugar de esperar bloqueado. Además, se puede manejar muchas tareas con una sola hebra, lo que reduce la complejidad y el costo de crear y administrar hilos.

En general, el uso de coroutines con asyncio es más apropiado para proyectos que realizan operaciones de entrada/salida, como solicitudes a servidores o lectura/escritura de archivos, y donde se necesite un alto nivel de concurrencia.

## Diferencias entre THREAD y COROUTINES

La elección entre usar hilos o corutinas depende de la naturaleza del problema que se esté tratando de resolver y del contexto en el que se esté desarrollando la aplicación.

En general, el uso de corutinas (como los proporcionados por asyncio) es más adecuado para aplicaciones que requieren una gran cantidad de entrada/salida (E/S), como aplicaciones de red y de E/S intensiva. Las corutinas pueden ser más eficientes que los hilos porque son más livianas y no tienen el sobrecarga asociada con el cambio de contexto y la asignación de recursos que implica la creación y destrucción de hilos.

Sin embargo, si su aplicación implica un procesamiento intensivo de la CPU, como cálculos matemáticos complejos o algoritmos de aprendizaje automático, puede ser más adecuado usar hilos o procesos en lugar de corutinas. Esto se debe a que las corutinas se ejecutan en un solo hilo, mientras que los hilos pueden ejecutarse en varios núcleos de CPU para aprovechar la potencia de procesamiento de la CPU.
