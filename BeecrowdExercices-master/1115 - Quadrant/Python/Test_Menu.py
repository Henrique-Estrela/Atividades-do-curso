from Coordinate import Coordinate
from Menu import Menu
from Coordinate import Coordinate


def test_should_cordinate_is_valid():
    # Arrange / Setup
    # 1
    
    coordinates = Coordinate(10,20)

    # Act / Action
    coordinates1 = Menu.cordinate_is_valid(Menu, coordinates)


    # Assert
    assert coordinates1 == True

   
 
