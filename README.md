# Proyecto 3 Mate Discreta

## Descripción
Este proyecto es una calculadora gráfica que permite realizar operaciones aritméticas modulares, como suma, resta, multiplicación, división y exponenciación, sobre enteros, dentro de un sistema modular. La aplicación está construida con una interfaz gráfica usando Tkinter. También permite manejar expresiones complejas que incluyen paréntesis y operaciones combinadas, además de cambiar el módulo sobre el cual se opera dinámicamente.

## Estructura del Proyecto
UI.py: La interfaz gráfica principal de la calculadora.
Evaluador.py: Evaluador que procesa y calcula el valor de expresiones aritméticas modulares.
ModularArithmetic.py: Implementa las operaciones aritméticas modulares.
Utilerias.py: Función auxiliar para verificar si un número es primo.
Instrucciones de Uso
Requisitos previos
Python 3.x
Tkinter instalado (viene por defecto en la mayoría de las distribuciones de Python)
Ejecutar la Calculadora
Para ejecutar la calculadora, simplemente ejecuta el archivo UI.py:


## Usar la Calculadora
Ingresar Expresiones: Introduce expresiones aritméticas en el campo de entrada. Puedes usar operaciones como suma (+), resta (-), multiplicación (*), división (/), y potencia (^).

Ejemplo: 7^3 + 4 * 5
Cambiar Módulo: Para especificar un nuevo módulo, usa la palabra clave mod seguida del número primo que quieras utilizar como módulo.

Ejemplo: (7^3 + 4 * 5) mod 23
Evaluar Expresiones: Después de ingresar una expresión, presiona = para evaluarla. El resultado aparecerá en la pantalla de la calculadora.

Limpiar la Pantalla: Presiona el botón C para limpiar la pantalla y comenzar una nueva operación.

## Operadores Disponibles
+: Suma
-: Resta
*: Multiplicación
/: División
^: Potencia
mod: Establece el módulo bajo el cual se realizarán las operaciones (debe ser un número primo).
Ejemplo de Expresiones
Potencia Modular: 7^3 mod 23
Suma y Producto Modular: (7 + 5) * 3 mod 13
Expresión Compleja: (7^3 + 4 * 5) * 2 mod 23
Archivos del Proyecto
1. UI.py
Este archivo contiene la interfaz gráfica desarrollada con Tkinter. En ella se colocan los botones numéricos, los operadores aritméticos y el botón de igual (=) que permite evaluar las expresiones ingresadas.

2. Evaluador.py
Contiene la clase ModularEvaluator, que es responsable de analizar y evaluar las expresiones aritméticas, aplicando las operaciones correspondientes y manejando correctamente el uso de paréntesis. Además, procesa el operador mod para cambiar el módulo utilizado en las operaciones.

3. ModularArithmetic.py
Este archivo implementa las operaciones aritméticas modulares como suma, resta, multiplicación, división y exponenciación. Todas las operaciones son realizadas bajo un módulo que puede ser configurado mediante la función set_modulo.

4. Utilerias.py
Contiene la función es_primo, que verifica si un número es primo, ya que el módulo debe ser un número primo para que ciertas operaciones modulares, como la división, sean válidas.

## Autores

Iris Ayala, Gabriel Bran, Jonathan Diaz, David Dominguez, Luis Padilla, Anggie Quezada