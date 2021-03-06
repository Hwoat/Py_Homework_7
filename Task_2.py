'''
Реализовать проект расчета суммарного расхода ткани на
производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать
формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на
практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике
работу декоратора @property.
'''


class Cloth:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)} м²')


class Coat(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Расход на пальто {self.square_c} м²'


class Suite(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3, 2)

    def __str__(self):
        return f'Расход на костюм {self.square_j} м²'


coat = Coat(2, 4)
suite = Suite(1, 2)
print(coat)
print(suite)
print(coat.get_sq_full)
print(suite.get_sq_full)
print(suite.get_square_c())
print(suite.get_square_j())
