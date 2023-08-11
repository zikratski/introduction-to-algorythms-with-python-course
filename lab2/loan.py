# #Напишите программу loan.py, которая рассчитывает ежемесячные выплаты по кредиту
# # (аннуитетный порядок погашения). Программа принимает три входных параметра:
#
#     amount -- сумма кредита, например, 1000
#     rate -- годовой процент, например, 0.1 для 10%
#     months -- срок в месяцах, например, 12
#
# На выходе должна получиться таблица вида:

from prettytable import PrettyTable
import sys

amount = float(sys.argv[1])
rate = float(sys.argv[2])
months = int(sys.argv[3])

def loantable(amount, rate, months):
    
    monthrate = rate/12
    payment = amount*(monthrate*(monthrate+1)**months)/((1+monthrate)**months - 1)
    left = amount
    res = [(0,0.00,0.00,0.00,left)]
    for i in range(months):
        interest = left * monthrate
        principal = payment - interest
        balance = left - principal
        left -= principal
        res.append((i+1,round(payment,2),round(principal,2),round(interest,2),abs(round(balance,2))))
    total_payment = round(sum([elem[1] for elem in res]),2)
    total_principal = round(sum([elem[2] for elem in res]),2)
    total_interest = round(sum([elem[3] for elem in res]),2)

    return (res, (total_payment, total_principal,total_interest))


if __name__ == "__main__":
        tb = PrettyTable(["#", "pmt", "principal", "interest", "balance"])
        result = loantable(amount, rate, months)
        for row in result[0]:
            tb.add_row(row)
        print(tb)
        total = PrettyTable(["total", result[1][0], result[1][1], result[1][2]])

        #tb.add_row(["total", result[1][0], result[1][0], result[1][0], ""])

        print(total)
        #print(f" = {result[1][0]}  {result[1][1]}  {result[1][2]}")