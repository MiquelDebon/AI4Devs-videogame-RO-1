# Videojuego - Buscaminas

Quiero que generes el código completo de un juego clásico de Buscaminas implementado en Python para ejecutarse en escritorio, con las siguientes características:

1. **Lenguaje**: Python 3.x
2. **Interfaz gráfica**: Aplicacion de escritorio
3. **Funcionamiento**:
   - Tablero cuadrado con tamaño configurable (por ejemplo, 10x10).
   - Número de minas configurable.
   - Al hacer clic izquierdo en una celda:
     - Si hay una mina: se muestra una bomba y el juego termina.
     - Si no hay mina: se muestra el número de minas adyacentes.
     - Si no hay minas adyacentes, se revelan automáticamente las celdas vecinas vacías.
   - Al hacer clic derecho en una celda: se coloca o quita una bandera.
   - El juego debe detectar si el usuario ha ganado (descubrió todas las celdas sin minas) o perdió.
4. **Interfaz amigable**:
   - Iconos simples (puedes usar emojis como 💣 o 🚩).
   - Colores para distinguir celdas abiertas, banderas y minas.
5. **Organización del código**:
   - Usa clases para separar la lógica del juego y la interfaz.
   - Nombra bien las funciones y variables.
6. **Extras deseables** (si es posible):
   - Mostrar un mensaje de victoria o derrota al final del juego.
   - Permitir reiniciar el juego sin cerrar la ventana (opcional).

Además del código, proporciona un archivo `README.md` con:

- Requisitos para ejecutar el juego (por ejemplo, tener Python y tkinter).
- Instrucciones claras de instalación y ejecución.
- Instrucciones de cómo se juega.
- Opciones para cambiar dificultad (por ejemplo, modificar tamaño y minas en el código).
- Cualquier sugerencia útil para extender el proyecto.

Escribe todo el código en un solo archivo `.py`, documentado, y que funcione directamente al ejecutarlo. No uses librerías externas.

Antes de empezar planteame 3 principales dudas que tienes para generar el juego
