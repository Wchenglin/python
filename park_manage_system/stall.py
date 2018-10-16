'''
    定义了停车位的属性及操作
'''
import park

class Stall():
    def __init__(self,parking_lot,stall_number,stall_type,stall_price):
    #定义了停车位属性：所属停车场、编号、类型、停车价格
        self.parking_lot = parking_lot
        self.stall_number = stall_number
        self.stall_type = stall_type
        self.stall_price = stall_price

stall1 = Stall(park.park1,1501,'VIP',50)
stall2 = Stall(park.park1,1502,'普通',5)

    
