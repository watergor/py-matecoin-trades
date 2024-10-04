import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        trades = json.load(json_file)
    profit = {"earned_money": 0, "matecoin_account": 0}
    for trade in trades:

        profit["earned_money"] += (
            Decimal(trade["sold"] or "0") - Decimal(trade["bought"] or "0")
        ) * Decimal(trade["matecoin_price"])
        
        profit["matecoin_account"] += Decimal(
            trade["bought"] or "0"
        ) - Decimal(trade["sold"] or "0")

    #print(profit["earned_money"], profit["matecoin_account"])

    with open("profit.json", "w") as file:
        json.dump(profit, file)


#calculate_profit("app/trades.json")
