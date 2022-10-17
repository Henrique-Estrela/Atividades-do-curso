from destinoRepositorio import destino_Repositorio
from destino import Destino


class interfaceUsuario:
    def __init__(self, destino_Repositorio) -> None:
        self.destino_Repositorio = destino_Repositorio
    
    def solicitar_input_usuario(self):
        resultado = int(input("Digite o DDD q voce quer saber:\n--->"))
        return resultado
    
    def exibir_destinos(self, ddd: Destino):
        return destino_Repositorio.obterPeloDDD(ddd)
        
    
    def saida_usuario(self):
        entrada = self.solicitar_input_usuario()

        checar_destino = destino_Repositorio.checarDestino(self ,entrada)
        if (checar_destino == False):
            return "DDD invalido"
        
        return self.exibir_destinos(entrada)
        