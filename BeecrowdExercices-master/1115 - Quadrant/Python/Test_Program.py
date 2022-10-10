from ast import Str
from pyclbr import Class
from re import S
from Menu import Menu
from Coordinate import Coordinate


def test_should_get_user_coordinate():
    # Arrange / Setup
    
    
    # Act / Action
    try:
        Menu.get_user_coordinate(Menu)
    except:
        a = False


    # Assert
    assert a == False
    
   