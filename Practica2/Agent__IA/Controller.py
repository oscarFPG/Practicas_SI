from Agent__IA.State import State
from Agent__IA.Direction import Direction

class Controller:

    DEBUG = True

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

    # Posicion agente
    AGENT_X = 12
    AGENT_Y = 13

    # Puede volver a disparar y cantidad de vida
    CAN_SHOOT = 14
    VIDA = 15


    def __init__(self):
        self.state = State()
        self._percepciones = []
        self._gameover = False
        self._destroyed = False


    def recibirEntorno(self, perceptions, gameover, destroyed):

        # Tipo de objeto
        self._percepciones.append(perceptions[self.OBJETO_ARRIBA])
        self._percepciones.append(perceptions[self.OBJETO_ABAJO])
        self._percepciones.append(perceptions[self.OBJETO_DERECHA])
        self._percepciones.append(perceptions[self.OBJETO_IZQUIERDA])

        # Distancia con objeto
        self._percepciones.append(perceptions[self.DIST_OBJETO_ARRIBA])
        self._percepciones.append(perceptions[self.DIST_OBJETO_ABAJO])
        self._percepciones.append(perceptions[self.DIST_OBJETO_DERECHA])
        self._percepciones.append(perceptions[self.DIST_OBJETO_IZQUIERDA])

        # Posicion jugador
        self._percepciones.append(perceptions[self.PLAYER_X])
        self._percepciones.append(perceptions[self.PLAYER_Y])

        # Posicion antena
        self._percepciones.append(perceptions[self.COMMAND_X])
        self._percepciones.append(perceptions[self.COMMAND_Y])

        # Posicion agente
        self._percepciones.append(perceptions[self.AGENT_X])
        self._percepciones.append(perceptions[self.AGENT_Y])

        # Puede volver a disparar y cantidad de vida
        self._percepciones.append(perceptions[self.CAN_SHOOT])
        self._percepciones.append(perceptions[self.VIDA])

        # Parametros de la partida
        self._gameover = gameover
        self._destroyed = destroyed

    def reaccionar(self):

        if(self.DEBUG):
            print("Percepciones:")
            for elem in self._percepciones:
                print(elem)

            print("Gameover:")
            print(self._gameover)

            print("Destroyed:")
            print(self._destroyed)


        self.state.execute(self._percepciones)
        self.state.nextState()
        self._percepciones.clear()

        return 0, self.shoot(False)