from Agent__IA.State import State
from Agent__IA.Parameters import Param
import math
import random

class Explorar(State):

    def __init__(self):
        return
    
    def execute(self, perceptions):

        if(random.randint(0, 100) < 5):
            return Param.MOVER_DERECHA, Param.DISPARA

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
    

        return siguienteDireccion, Param.DISPARA
    

    def calcularDistanciaEntrePuntos(self, pos1_x, pos1_y, pos2_x, pos2_y) -> float:

        distanciaX = abs(pos1_x - pos2_x)
        distanciaY = abs(pos1_y - pos2_y)
        return math.sqrt( (distanciaX ** 2) + (distanciaY ** 2) )