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
        "Rosy": [8, 15, "Platinum"],
        "Ana":  [7, 8, "Gold"],
        "Agus": [5, 8, "Silver"]
    }
    