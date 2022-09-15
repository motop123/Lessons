import abc

class Vecicle(abc.ABC):


    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def drive(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

class Car(Vecicle):

    def start(self):
        print('Start')

c1 = Car()
c1.start()
