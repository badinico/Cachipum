# Juego de Piedra, Papel o Tijeras en Python

## Descripción

Este es un simple juego de Piedra, Papel o Tijeras implementado en Python. Permite a dos jugadores competir en una serie de rondas, y el jugador que gane la mayoría de las rondas es declarado como el ganador.

## Cómo jugar

Cada jugador debe ingresar su elección en cada ronda: 'piedra', 'papel' o 'tijera'. Luego, el programa determinará el ganador según las reglas clásicas del juego.

## Código

```python
def log_tijera(p1, p2):
    if p1 == 'tijera' and p2 == 'piedra':
        return False, True
    elif p1 == 'tijera' and p2 == 'papel':
        return True, False
    elif p1 == 'tijera' and p2 == 'tijera':
        return False, False

def log_papel(p1, p2):
    if p1 == 'papel' and p2 == 'tijera':
        return False, True
    elif p1 == 'papel' and p2 == 'piedra':
        return True, False
    elif p1 == 'papel' and p2 == 'papel':
        return False, False

def log_piedra(p1, p2):
    if p1 == 'piedra' and p2 == 'papel':
        return False, True
    elif p1 == 'piedra' and p2 == 'tijera':
        return True, False
    elif p1 == 'piedra' and p2 == 'piedra':
        return False, False

def logica(player_1, player_2):
    # Llamamos a las funciones auxiliares según la elección de cada jugador
    if player_1 == 'piedra':
        point_p1, point_p2 = log_piedra(player_1, player_2)
    elif player_1 == 'papel':
        point_p1, point_p2 = log_papel(player_1, player_2)
    elif player_1 == 'tijera':
        point_p1, point_p2 = log_tijera(player_1, player_2)
  
    return point_p1, point_p2

def opcion_valida(opcion):
    return opcion in ['piedra', 'papel', 'tijera']

def main():
    # El código principal del juego está aquí...

if __name__ == "__main__":
    main()
```


## Requisitos

* Python 3.x

## Ejecución

1. Clona este repositorio o descarga el archivo ZIP.
2. Abre una terminal y navega hasta el directorio del juego.
3. Ejecuta el juego con el comando: `python juego_piedra_papel_tijeras.py`

¡Diviértete jugando Piedra, Papel o Tijeras en Python!

Recuerda reemplazar `tuusuario` y `turepo` con tu nombre de usuario y el nombre de tu repositorio en GitHub, respectivamente. Además, asegúrate de agregar una imagen relacionada con el juego en la sección `Descripción`.

Espero que esta versión del `README.md` sea llamativa y creativa para tu proyecto. ¡Diviértete y buena suerte! Si tienes alguna otra pregunta o necesitas más ayuda, no dudes en preguntar.
