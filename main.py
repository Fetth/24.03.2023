class Transport():
    def __init__(self, speed, oil):
        self._speed = speed
        self._oil = oil
    
    def setSpeed(self):
        self._speed = input("Введите скорость ")

    def setOil(self):
        self._oil = input("Введите топливо ")
    
    def getSpeed(self):
        return self.speed 
    
    def getOil(self):
        return self.oil

    speed = property(getSpeed, setSpeed)
    oil = property(getOil, setOil)
    def out(self):
        print(self._speed , self._oil)

auto = Transport(" ", " ")
auto.setSpeed()
auto.setOil()
auto.out()


class LandTr(Transport):

    def __init__(self, speed, oil, model):
         super().__init__(speed, oil)
         self._model = model

    def getModel(self):
        return self._model 
    
    def setModel(self):
        self._model = input("Введите модель ")
    
    auto1 = property(getModel, setModel)
    def out(self):
        print(self._speed , self._oil, self._model)

auto = LandTr(" ", " ", " ")
auto.setSpeed()
auto.setOil()
auto.setModel()
auto.out()



class Auto(LandTr):
    def __init__(self, speed, oil, model, color):
        super().__init__(speed, oil, model)
        self.__color = color

    def getColor(self):
        return self.__color 
    
    def setColor(self):
        self.__color = input("Введите цвет ")
    
    auto2 = property(getColor, setColor)
    def out3(self):
        print(self._speed , self._oil, self._model, self.__color)

auto = Auto(" ", " ", " ", " ")
auto.setSpeed()
auto.setOil()
auto.setModel()
auto.setColor()
auto.out()



class Air(Transport):
    
    def __init__(self, speed, oil, mark):
        super().__init__(speed, oil)
        self._mark = mark
    
    def getMark(self):
        return self._mark

    def setMark(self):
        self._mark = input("Введите марку самолета ")

    auto3 = property(getMark, setMark)
    def out(self):
        print(self._speed , self._oil, self._mark)

auto = Air(" ", " ", " ")
auto.setSpeed()
auto.setOil()
auto.setMark()
auto.out()

class Airplane(Air):
    def __init__(self, speed, oil, mark, pas):
        super().__init__(speed, oil, mark)
        self.__pas = pas

    def getPas(self):
        return self.__pas
    
    def setPas(self):
        self.__pas = input("Сколько там помещается пассажиров ")
    
    auto4 = property(getPas, setPas)
    def out(self):
        print(self._speed , self._oil, self._mark, self.__pas)
auto = Airplane(" ", " ", " ", " ")
auto.setSpeed()
auto.setOil()
auto.setMark()
auto.setPas()
auto.out()






# class Water(Transport):

#     def __init__(self, speed, oil, tonage):
#         super().__init__(speed, oil, tonage)
#         self._tonage = tonage
    
#     def getTonage(self):
#         return self._tonage

#     def setTonage(self, tonage):
#         self._tonage = tonage

#     auto5 = property(getTonage, setTonage)

#     def out(self):
#         print(self.speed, self.oil, self._tonage)



# class ship(Water):
#     def __init__(self, speed, oil, tonage, type):
#         super().__init__(speed, oil, tonage, type)
#         self.__type = type

#     def getType(self):
#         return self.__type
    
#     def setType(self, type):
#         self.__type = type

#     auto6 = property(getType, setType)
#     def out(self):
#         print(self.speed , self.oil, self._tonage , self.__type)
