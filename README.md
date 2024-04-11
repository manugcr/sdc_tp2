# Sistemas de Computacion
Trabajo Practico 2 - Sistemas de Computacion 

## Stack frame

**Integrantes:**
- [Gil Cernich, Manuel](https://github.com/manugcr/)
- [Pallardo, Agustin](https://github.com/djpallax)
- [Saporito, Franco](https://github.com/fasaporito)

---

## Objetivo

Se debe diseñar e implementar una interfaz que muestre el índice GINI. La capa superior recuperará la información del [WorldBank API](https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22). Se recomienda el uso de API Rest y Python. Los datos de consulta realizados deben ser entregados a un programa en C (capa intermedia) que convocará rutinas en ensamblador para que hagan los cálculos de conversión de float a enteros y devuelva el índice de un país como Argentina u otro sumando uno (+1). Luego el programa en C o python mostrará los datos obtenidos.- 

Se debe utilizar el stack para convocar, enviar parámetros y devolver resultados. O sea utilizar las convenciones de llamadas de lenguajes de alto nivel a bajo nivel.

En una primera iteración resolverán todo el trabajo práctico usando C con Python sin ensamblador. En la siguiente iteración usarán los conocimientos de ensamblador para completar el tp.

**IMPORTANTE: en esta segunda iteración deberán mostrar los resultados con gdb, para ello pueden usar un programa de C puro. Cuando depuren muestran el estado del área de memoria que contiene el stack antes, durante y después de la función.**

---
## Requerimientos

### Enviroment
En este trabajo buscamos compilar assembler x86 de 32bits sobre Python 3.7 de 64bits, lo cual no es compatible. Una posible solucion encontrada es utilizar un enviroment gracias a conda, la cual nos permite crear y gestionar entornos de desarrollo independientes, lo que facilita trabajar con diferentes versiones de paquetes y dependencias sin conflictos.

Para instalarla se puede seguir los siguientes pasos para un sistema linux, encontrados en la [pagina oficial](https://docs.anaconda.com/free/miniconda/):

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

Luego de instalarlo hay que agregar la ruta al PATH del sistema, para que se pueda acceder a los comandos de conda desde cualquier lugar. Para ello se debe agregar a `.bashrc` la linea `export PATH="/home/usr/miniconda3/bin:$PATH"`. Una vez agregado se debe actualizar el archivo de configuracion:

```bash
usr@hostname:~$ source ~/.bashrc
```

Ya instalado miniconda, se debe crear un enviroment con la version de Python 3.7 32bits y activarlo:

```bash
(base) usr@hostname:~$ conda create -n py32 python=3.7 -c https://repo.anaconda.com/pkgs/main/linux-32/ --override-channels
(py32) usr@hostname:~$ conda activate py32
```

Podemos corroborar que nuestro enviroment esta bien configurado ejecutando el siguiente comando:

```bash
(py32) usr@hostname:~$ python -c "import platform; print(platform.architecture())"
('32bit', 'ELF')
```

### Librerias
Para poder ejecutar el programa se necesita tener instalado Python 3.7+ y GCC para poder compilar la libreria en C. Para la segunda etapa del proyecto se necesita tener instalado gdb y nasm para poder compilar el codigo en assembler. Aun que estas herramientas estan instaladas por defecto en la mayoria de los sistemas operativos, se puede instalar con los siguientes comandos:

```bash
~$ sudo apt install build-essential nasm gcc-multilib g++-multilib
```

Las librerias de python necesarias `ctypes`, `tkinter`, `json`, `matplot` `request` son modulos que vienen por defecto en la instalacion de Python. Pero si no estan instalados se pueden instalar con los siguientes comandos:

```bash
pip3 install requests
pip3 install json
pip3 install ctypes
pip3 install tkinter
pip3 install matplotlib
```

En caso de que falle la instalación de la librería tkinter, se puede probar en sistemas operativos basados en Debian el siguiente comando:

```bash
sudo apt install python3-tk
```

---

## Ejecucion

Para la segunda parte de la implementacion se utilizo Python y una libreria un C, mediante ctypes, la cual luego llama a una rutina de assembler para realizar la conversion de float a entero, y sumarle uno. Para ejecutar el programa se debe correr el siguiente comando desde la carpeta root del proyecto.

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

Como vemos en el diagrama de ejecucion, se implemento una libreria en C que se encarga de realizar la conversion de float a entero. Esta libreria se compila y se carga en memoria para poder ser utilizada por el script de Python. 

Una vez que se carga la libreria, desde python se creo una GUI con `tkinter` para poder seleccionar el pais a consultar. Seleccionado el pais, se realiza la consulta a la API de WorldBank y se obtiene el indice GINI del pais seleccionado. Luego se llama a la funcion de la libreria en C para realizar la conversion de float a entero y se muestra el resultado en pantalla.

Para mayor comodidad a la hora de elegir el pais, se implemento un json con la lista de paises y sus respectivos codigos de pais. De esta forma se puede seleccionar el pais por su nombre y se obtiene el codigo de pais para realizar la consulta a la API, sin necesidad de tener que escribir el pais a buscar.

<p align="center">
  <img src="./imgs/exec.png" alt="Ejemplo de ejecucion"><br>
  <ei>Fig 2. Ejemplo de ejecucion.</em>
</p>

# **...(Completar y arreglar)**

---

## API REST
Una API REST es una interfaz que opera sobre el protocolo HTTP, utilizando sus métodos estándar (GET, POST, PUT, DELETE) para realizar operaciones sobre recursos específicos. Estos recursos pueden ser datos, servicios o cualquier otro elemento que la API proporcione acceso.

En este caso entre el sistema de WorldBank y el sistema de la aplicacion. La misma permite realizar consultas a la base de datos y obtener la informacion de los paises y sus indices.

Funcionalidades de las API Rest:
- **GET**: Se emplea para solicitar datos de recursos específicos. En el contexto de WorldBank, podría ser utilizado para obtener información sobre los índices GINI de diversos países.
- **POST**: Se utiliza para enviar informacion a la base de datos.
- **PUT**: Se utiliza para actualizar informacion en la base de datos.
- **DELETE**: Se utiliza para eliminar informacion de la base de datos.

Codigos de respuesta:
- **200**: OK. La solicitud ha tenido éxito.
- **201**: Creado. La solicitud ha tenido éxito y se ha creado un nuevo recurso como resultado.
- **400**: Solicitud incorrecta. La solicitud no se pudo procesar debido a un error del cliente.
- **401**: No autorizado. El cliente debe autenticarse para obtener la respuesta solicitada.
- **404**: No encontrado. El servidor no pudo encontrar el recurso solicitado.
- **500**: Error interno del servidor. El servidor ha encontrado una situación inesperada que le impide cumplir con la solicitud.


En este caso se utilizo el metodo GET para obtener la informacion de los paises y sus indices GINI. La informacion se obtuvo en formato JSON y se parseo para obtener los datos necesarios, ya que se obtiene una lista de paises con sus respectivos indices, y a su vez una lista con los diferentes indices de cada año. Pero para evitar la complejidad de tener que seleccionar el año, se selecciono el indice mas actual para mostrar en pantalla.

---
## Libreria en C
Un archivo `.so` es un archivo de biblioteca compartida, que contiene funciones que pueden ser utilizadas por otros programas, estos archivos son similares a los archivos `.dll` en Windows.

Para poder utilizar una libreria en C desde Python se utilizo la libreria `ctypes`. Esta libreria permite cargar una libreria en C en memoria y poder utilizar las funciones de la misma desde Python. Para ello primero se debe compilar el codigo en C en un archivo `.so` en sistemas linux. Para ello se utilizo el script en bash `build.sh` que ejecuta los siguientes comandos:

```bash
# Compiling the C code into an object file.
gcc -c -m32 -Wall -Werror -fpic ./src/gini_manipulation.c -o ./build/gini_manipulation_c.o

# Assemble the asm file into and object file.
nasm -f elf32 ./src/gini_manipulation_asm.asm -o ./build/gini_manipulation_asm.o

# Link both object files into a shared library.
gcc -m32 -shared -o ./include/libgini.so ./build/gini_manipulation_c.o ./build/gini_manipulation_asm.o
```

Como dijimos anteriormente, la libreria en C se encarga de llamar a una rutina en assembler 32bits, por ello se necesito de nasm y se utilizo la flag `-m32`.

Luego para linkear nuestra libreria `libgini.so` con el script de Python, se deben definir los tipos de entrada y retorno de la funcion en C.

```python
import ctypes
libgini = ctypes.CDLL('./include/libgini.so')
libgini._gini_manipulation.argtypes = [ctypes.c_float]
libgini._gini_manipulation.restype = ctypes.c_int
```

---
## Profiling de la aplicacion
El profiling es una técnica que se utiliza para analizar el rendimiento de un programa y determinar qué partes del código consumen más recursos y cuáles son las que más tiempo tardan en ejecutarse. 

En nuestro trabajo se utilizo una llamada a funcion desde una libreria en C sobre Python, con el proposito de mejorar el rendimiento de la aplicacion. Para poder analizar el rendimiento de la aplicacion se utilizo la libreria `timeit` de Python, la cual toma los tiempos de ejecucion de una funcion y los muestra en pantalla.

Como nuestra aplicacion principal se ejecuta desde Python, nos parecio correcto hacer esta medicion sobre el python mismo, y no compararla directamente con la libreria de C.

Para ello creamos una funcion en Python que simula la conversion de un float a un entero, y luego se ejecuta la funcion de conversion de la libreria en C. Se toman los tiempos de ejecucion de ambas funciones y se muestran en pantalla.

```python
# Python equivalent of the C function
def gini_manipulation(gini_index):
    gini_index_int = int(gini_index)
    return gini_index_int + 1
```

```c
// C function 
int _gini_manipulation(float gini_index) 
{
    int gini_index_int = (int)gini_index;
    return gini_index_int + 1;
}
```

```asm
; Assembler function
section .text
    global gini_manipulation_asm

gini_manipulation_asm:
    push ebp
    mov ebp, esp

    ; Convert float to int
    fld dword [ebp+8]
    fistp dword [ebp-4]

    ; Add 1 to the integer
    mov eax, dword [ebp-4]
    add eax, 1

    ; Exit
    mov esp, ebp
    pop ebp
    ret    
```

Al correr el script de profiling para que convierta el numero 42.3 por 1.000.000 de veces consecutivas se obtienen los siguientes resultados:

```bash
~/sdc_tp2$ python3 ./profiling/profiling.py 
  Time taken by C+asm code: 0.698672358004842
  Time taken by C code: 0.7135395390214399
  Time taken by Python code: 0.2677964539907407
```

Como podemos observar los tiempos de ejecucion de la funcion en C es mayor que la funcion en Python, al contrario de lo que se esperaba. Pero creemos que esto se debe a que llamar a una funcion en C desde Python tiene un overhead mayor que llamar a una funcion en Python directamente. 

Tambien se puede observar que la funcion en assembler es mas rapida que la funcion en C, lo cual era lo esperado, ya que el assembler es un lenguaje de bajo nivel y se ejecuta directamente sobre el hardware, mientras que el C es un lenguaje de mas alto nivel y necesita ser compilado.

# **...(Completar y arreglar)**

---
## TO DO

Unit tests:
- Profiling de Python con C y Assembler.
- Test de validacion de datos de la API
- Validacion de sistema y de usuario

---
## Informacion externa utilizada

- [World countries json](https://github.com/stefangabos/world_countries/tree/master)
- [Miniconda](https://docs.anaconda.com/free/miniconda/)
