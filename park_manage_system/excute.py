'''
车主从进入到离开停车场的过程
'''

import park,owners,indent,stall,car,parking_record

owners.owner1.in_park(park.park1)
owners.owner1.parking(stall.stall1)
owners.owner1.leave_stall()
owners.owner1.leave_park()
record = parking_record.Record()
print(record.produce_recard())
indent.indent1.print_info()

