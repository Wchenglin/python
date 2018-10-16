'''
停车记录
'''
import owners
import stall
import park

class Record():
    #定义停车记录的属性：停车记录id、进停车场时间、开始停车时间、停车位编号、离开停车位时间、离开停车场时间
    def __init__(self):
        self.record_id = None
        self.in_park_time = ''
        self.parking_time = ''
        self.record_stall = ''
        self.leave_stall_time = ''
        self.leave_park_time = ''

    #产生停车记录
    def produce_recard(self):
        
        self.record_id = '10000'
        self.in_park_time = owners.owner1.in_time()
        self.parking_time = owners.owner1.parking_time()
        self.record_stall = owners.owner1.parking(stall.stall1)
        self.leave_stall_time = owners.owner1.leave_stall()
        self.leave_park_time = owners.owner1.leave_park()
        return self.record_id,self.in_park_time,self.parking_time,self.record_stall,self.leave_stall_time,self.leave_park_time


    
