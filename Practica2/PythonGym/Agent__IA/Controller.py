from Agent__IA.Parameters import Param
from Agent__IA.Idle import Idle
from Agent__IA.Explorar import Explorar
from Agent__IA.Alerta import Alerta
from Agent__IA.Atacar import Atacar

class Controller:

    DEBUG = True
    CODIGO = None

    def __init__(self):
        self.state = Idle()
        self._percepciones = []
        self._gameover = False
        self._destroyed = False


    def recibirEntorno(self, perceptions, gameover, destroyed):

        # Tipo de objeto
        self._percepciones.append(perceptions[Param.OBJETO_ARRIBA])
        self._percepciones.append(perceptions[Param.OBJETO_ABAJO])
        self._percepciones.append(perceptions[Param.OBJETO_DERECHA])
        self._percepciones.append(perceptions[Param.OBJETO_IZQUIERDA])

        if(self.DEBUG):
            print("Objeto arriba: " + str(self._percepciones[Param.OBJETO_ARRIBA]))
            print("Objeto abajo: " + str(self._percepciones[Param.OBJETO_ABAJO]))
            print("Objeto derecha: " + str(self._percepciones[Param.OBJETO_ABAJO]))
            print("Objeto izquierda: " + str(self._percepciones[Param.OBJETO_IZQUIERDA]))

        # Distancia con objeto
        self._percepciones.append(perceptions[Param.DIST_OBJETO_ARRIBA])
        self._percepciones.append(perceptions[Param.DIST_OBJETO_ABAJO])
        self._percepciones.append(perceptions[Param.DIST_OBJETO_DERECHA])
        self._percepciones.append(perceptions[Param.DIST_OBJETO_IZQUIERDA])

        if(self.DEBUG):
            print("Distancia arriba: " + str(self._percepciones[Param.DIST_OBJETO_ARRIBA]))
            print("Distancia abajo: " + str(self._percepciones[Param.DIST_OBJETO_ABAJO]))
            print("Distancia derecha: " + str(self._percepciones[Param.DIST_OBJETO_DERECHA]))
            print("Distancia izquierda: " + str(self._percepciones[Param.DIST_OBJETO_IZQUIERDA]))

        # Posicion jugador
        self._percepciones.append(perceptions[Param.PLAYER_X])
        self._percepciones.append(perceptions[Param.PLAYER_Y])

        if(self.DEBUG):
            print("Posicion jugador: (" + str(self._percepciones[Param.PLAYER_X]) + " - " + str(self._percepciones[Param.PLAYER_Y]) + ")")

        # Posicion antena
        self._percepciones.append(perceptions[Param.COMMAND_X])
        self._percepciones.append(perceptions[Param.COMMAND_Y])

        if(self.DEBUG):
            print("Posicion Comando: (" + str(self._percepciones[Param.COMMAND_X]) + " - " + str(self._percepciones[Param.COMMAND_Y]) + ")")

        # Posicion agente
        self._percepciones.append(perceptions[Param.AGENT_X])
        self._percepciones.append(perceptions[Param.AGENT_Y])

        if(self.DEBUG):
            print("Posicion agente: (" + str(self._percepciones[Param.AGENT_X]) + " - " + str(self._percepciones[Param.AGENT_Y]) + ")")

        # Puede volver a disparar y cantidad de vida
        self._percepciones.append(perceptions[Param.CAN_SHOOT])
        self._percepciones.append(perceptions[Param.VIDA])

        if(self.DEBUG):
            print("Puede disparar: " + str(self._percepciones[Param.CAN_SHOOT]))
            print("Vida: " + str(self._percepciones[Param.VIDA]))
            print("--FIN--\n")

        # Parametros de la partida
        self._gameover = gameover
        self._destroyed = destroyed

    def reaccionar(self):

        # Detecciones por lado
        codeArriba = None
        codeAbajo = None
        codeDerecha = None
        codeIzquierda = None

        # Detectar distancia y tipo de objeto de arriba
        objetoArriba = self._percepciones[Param.OBJETO_ARRIBA]
        if(objetoArriba == Param.BALA):
            codeArriba = Param.RED
        elif(objetoArriba == Param.PLAYER):
            codeArriba = Param.BLUE
        else:
            codeArriba = Param.GREEN


        # Detectar distancia y tipo de objeto de abajo
        objetoAbajo = self._percepciones[Param.OBJETO_ABAJO]
        if(objetoAbajo == Param.BALA):
            codeAbajo = Param.RED
        elif(objetoAbajo == Param.PLAYER):
            codeAbajo = Param.BLUE
        else:
            codeAbajo = Param.GREEN

        # Detectar distancia y tipo de objeto de derecha
        objetoDerecha = self._percepciones[Param.OBJETO_DERECHA]
        if(objetoDerecha == Param.BALA):
            codeDerecha = Param.RED
        elif(objetoDerecha == Param.PLAYER):
            codeDerecha = Param.BLUE
        else:
            codeDerecha = Param.GREEN

        # Detectar distancia y tipo de objeto de izquierda
        objetoIzquierda = self._percepciones[Param.OBJETO_IZQUIERDA]
        if(objetoIzquierda == Param.BALA):
            codeIzquierda = Param.RED
        elif(objetoIzquierda == Param.PLAYER):
            codeIzquierda = Param.BLUE
        else:
            codeIzquierda = Param.GREEN


        # Siguiente estado
        if(codeArriba == Param.RED or 
           codeAbajo == Param.RED or 
           codeDerecha == Param.RED or 
           codeIzquierda == Param.RED):
            self.state = Explorar()

        elif(codeArriba == Param.BLUE or 
           codeAbajo == Param.BLUE or 
           codeDerecha == Param.BLUE or 
           codeIzquierda == Param.BLUE):
            self.state = Explorar()
           
        else:
           self.state = Explorar()

        direction, fire = self.state.execute(self._percepciones)

        self._percepciones.clear()
        return direction, fire