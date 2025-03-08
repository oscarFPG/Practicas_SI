
class Param:

    # Tipo de objeto
    OBJETO_ARRIBA = 0
    OBJETO_ABAJO = 1
    OBJETO_DERECHA = 2
    OBJETO_IZQUIERDA = 3

    # Distancia con objeto
    DIST_OBJETO_ARRIBA = 4
    DIST_OBJETO_ABAJO = 5
    DIST_OBJETO_DERECHA = 6
    DIST_OBJETO_IZQUIERDA = 7

    # Posicion jugador
    PLAYER_X = 8
    PLAYER_Y = 9

    # Posicion antena
    COMMAND_X = 10
    COMMAND_Y = 11

    # Posicion de nuestro agente
    AGENT_X = 12
    AGENT_Y = 13

    # Puede volver a disparar y cantidad de vida
    CAN_SHOOT = 14
    VIDA = 15

    # Direccion
    QUIETO = 0
    MOVER_ARRIBA = 1
    MOVER_ABAJO = 2
    MOVER_DERECHA = 3
    MOVER_IZQUIERDA = 4

    # Acciones
    DISPARA = "1"
    NO_DISPARA = "0"

    # Tipos de objetos
    NADA = 0
    MURO_IRROMPIBLE = 1
    MURO = 2
    CENTRO_COMANDO = 3
    PLAYER = 4
    BALA = 5
    OTRO = 6

    # Tipo de codigos
    GREEN = 1010
    BLUE = 2020
    RED = 3030

    def __init__(self):
        return