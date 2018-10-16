'''
订单
'''
import owners

class Indent():
    def __init__(self):
        #定义一个订单，属性依次为：订单编号、交易金额、订单生成时间、支付方式、支付状态、支付人、停车记录id
        self.indent_number = '122500'
        self.indent_money = '500'
        self.indent_time = owners.owner1.leave_park()
        self.pay_type = '支付宝'
        self.pay_status = '未支付'
        self.pay_humen = '李雷'
    def print_info(self):
        print(self.indent_number,self.indent_money,self.indent_time,self.pay_type,self.pay_status,self.pay_humen)
indent1 = Indent()

