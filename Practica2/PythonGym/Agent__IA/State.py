import math
import random
from Agent__IA.Parameters import Param

class State:

    def __init__(self):
        self._ultimaDireccion = Param.QUIETO
        return

    def ejecutar_explorar(self, perceptions):

        rand = random.randint(0, 200)

        if(rand < 5):
            self._ultimaDireccion = Param.MOVER_DERECHA
            return Param.MOVER_DERECHA, Param.NO_DISPARA
        elif(rand < 10):
            self._ultimaDireccion = Param.MOVER_IZQUIERDA
            return Param.MOVER_IZQUIERDA, Param.NO_DISPARA
        elif(rand < 15):
            self._ultimaDireccion = Param.MOVER_ARRIBA
            return Param.MOVER_ARRIBA, Param.NO_DISPARA
        elif(rand < 20):
            self._ultimaDireccion = Param.MOVER_ABAJO
            return Param.MOVER_ABAJO, Param.NO_DISPARA

        # Objetos y distancias
        objetos = [
                   perceptions[Param.OBJETO_ARRIBA], 
                   perceptions[Param.OBJETO_ABAJO], 
                   perceptions[Param.OBJETO_DERECHA], 
                   perceptions[Param.OBJETO_IZQUIERDA]
                  ]
        distancias = [
                      perceptions[Param.DIST_OBJETO_ARRIBA], 
                      perceptions[Param.DIST_OBJETO_ABAJO], 
                      perceptions[Param.DIST_OBJETO_DERECHA], 
                      perceptions[Param.DIST_OBJETO_IZQUIERDA]
                     ]

        # Si estamos pegados a un muro irrompible, no intentamos ir en esa direccion
        arribaLibre = False if (objetos[0] == Param.MURO_IRROMPIBLE and distancias[0] < 0.5) else True
        abajoLibre = False if (objetos[1] == Param.MURO_IRROMPIBLE and distancias[1] < 0.5) else True
        derechaLibre = False if (objetos[2] == Param.MURO_IRROMPIBLE and distancias[2] < 0.5) else True
        izquierdaLibre = False if (objetos[3] == Param.MURO_IRROMPIBLE and distancias[3] < 0.5) else True

        offset = 0.5
        pos_x = perceptions[Param.AGENT_X]
        pos_y = perceptions[Param.AGENT_Y]
        command_x = perceptions[Param.COMMAND_X]
        command_y = perceptions[Param.COMMAND_Y]
        minimaDistancia = 1000
        siguienteDireccion = 0

        # Ver a que lado nos acercamos mas a la base y vamos en esa direccion -> Distancia entr dos puntos
        if(arribaLibre):
            dist_arriba = self.calcularDistanciaEntrePuntos(pos_x, pos_y + offset, command_x, command_y)
            if(dist_arriba < minimaDistancia):
                minimaDistancia = dist_arriba
                siguienteDireccion = Param.MOVER_ARRIBA


        if(abajoLibre):
            dist_abajo = self.calcularDistanciaEntrePuntos(pos_x, pos_y - offset, command_x, command_y)
            if(dist_abajo < minimaDistancia):
                minimaDistancia = dist_abajo
                siguienteDireccion = Param.MOVER_ABAJO

        if(derechaLibre):
            dist_derecha = self.calcularDistanciaEntrePuntos(pos_x + offset, pos_y, command_x, command_y)
            if(dist_derecha < minimaDistancia):
                minimaDistancia = dist_derecha
                siguienteDireccion = Param.MOVER_DERECHA

        if(izquierdaLibre):
            dist_izquierda = self.calcularDistanciaEntrePuntos(pos_x - offset, pos_y, command_x, command_y)
            if(dist_izquierda < minimaDistancia):
                minimaDistancia = dist_izquierda
                siguienteDireccion = Param.MOVER_IZQUIERDA

        # Ver si hay que disparar
        disparar = Param.NO_DISPARA
        if(siguienteDireccion == Param.MOVER_ARRIBA and (objetos[Param.OBJETO_ARRIBA] == Param.MURO  and distancias[0] < 1.2563) or objetos[Param.OBJETO_ARRIBA] == Param.CENTRO_COMANDO):
            disparar = Param.DISPARA
        elif(siguienteDireccion == Param.MOVER_ABAJO and (objetos[Param.OBJETO_ABAJO] == Param.MURO and distancias[1] < 1.2563) or objetos[Param.OBJETO_ABAJO] == Param.CENTRO_COMANDO):
            disparar = Param.DISPARA
        elif(siguienteDireccion == Param.MOVER_DERECHA and (objetos[Param.OBJETO_DERECHA] == Param.MURO and distancias[2] < 1.2563) or objetos[Param.OBJETO_DERECHA] == Param.CENTRO_COMANDO):
            disparar = Param.DISPARA
        elif(siguienteDireccion == Param.MOVER_IZQUIERDA and (objetos[Param.OBJETO_IZQUIERDA] == Param.MURO and distancias[3] < 1.2563) or objetos[Param.OBJETO_IZQUIERDA] == Param.CENTRO_COMANDO):
            disparar = Param.DISPARA

        if(abs(pos_x - command_x) < 1 and abs(pos_y - command_y) < 1):
            disparar = Param.DISPARA


        self._ultimaDireccion = siguienteDireccion
        return siguienteDireccion, disparar
    

    def ejecutar_alerta(self, perceptions, direccionBlue):

        siguienteDireccion = Param.QUIETO
        #Enfoca
        if(direccionBlue != self._ultimaDireccion):
            siguienteDireccion = direccionBlue

        #dispara


        self._ultimaDireccion = siguienteDireccion
        return 0, 0

    def ejecutar_atacar(self, perceptions, direccionRed):
        
        #Mirar si puede disparar

        #Estado Disparar

        #Estado alejarse


        return 0, 0

    def calcularDistanciaEntrePuntos(self, pos1_x, pos1_y, pos2_x, pos2_y) -> float:

        distanciaX = abs(pos1_x - pos2_x)
        distanciaY = abs(pos1_y - pos2_y)
        return math.sqrt( (distanciaX ** 2) + (distanciaY ** 2) )