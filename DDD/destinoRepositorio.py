from destino import Destino

class destino_Repositorio:
    listaDestino: Destino = []
    
    def __init__(self) -> None:
        pass
    
    def adicionarDestino(self, destino: Destino) -> None:
        self.listaDestino.append(destino)
    
    
    def checarDestino(self, entrada: Destino) -> bool:
        for item in self.listaDestino:
            if (entrada.ddd == item.ddd):
                return True

            return False
    def check_if_itens_exists(self, order: Order) -> bool:
        for item in self.menu_itens:
            if (order.code == item.code):
                return True 

        return False
    
    def obterPeloDDD(self, entrada: Destino):
        for item in self.listaDestino:
            if (entrada.ddd == item.ddd):
                return item.destino

