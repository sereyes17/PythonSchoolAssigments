__author__ = 'Sharayah Reyes'

# This program is the second programing exercise from chapter 14 in which the book asks
# to create a class Car and to make an object from that class. Then, the accelerate and brake methods
# will be called 5 times each and the current speed will print after each call

# Output: my_car.accelerate(), my_car.brake(), my_car.get_year(), my_car.get_make(), my_car.get_speed()


# Class Car
#   Private Integer __year = 0
#   Private String __make = ""
#   Private Integer __speed = 0
#
#   Public Module Car(Integer year, String make, Integer speed)
#       Set __year = year
#       Set __make = make
#       Set __speed = 0
#   End Module
#
#   Public Module set_year(Integer year)
#       Set __year = year
#   End Module
#
#   Public Module set_make(String make)
#       Set __make =  make
#   End Module
#
# Public Module set_speed(Integer speed)
#       Set __speed = 0
#   End Module
#
#   Public Function Integer get_year()
#       Return __year
#   End Function
#
#   Public Function String get_make()
#       Return __make
#   End Function
#
#   Public Function Integer get_speed()
#       Return __speed
#   End Function
#
#   Public Function Integer accelerate()
#       __speed += 5
#       Return __speed
#   End Function
#
#   Public Function Integer brake()
#       __speed -= 5
#       Return __speed
# End Class

class Car:

    __year = 0
    __make = ""
    __speed = 0

    def __init__(self, year, make, speed):
        self.__year = year
        self.__make = make
        self.__speed = 0

    def set_year(self, year):
        self.__year = year

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = 0

    def get_year(self):
        return self.__year

    def get_make(self):
        return self.__make

    def get_speed(self):
        return self.__speed

    def accelerate(self):
        self.__speed += 5
        return self.__speed

    def brake(self):
        self.__speed -= 5
        return self.__speed


#   Module main()
#       Declare counter = 0
#       Declare MAX_VALUE = 5
#       Set my_car = new Car(2012, "Jeep", 0)
#
#       For counter to MAX_VALUE
#           Call my_car.accelerate()
#           Display "Your", my_car.get_year(), my_car.get_make(), "accelerates!"
#           Display "The speed in now:", my_car.get_speed()
#       End For
#
#        For counter to MAX_VALUE
#            Call my_car.brake()
#            Display "Your", my_car.get_year(), my_car.get_make(), "brakes!"
#            Display "The speed in now:", my_car.get_speed()
#        End For
#   End Module

def main():

    counter = 0
    MAX_VALUE = 5
    my_car = Car(2012, "Jeep", 0)

    for counter in range(MAX_VALUE):
            my_car.accelerate()
            print("Your", my_car.get_year(), my_car.get_make(), "accelerates!")
            print("The speed in now:", my_car.get_speed())

    for counter in range(MAX_VALUE):
        my_car.brake()
        print("Your", my_car.get_year(), my_car.get_make(), "brakes!")
        print("The speed in now:", my_car.get_speed())


main()