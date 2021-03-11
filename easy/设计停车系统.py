# coding=utf-8
# coding=utf-8
class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.carType = {1:big, 2:medium, 3:small}


    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.carType[carType] > 0:
            self.carType[carType] -= 1
            return True
        else:
            return False

# Your ParkingSystem object will be instantiated and called as such:
if __name__ == '__main__':
    # 1 2 3 对应大中小
    obj = ParkingSystem(1, 1, 0)
    print obj.addCar(1)
    print obj.addCar(2)
    print obj.addCar(3)
    print obj.addCar(1)