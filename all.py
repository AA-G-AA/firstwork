import datetime


class Manager:
    def __init__(self):
        self.income_list = []
        self.expense_list = []

    def run(self):
        while True:
            print("\n=================================")
            print("欢迎使用个人账单管理系统")
            print("=================================")
            print("请选择操作：")
            print("1. 记录收入")
            print("2. 记录支出")
            print("3. 查看所有账单")
            print("4. 查询账单")
            print("5. 退出系统")

            choice = input("请输入选项序号：")

            if choice == '1':
                self.record_income()
            elif choice == '2':
                self.record_expense()
            elif choice == '3':
                self.display_all_bills()
            elif choice == '4':
                self.query_bills()
            elif choice == '5':
                print("感谢使用个人账单管理系统，再见！")
                break
            else:
                print("错误：无效的选项，请重新输入。")

            input("按任意键返回主菜单...")

    def record_income(self):
        date = input("日期（YYYY-MM-DD）：")
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("日期格式错误，请重新输入。")
            return
        amount = input("收入金额：")
        try:
            amount = float(amount)
            if amount <= 0:
                print("金额必须大于0，请重新输入。")
                return
        except ValueError:
            print("金额格式错误，请重新输入。")
            return
        description = input("类别（如工资、奖金等）：")
        remark = input("备注：")
        self.income_list.append(bullrecord(date, amount, description, remark))
        print("收入已成功记录！")

    def record_expense(self):
            date = input("日期（YYYY-MM-DD）：")
            try:
                datetime.datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                print("日期格式错误，请重新输入。")
                return
            amount = input("支出金额：")
            try:
                amount = float(amount)
                if amount <= 0:
                    print("金额必须大于0，请重新输入。")
                    return
            except ValueError:
                print("金额格式错误，请重新输入。")
                return
            description = input("类别（如餐饮、交通、购物等）：")
            remark = input("备注：")
            self.expense_list.append(bullrecord(date, amount, description, remark))
            print("支出已成功记录！")

    def display_all_bills(self):
        print("收入记录：")
        for bill in self.income_list:
            print(bill)
        print("支出记录：")
        for bill in self.expense_list:
            print(bill)


    def query_bills(self):
        pass


class bullrecord:
    def __init__(self, date,amount,description,remark):
        self.date = date
        self.amount = amount
        self.description = description
        self.remark = remark

    def __str__(self):
        return f"日期: {self.date}, 金额: {self.amount}, 类别: {self.description}, 备注: {self.remark}"

if __name__ == "__main__":
    manager = Manager()
    manager.run()