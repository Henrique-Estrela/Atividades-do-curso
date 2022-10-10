from Coordinate import Coordinate
from Quadrant import Quadrant


def test_should_get_quadrant_coordinate():
    # Arrange / Setup
    # 1
    a = 10
    b = 20
    # 2
    c = -10
    d = 20
    # 3
    e = -10
    f = -20
    # 4
    g = 10
    h = -20
    # 5
    i = 0
    j = 20

    coordinates1 = Coordinate(a, b)
    quadrant1 = Quadrant(coordinates1)

    coordinates2 = Coordinate(c, d)
    quadrant2 = Quadrant(coordinates2)

    coordinates3 = Coordinate(e, f)
    quadrant3 = Quadrant(coordinates3)

    coordinates4 = Coordinate(g, h)
    quadrant4 = Quadrant(coordinates4)

    coordinates5 = Coordinate(i, j)
    quadrant5 = Quadrant(coordinates5)

    # Act / Action
    result1 = quadrant1.get_quadrant_coordinate()
    result2 = quadrant2.get_quadrant_coordinate() 
    result3 = quadrant3.get_quadrant_coordinate()
    result4 = quadrant4.get_quadrant_coordinate()
    result5 = quadrant5.get_quadrant_coordinate()

    # Assert
    assert result1 == "First"
    assert result2 == "Second"
    assert result3 == "Third"
    assert result4 == "Fourth"
    assert result5 == ""
