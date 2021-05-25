from math import ceil, log, pow
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-t', '--type')
parser.add_argument('-a', '--payment', default=0)
parser.add_argument('-p', '--principal', default=0)
parser.add_argument('-n', '--periods', type=int, default=0)
parser.add_argument('-i', '--interest', default=0)

args = parser.parse_args()

t = args.type
a = args.payment
p = args.principal
n = args.periods
i = args.interest
try:
    a, p, i = map(float, [a, p, i])
except ValueError:
    exit('Incorrect parameters')

s = sum(map(lambda x: int(bool(x)), [a, p, n]))

if t not in ['annuity', 'diff'] \
        or t == 'diff' and a \
        or s != 2 \
        or i <= 0 or a < 0 or p < 0 or n < 0:
    print('Incorrect parameters')
    exit()

i = i / 1200

if t == 'annuity':
    if n == 0:  # for number of monthly payments
        n = ceil(log(a / (a - i * p), 1 + i))
        years = n // 12
        months = n % 12
        years = '1 year' if years == 1 else str(years) + ' years' if years else ''
        the_and = ' and ' if years and months else ''
        months = str(months) + ' months' if months else ''
        print(f'It will take {years}{the_and}{months} to repay this loan!')

    if a == 0:  # for annuity monthly payment amount
        a = ceil(p * (i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
        print(f'\nYour monthly payment = {a}!')

    if p == 0:  # for loan principal
        p = round(a / ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1)))
        print(f'\nYour loan principal = {p}!')

    over = ceil(n * a - p)
    print(f'\nOverpayment = {over}!')

if t == 'diff':
    total = 0
    for m in range(1, n + 1):
        a = ceil(p / n + i * (p - (p * (m - 1)) / n))
        total += a
        print(f'\nMonth {m}: payment is {a}')
    print(f'\nOverpayment = {ceil(total - p)}!')
