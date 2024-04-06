# Sistemas de Computacion
Trabajo Practico 2 - Sistemas de Computacion 

---

## Objetivo

Se debe diseñar e implementar una interfaz que muestre el índice GINI. La capa superior recuperará la información del [WorldBank API](https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22). Se recomienda el uso de API Rest y Python. Los datos de consulta realizados deben ser entregados a un programa en C (capa intermedia) que convocará rutinas en ensamblador para que hagan los cálculos de conversión de float a enteros y devuelva el índice de un país como Argentina u otro sumando uno (+1). Luego el programa en C o python mostrará los datos obtenidos.- 

Se debe utilizar el stack para convocar, enviar parámetros y devolver resultados. O sea utilizar las convenciones de llamadas de lenguajes de alto nivel a bajo nivel.

**En una primera iteración resolverán todo el trabajo práctico usando C con Python sin ensamblador. En la siguiente iteración usarán los conocimientos de ensamblador para completar el tp.**

IMPORTANTE: en esta segunda iteración deberán mostrar los resultados con gdb, para ello pueden usar un programa de C puro. Cuando depuren muestran el estado del área de memoria que contiene el stack antes, durante y después de la función.

---

## Requerimientos

Para poder ejecutar el programa se necesita tener instalado Python 3.7+ y GCC para poder compilar la libreria en C. Para la segunda etapa del proyecto se necesita tener instalado gdb y nasm para poder compilar el codigo en assembler. Aun que estas herramientas estan instaladas por defecto en la mayoria de los sistemas operativos, se puede instalar con los siguientes comandos:

```bash
$ sudo apt install build-essential nasm gcc-multilib g++-multilib
```

Las librerias de python necesarias `ctypes`, `tkinter`, `json` y `request` son modulos que vienen por defecto en la instalacion de Python. Pero si no estan instalados se pueden instalar con los siguientes comandos:

```bash
$ pip3 install requests
$ pip3 install json
$ pip3 install ctypes
$ pip3 install tkinter
```

En caso de que falle la instalación de la librería tkinter, se puede probar en sistemas operativos basados en Debian el siguiente comando:

```bash
$ sudo apt install python3-tk
```

---

## Ejecucion

En esta primera parte de la implementacion solamente se utilizo Python y una libreria un C, mediante ctypes, para realizar la conversion de float a entero. Para ejecutar el programa se debe correr el siguiente comando desde la carpeta root del proyecto.

```bash
~/sdc_tp2$ sh build.sh
~/sdc_tp2$ sh launch.sh
    -> Executing script ...
```
Luego se mostrara un menu con la lista de paises disponibles para consultar el indice GINI. Se debe pueden seleccionar diferentes paises y se mostraran los mismos en pantalla, con su valor redondeado a entero.

<p align="center">
  <img src="./imgs/sequence_diagram.drawio.png" alt="Diagrama de secuencias"><br>
  <ei>Fig 1. Diagrama de secuencias.</em>
</p>

<p align="center">
  <img src="./imgs/exec.png" alt="Ejemplo de ejecucion"><br>
  <ei>Fig 2. Ejemplo de ejecucion.</em>
</p>

---

[World countries json](https://github.com/stefangabos/world_countries/tree/master)

[Informe del desarrollo](https://docs.google.com/document/d1jW9MoEiCJ7JhiNN3AmMY-2FMexjHuQbrLYXATDKkyik/edit?usp=sharing)
