'''
某公司,账户余额有1W元,给20名员工发工资。
员工编号从1到20,从编号1开始,依次领取工资,每人可领取1000元
领工资时,财务判断员工的绩效分(1-10)(随机生成),如果低于5,不发工资,换下一位
如果工资发完了,结束发工资。

'''
import random
# 定义公司账户余额变量
company_account_balance = 10000


for i in range(1,21):
    # 定义随机绩效分
    performance = random.randint(1,10)
    # 判断员工绩效分
    if performance < 5:
        print(f"员工{i},绩效分{performance},低于5,不发工资,下一位。")
        # 如果当前员工绩效不满足条件，continue结束当前循环进入下一次循环
        continue
    # 发工资，判断公司账户余额
    if company_account_balance >= 1000:
        # 发放工资，账户扣除
        company_account_balance -= 1000
        print(f"员工{i}绩效分{performance},满足条件发放工资1000元,工资账户余额剩余{company_account_balance}元")
    # 账户余额不足，无法发工资
    else:
        print(f"余额不足,公司账户余额{company_account_balance}元,不足以发工资,下个月再来")
        # 余额不足break结束循环
        break