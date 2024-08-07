# Proyecto 1 Mate Discreta

## Descripción
Este proyecto es una aplicación para manejar y operar conjuntos utilizando una interfaz gráfica construida con Tkinter. Puedes crear conjuntos manualmente o utilizando operaciones entre conjuntos existentes, y luego realizar diversas operaciones sobre ellos.

## Estructura del Proyecto

- **App**: La interfaz gráfica principal.
- **Funciones**: Implementa las operaciones sobre conjuntos.
- **Evaluador de Conjuntos**: Evalúa las expresiones que contienen operaciones entre conjuntos.
- **Utilerias**: Funciones auxiliares para la manipulación de los conjuntos.

## Instrucciones de Uso
Para ejecutar el programa, simplemente ejecuta el archivo principal: App.py
### Crear Conjuntos

1. **Manual**: 
   - Ingresar los elementos del conjunto separados por comas en el campo de entrada.
   - Ejemplo: `1,3,(1,2)`
   - Hacer clic en "New" para crear el conjunto.

2. **Con Operaciones**:
   - Ingresar la expresión de la operación en el campo de entrada. 
   - Utilizar los nombres de los conjuntos y operadores separados por espacios.
   - Ejemplo: `(A uni B) int C`
   - Hacer clic en "New" para crear el conjunto resultante de la operación.

### Operar Conjuntos

1. Ingresar la expresión de la operación en el campo de entrada.
   - Utilizar los nombres de los conjuntos y operadores separados por espacios.
   - Ejemplo: `(A uni B) int C`
2. Hacer clic en "Operar" para obtener el resultado de la operación, que se mostrará en el área de resultados.

### Operadores Disponibles

- `uni`: Unión
- `int`: Intersección
- `dif`: Diferencia
- `com`: Complemento
- `fun`: Verificar si es función
- `pro`: Producto cartesiano

### Notas Importantes

- Los elementos del conjunto deben separarse por comas.
- Las operaciones deben estar asociadas con paréntesis y separadas por espacios.
- Los nombres de los conjuntos son: `U`, `A`, `B`, ..., `Z`.

## Ejemplos de Uso

### Crear un Conjunto Manualmente

Entrada: `1, 2, 3, (4, 5)`

### Crear un Conjunto Mediante Operaciones

Entrada: `(A uni B) int C`

### Operar Conjuntos

Entrada: `(A int B) dif C`

## Autores

Iris Ayala, Gabriel Bran, Jonathan Diaz, David Dominguez, Luis Padilla, Anggie Quezada