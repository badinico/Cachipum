from logica_opciones import log_piedra, log_papel, log_tijera


def logica(player_1, player_2):
    # Llamamos a las funciones auxiliares según la elección de cada jugador
    if player_1 == 'piedra':
        point_p1, point_p2 = log_piedra(player_1, player_2)
    elif player_1 == 'papel':
        point_p1, point_p2 = log_papel(player_1, player_2)
    elif player_1 == 'tijera':
        point_p1, point_p2 = log_tijera(player_1, player_2)
    
    return point_p1, point_p2