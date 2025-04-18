

#Algoritmo A* genérico que resuelve cualquier problema descrito usando la plantilla de la
#la calse Problem que tenga como nodos hijos de la clase Node
class AStar:

    def __init__(self, problem):
        self.open = [] # lista de abiertos o frontera de exploración
        self.precessed = set() # set, conjunto de cerrados (más eficiente que una lista)
        self.problem = problem #problema a resolver

    def GetPlan(self):
        findGoal = False
        #TODO implementar el algoritmo A*
        #cosas a tener en cuenta:
        #Si el número de sucesores es 0 es que el algoritmo no ha encontrado una solución, devolvemos el path vacio []
        #Hay que invertir el path para darlo en el orden correcto al devolverlo (path[::-1])
        #GetSucesorInOpen(sucesor) nos devolverá None si no lo encuentra, si lo encuentra
        #es que ese sucesor ya está en la frontera de exploración, DEBEMOS MIRAR SI EL NUEVO COSTE ES MENOR QUE EL QUE TENIA ALMACENADO
        #SI esto es asi, hay que cambiarle el padre y setearle el nuevo coste.
        self.open.clear()
        self.precessed.clear()
        self.open.append(self.problem.Initial())
        path = []
        #mientras no encontremos la meta y haya elementos en open....
        #TODO implementar el bucle de búsqueda del algoritmo A*
        camino = False
        sucesor = []
        x = 
        while camino == False or self.open.count != 0:
            #Elegir node mas prometedor 

            #Mirar node sucesores de el node mas prometedor
            sucesor = self.problem.GetSucessors(self.open[x])

            #mientras pueda generar camino el node que estoy mirando (tenga sucesores)
            while sucesor.count != 0:
                

                #miro si tenia un camino ya hecho
                cuyuntura = self.GetSucesorInOpen()

                #si tenia un camino ya hecho:: miro si era mejor y lo cambio
                if cuyuntura != None:
                    if cuyuntura.F < self.open[x].F :
                        self._ConfigureNode(self.open[x], cuyuntura.GetParent, cuyuntura.G)
                
                #miro si a llegado a la meta
                if self.open[x].H == 0:
                    camino = True

                #quito el nodo de la lista de sucesor

            #Meto el node que he mirado en precessed

            #quito el nodo que he mirado de la lista 


        #invertir phat
        path = self.ReconstructPath(path)#!!!
        return path

    #nos permite configurar un nodo (node) con el padre y la nueva G
    def _ConfigureNode(self, node, parent, newG):
        node.SetParent(parent)
        node.SetG(newG)
        #TODO Setearle la heuristica que está implementada en el problema. (si ya la tenía será la misma pero por si reutilizais este método para otras cosas)

    #nos dice si un sucesor está en abierta. Si esta es que ya ha sido expandido y tendrá un coste, comprobar que le nuevo camino no es más eficiente
    #En caso de serlos, _ConfigureNode para setearle el nuevo padre y el nuevo G, asi como su heurística
    def GetSucesorInOpen(self,sucesor):
        i = 0
        found = None
        while found == None and i < len(self.open):
            node = self.open[i]
            i += 1
            if node == sucesor:
                found = node

        return found


   # ------------------------------------------- Our Auxiliary Funtion ------------------------------------------- #

    #reconstruye el path desde la meta encontrada.
    def ReconstructPath(self, goal):
        
        path = []
        numNodes = j = goal.lenght
        for i in range(0, numNodes):
            path.append(goal[j])
            j = j - 1

        return path

    # ------------------------------------------- Our Auxiliary Funtion ------------------------------------------- #



