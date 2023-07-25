from logica_opciones import log_piedra, log_papel, log_tijera
from logica import logica
from validador_opciones import opcion_valida
from config import juego

def main():
    point_p1 = 0
    point_p2 = 0
    juegos = juegos
    
    while point_p1 < juegos and point_p2 < juegos:
        player_1 = input("Jugador 1: ")  # Pedimos la opción al Jugador 1
        
        # Verificamos si la opción ingresada por el jugador es válida
        while not opcion_valida(player_1):
            print("Opción inválida. Debes elegir 'piedra', 'papel' o 'tijera'.")
            player_1 = input("Jugador 1: ")
        
        player_2 = input("Jugador 2: ")  # Pedimos la opción al Jugador 2
        
        # Verificamos si la opción ingresada por el jugador 2 es válida
        while not opcion_valida(player_2):
            print("Opción inválida. Debes elegir 'piedra', 'papel' o 'tijera'.")
            player_2 = input("Jugador 2: ")
        
        P1, P2 = logica(player_1, player_2)  # Llamamos a la función logica para determinar el ganador
        
        if P1:
            point_p1 += 1  # Sumamos un punto al Jugador 1 si ganó
            print("Gana Jugador 1")
        elif P2:
            point_p2 += 1  # Sumamos un punto al Jugador 2 si ganó
            print("Gana Jugador 2")
        else:
            print("Empate")
            
    print("Puntaje final - Jugador 1:", point_p1, "Jugador 2:", point_p2)
    
main()
