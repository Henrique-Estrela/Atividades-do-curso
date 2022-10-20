from DestinoRepository import DestinoRepository
from Destino import Destino


class InterfaceUser:
    def __init__(self, Destino_Repository:DestinoRepository) -> None:
        self.Destino_Repository = Destino_Repository

    def solicitar_input_usuario(self) -> Destino:
        result = int(input("Informe seu DDD \n>>>> "))
        return result

    def exibir_destinos(self, ddd: int):
        return self.Destino_Repository.obter_destino_pelo_ddd(ddd)

    def saida_usuario(self) -> bool:
        destino = self.solicitar_input_usuario()

        if (self.Destino_Repository.checa_se_destino_existe(destino) == False):
            return "DDD invalido!"

        return self.Destino_Repository.obter_destino_pelo_ddd(destino)
