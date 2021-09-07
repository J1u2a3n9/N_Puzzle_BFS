class Estado:
    def __init__(self,estado,padre,movimiento):
        self.estado=estado
        self.padre=padre
        self.movimiento=movimiento
        if self.estado:
            self.map=''.join(str(estado) for estado in self.estado)
    
    def __eq__(self,estado_objetivo):
        return self.map == estado_objetivo.map
    
    def __lt__(self,estado_objetivo):
        return self.map<estado_objetivo.map
