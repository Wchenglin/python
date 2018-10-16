'''
汽车
'''


class Car():
    def __init__(self,license_number,license_color,car_brand,car_color):
    #定义了汽车属性：车牌号、车牌颜色、汽车型号、汽车颜色
        self.license_plate_number = license_number
        self.license_plate_color = license_color
        self.car_brand = car_brand
        self.car_color = car_color

car1 = Car('辽A88888','蓝色','奔驰','银白色')
car2 = Car('辽A66666','蓝色','宝马','黑色')