from Destino import Destino



class DestinoRepository:
    lista_destino: Destino = []

    def __init__(self) -> None:
        pass

    def adicioanar_destino(self, destino: Destino) -> None:
        self.lista_destino.append(destino)

    def checa_se_destino_existe(self, ddd: int) -> bool:
        for item in self.lista_destino:
            if (ddd == item.ddd):
                return True 
            
        return False

    def obter_destino_pelo_ddd(self, ddd: int) :
        for item in self.lista_destino:
            if (ddd == item.ddd):
                return item.destino

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<20} \n"
        menu = formatText.format("ddd", "destino")

        for item in self.lista_destino:
            menu += formatText.format(item.ddd, item.destino)

        return menu
