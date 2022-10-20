from Destino import Destino
from DestinoRepository import DestinoRepository
from interfaceUser import InterfaceUser

Destino_Repository = DestinoRepository()

Destino_Repository.adicioanar_destino(Destino(71, "Salvador"))
Destino_Repository.adicioanar_destino(Destino(68,"Acre"))


print(Destino_Repository)

user_interface = InterfaceUser(Destino_Repository)

while True:
    retorno = user_interface.saida_usuario()
    if retorno == 'DDD invalido!':
        break

    print(retorno)
