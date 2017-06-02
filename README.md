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
* Para que funcione hay que añadir el token para autentificarnos en dropbox en el archivo servidorv1.py, en la línea 20.

## Capturas

**Subir archivo a dropbox con la lista de películas**

![captura01](https://github.com/josevc93/PuntuacionePeliculas_Python/blob/master/img/1.jpg)

**Se lanza el servidor**

![captura02](https://github.com/josevc93/PuntuacionePeliculas_Python/blob/master/img/2.jpg)

**Se lanzan los workers**

![captura03](https://github.com/josevc93/PuntuacionePeliculas_Python/blob/master/img/3.jpg)

**Se lanza el cliente**

![captura04](https://github.com/josevc93/PuntuacionePeliculas_Python/blob/master/img/4.jpg)

**Obtenemos el resultado en dropbox**

![captura05](https://github.com/josevc93/PuntuacionePeliculas_Python/blob/master/img/5.jpg)
