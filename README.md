# Sistemas de Computacion
Trabajo Practico 2 - Sistemas de Computacion 

---

## Objetivo

Se debe diseñar e implementar una interfaz que muestre el índice GINI. La capa superior recuperará la información del [WorldBank API](https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22). Se recomienda el uso de API Rest y Python. Los datos de consulta realizados deben ser entregados a un programa en C (capa intermedia) que convocará rutinas en ensamblador para que hagan los cálculos de conversión de float a enteros y devuelva el índice de un país como Argentina u otro sumando uno (+1). Luego el programa en C o python mostrará los datos obtenidos.- 

Se debe utilizar el stack para convocar, enviar parámetros y devolver resultados. O sea utilizar las convenciones de llamadas de lenguajes de alto nivel a bajo nivel.

En una primera iteración resolverán todo el trabajo práctico usando c con python sin ensamblador. En la siguiente iteración usarán los conocimientos de ensamblador para completar el tp.

**IMPORTANTE: en esta segunda iteración deberán mostrar los resultados con gdb, para ello pueden usar un programa de C puro. Cuando depuren muestran el estado del área de memoria que contiene el stack antes, durante y después de la función.**

---

## Requerimientos

Para poder ejecutar el programa se necesita tener instalado Python 3.7+ y gcc para poder compilar la libreria en C. Tambien para la segunda etapa del proyecto se necesita tener instalado gdb y nasm para poder compilar el codigo en assembler. Aun que estas herramientas estan instaladas por defecto en la mayoria de los sistemas operativos, se puede instalar con los siguientes comandos.

```bash
sudo apt install build-essential nasm gcc-multilib g++-multilib
```

Las librerias de python necesarias `ctypes`, `tkinter` y `json` son modulos que vienen por defecto en la instalacion de Python. Pero para hacer los requests a la REST API se necesita instalar la libreria `requests`.

```bash
$ pip3 install requests
```

---

## Ejecucion

En esta primera parte de la implementacion solamente se utilizo Python y una libreria un C, mediante ctypes, para realizar la conversion de float a entero. Para ejecutar el programa se debe correr el siguiente comando desde la carpeta root del proyecto.

```bash
$ sh build.sh
$ python3 ./src/main.py
```
Luego se mostrara un menu con la lista de paises disponibles para consultar el indice GINI. Se debe pueden seleccionar diferentes paises y se mostraran los mismos en pantalla, con su valor redondeado a entero.

---

[JSON con paises y su alpha-3 code](https://github.com/stefangabos/world_countries/tree/master)

[Informe](https://docs.google.com/document/d1jW9MoEiCJ7JhiNN3AmMY-2FMexjHuQbrLYXATDKkyik/edit?usp=sharing)
