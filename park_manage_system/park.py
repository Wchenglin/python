'''
定义了停车场的属性以及操作
'''

import datetime

class Park():
    #定义停车场属性，依次为停车场名称、开放时间、出口、入口、停车场类型、空闲停车位数量
    def __init__(self,park_name,park_way_out,park_entrance,park_type,free_parking):
        self.park_name = park_name
        self.opening_hours = None
        self.park_way_out = park_way_out
        self.park_entrance = park_entrance
        self.park_type = park_type
        self.free_parking = free_parking

park1 = Park('美行停车场','出口：东门','入口：西门','地下停车场',100)


        
        



