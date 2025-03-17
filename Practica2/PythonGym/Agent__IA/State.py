import math
import random
from Agent__IA.Parameters import Param

class State:

    MAX_CICLOS_ATASCADO = 2
    MAX_DIST_PARA_DISPARAR = 4

    def __init__(self):
        self._ultimaDireccion = Param.QUIETO
        self._ultimasCoordenadas = []
        self._limiteCiclosAtascado = State.MAX_CICLOS_ATASCADO
        return

    def ejecutar_explorar(self, perceptions):

        randomNum = random.randint(0, 100)

        current_x = perceptions[Param.AGENT_X]
        current_y = perceptions[Param.AGENT_Y]

        # Guardar la posicion por primera vez
        if(len(self._ultimasCoordenadas) == 0):
            self._ultimasCoordenadas.append(current_x)
            self._ultimasCoordenadas.append(current_y)
        else:

            # Si no nos movemos -> Decrementamos contador
            if(current_x == self._ultimasCoordenadas[0] and current_y == self._ultimasCoordenadas[1]):
                self._limiteCiclosAtascado -= 1

            # Si llegamos al limite de ciclos atascados -> Movimiento aleatorio
            if(self._limiteCiclosAtascado == 0):
                self._limiteCiclosAtascado = State.MAX_CICLOS_ATASCADO
                direccion, fire = self.moverAleatoriamente(randomNum)
                self._ultimaDireccion =  direccion
                return direccion, fire
            
            else:
                self._ultimasCoordenadas.pop()
                self._ultimasCoordenadas.pop()
                self._ultimasCoordenadas.append(current_x)
                self._ultimasCoordenadas.append(current_y)
        

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

        distanciaBlue = 0.0
        siguienteDireccion = Param.QUIETO
        debeDisparar = Param.NO_DISPARA

        # Calcular distancia con el objetivo
        if(direccionBlue == Param.MOVER_ARRIBA):
            distanciaBlue = perceptions[Param.DIST_OBJETO_ARRIBA]
        elif(direccionBlue == Param.MOVER_ABAJO):
            distanciaBlue = perceptions[Param.DIST_OBJETO_ABAJO]
        elif(direccionBlue == Param.MOVER_DERECHA):
            distanciaBlue = perceptions[Param.DIST_OBJETO_DERECHA]
        else:
            distanciaBlue = perceptions[Param.DIST_OBJETO_IZQUIERDA]

        # Enfocar a la direccion 'direccionBlue' si no lo estamos ya
        if(direccionBlue != self._ultimaDireccion):
            siguienteDireccion = direccionBlue
        self._ultimaDireccion = siguienteDireccion

        # Disparar si estamos a cierta distancia
        # Si no, ignorar
        if(distanciaBlue <= State.MAX_DIST_PARA_DISPARAR):
            debeDisparar = Param.DISPARA

        return siguienteDireccion, debeDisparar

    def ejecutar_atacar(self, perceptions, direccionRed):
        
        siguienteDireccion = Param.QUIETO
        disparar = Param.NO_DISPARA
        puedoDisparar = perceptions[Param.CAN_SHOOT]

        # Calcular distancia con el objetivo
        if(direccionRed == Param.MOVER_ARRIBA):
            direccionRed = perceptions[Param.DIST_OBJETO_ARRIBA]
        elif(direccionRed == Param.MOVER_ABAJO):
            direccionRed = perceptions[Param.DIST_OBJETO_ABAJO]
        elif(direccionRed == Param.MOVER_DERECHA):
            direccionRed = perceptions[Param.DIST_OBJETO_DERECHA]
        else:
            direccionRed = perceptions[Param.DIST_OBJETO_IZQUIERDA]

        # Mirar si puede disparar
        if(puedoDisparar):
            disparar = Param.DISPARA

        # Estado Disparar


        # Estado alejarse


        self._ultimaDireccion = siguienteDireccion

        return siguienteDireccion, disparar


## ------------------------- METODOS AUXILIARES ------------------------- ##
    def calcularDistanciaEntrePuntos(self, pos1_x, pos1_y, pos2_x, pos2_y) -> float:

        distanciaX = abs(pos1_x - pos2_x)
        distanciaY = abs(pos1_y - pos2_y)
        return math.sqrt( (distanciaX ** 2) + (distanciaY ** 2) )
    
    def moverAleatoriamente(self, probabilidad):

        print("MOVIMIENTO ALEATORIO")
        if(probabilidad < 25):
            self._ultimaDireccion = Param.MOVER_DERECHA
            return Param.MOVER_DERECHA, Param.NO_DISPARA
        elif(probabilidad < 50):
            self._ultimaDireccion = Param.MOVER_IZQUIERDA
            return Param.MOVER_IZQUIERDA, Param.NO_DISPARA
        elif(probabilidad < 75):
            self._ultimaDireccion = Param.MOVER_ARRIBA
            return Param.MOVER_ARRIBA, Param.NO_DISPARA
        else:
            self._ultimaDireccion = Param.MOVER_ABAJO
            return Param.MOVER_ABAJO, Param.NO_DISPARA