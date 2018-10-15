'''
定义了停车场的属性以及操作
'''

import datetime

class Park():
    #假设停车场一共有100个停车位
    park_spot = 100

    #输入车牌号，统计停车位剩余情况
    @classmethod
    def user_park(cls):
        print('类方法')
        if cls.park_spot < 0:
           return '无剩余停车位！！！'
        else:
            print('输入车牌号：')
            cls.license_plate_number = input()
            cls.park_spot -= 1
            return(cls.park_spot)
    #停车开始时间
    def start_time(self):
        pass

    #停车结束时间
    def end_time(self):
        pass

    #根据停车时间收取停车费
    def parking_fee(self):
        pass

        



