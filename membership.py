from tabulate import tabulate

class Membership:
    table_benefit = [
            ["Platinum", "15%", 0.15, "Benefit Gold + Silver + Cashback max. 30%"],
            ["Gold", "10%", 0.1,"Benefit Silver + Voucher Ojek Online"],
            ["Silver", "8%", 0.08,"Voucher Makanan"],
        ]
    
    header_benefit = ["Membership", "Discount Percentage", "Discount", "Another Benefit"]

    table_req = [
            ["Platinum", 8, 15],
            ["Gold", 6, 10],
            ["Silver", 5, 7],
        ]
    header_req = ["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]

    data_user = {
        "rosy": [8, 15, "Platinum"],
        "ana":  [7, 8, "Gold"],
        "agus": [5, 8, "Silver"]
    }

    def __init__(self):
        self.username = None
        self.monthly_expense = None
        self.monthly_income = None
        self.membership =None

    def login(self, username):
        username = str(username).lower()
        if username in self.data_user:
            self.username = username
            self.monthly_expense = self.data_user[username][0]
            self.monthly_income = self.data_user[username][1]
            self.membership = self.data_user[username][2]
        else: 
            self.username = username
            self.monthly_expense = None
            self.monthly_income = None
            self.membership = None


    def registry(self, username, monthly_expense, monthly_income):
        username = str(username).lower()

        if username not in self.data_user:
            # set atribut class
            self.username = username
            self.monthly_expense = monthly_expense
            self.monthly_income = monthly_income
            self.membership = None

            # add new data user
            self.data_user[username] = [self.monthly_expense,  self.monthly_income, 
                                        self.membership]
        else:
            print("anda sudah terdaftar")

