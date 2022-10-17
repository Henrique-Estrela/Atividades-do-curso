from UserInterface import UserInterface
from MenuRepository import MenuRepository
from Order import Order



def test_get_user_input():
   
    result = "1 3".split()
    order = Order(int(result[0]), int(result[1]))
    

    assert isinstance(order, object) == True  

def test_get_total_price():
    item = (1, "Hot dog", 4.00)

    menu = MenuRepository()
    menu.get_total_price(Order)
    order = Order(1, 2)
    a = ''

    if (order.code == item[0]):
        a = item[2] * order.quantity
    


    assert a == 8.0  