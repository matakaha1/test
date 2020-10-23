# 2020/10/23
# 摂氏から華氏へ変換

celsius = [10, 35, 21, 43]
fahrenheit = [round(temperture * 1.8, 1) + 32 for temperture in celsius]

print(fahrenheit)
