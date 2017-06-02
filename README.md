# PuntuacionePeliculas_Python

Este proyecto consiste en obtener las puntuaciones de las películas que desee el usuario, además se calcula la media de la puntuación de las películas en varias páginas (imdb y filmaffinity). Una vez finalizado el proceso podemos encontrar el resultado en Dropbox.

## Tecnologías

Este proyecto utiliza:

* ZeroMQ 
* Python
* Scrapy
* Dropbox

## Como ejecutarlo

* El primer paso es subir un fichero a dropbox con una lista de películas separadas por un salto de línea.
* Seguidamente se lanzan el servidor y los workers (se utilizan tantos workers como películas).
* Posteriormente se ejecuta el cliente, introduciendo por consola el nombre del fichero en dropbox (que se la pasará al servidor).
* Una vez finalizado los procesos, podemos ver el resultado en Dropbox.

