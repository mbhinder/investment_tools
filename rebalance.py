import pprint
import tabulate
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", help="Vanguard transaction file",
                    dest="input_file", required=True)
parser.add_argument("-m", help="Money to invest",
                    dest="money_to_invest", required=True)
args = parser.parse_args()

money_to_invest = float(args.money_to_invest)
account_splits = {
    'bonds': 0,
    'domestic_stocks': 0,
    'international_stocks': 0,
    'total': 0
}
expected_splits = {
    'bonds': 0,
    'domestic_stocks': 0,
    'international_stocks': 0,
    'total': 0
}
with open(args.input_file, "r") as input_file:
    for account in input_file:
        account_type, balance = account.split(',')[1], float(account.split(',')[4])
        if 'Total Stock Market' in account_type:
            account_splits['domestic_stocks'] += balance
        elif 'Total International Stock' in account_type:
            account_splits['international_stocks'] += balance
        elif 'Total Bond Market' in account_type:
            account_splits['bonds'] += balance
        account_splits['total'] += balance
expected_splits['total'] = account_splits['total'] + money_to_invest
expected_splits['bonds'] = 0.10 * expected_splits['total']
expected_splits['domestic_stocks'] = 0.70*0.90 * expected_splits['total']
expected_splits['international_stocks'] = 0.30*0.90* expected_splits['total']
table = [["Category", "Actual", "Expected", "Delta"]]
for cat in account_splits.keys():
    table.append([cat, account_splits[cat], expected_splits[cat],
                 expected_splits[cat] - account_splits[cat]])
print tabulate.tabulate(table)
