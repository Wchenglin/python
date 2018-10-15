'''
执行停车场的相关操作
'''

from park import Park

excute_park = Park()
#汽车进入停车场
Park().user_park()
#汽车停到停车位上
excute_park.start_time()
#汽车离开停车位
excute_park.end_time
#计算停车费用，在停车场出口收取停车费用
excute_park.parking_fee()