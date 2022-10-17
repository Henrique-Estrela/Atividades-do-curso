from destino import Destino
from interfaceUsario import interfaceUsuario
from destinoRepositorio import destino_Repositorio

menu = destino_Repositorio()

menu.adicionarDestino(Destino(71, "Salvador"))
menu.adicionarDestino(Destino(75, "Feira"))
menu.adicionarDestino(Destino(68, "Acre"))


user_interface = interfaceUsuario(menu)

while user_interface.saida_usuario():
    pass