'''
    定义了车主的属性及操作
'''
import park
import stall
import car
import datetime
import random

class Owner():
    #定义车主属性，依次为：车主姓名、性别、联系电话、拥有汽车
    def __init__(self,owner_name,owner_sex,owner_tel,owner_cars):
        self.owner_name = owner_name
        self.owner_sex = owner_sex
        self.owner_tel = owner_tel
        self.owner_cars = owner_cars

    def in_park(self,park_model):
        if  park_model.free_parking > 0:
            print('剩余空闲停车位：' + str(park_model.free_parking) )
        else:
            print('剩余空闲停车位：0')
        pass

    #进入停车场时间
    def  in_time(self):
        self.time = datetime.datetime.now().strftime('%Y-%m-%d-%T')
        return self.time

    #返回停车位编号
    def parking(self,stall_model):        
        return stall_model.stall_number 

    #返回开始停车时间    
    def parking_time(self):
        self.time_start = datetime.datetime.now().strftime('%Y-%m-%d-%T') 
        return self.time_start

    #返回离开停车位时间
    def leave_stall(self):
        self.time_leave = datetime.datetime.now().strftime('%Y-%m-%d-%T')
        return self.time_leave

    #返回离开停车场时间
    def leave_park(self):
        self.time_out = datetime.datetime.now().strftime('%Y-%m-%d-%T')
        return self.time_out

owner1 = Owner('李雷','男','17899999999',car.car1)