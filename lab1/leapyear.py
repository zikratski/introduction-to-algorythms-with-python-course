# Напишите программу leapyear.py, которая принимает на вход год и говорит високосный он (True)
# или нет (False). Високосность года определяется следующими правилами:
#
#     год, номер которого кратен 400, — високосный
#     остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300)
#     остальные годы, номер которых кратен 4, — високосные


import sys
year = int(sys.argv[1])
flag = (year % 400 == 0) or ((year % 4 == 0) and (year % 100 !=0))
print(flag)
