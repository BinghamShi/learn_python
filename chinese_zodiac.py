# 记录生肖，根据年份来判断生肖
# python序列的概念，类似于java的数组，但是感觉比java数组更强大
#序列字符串的基本操作
#1.成员关系操作符（in，not in）   对象【not】 in 序列
#2.连接操作符（+） 序列 + 序列
#3.重复操作符（*）序列 * 整数
#4.切片操作符([:]) 序列[0:整数]


chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊猴鸡狗猪' 

print(chinese_zodiac[0:4])

print(chinese_zodiac[-1])

year = 2020

print(year % 12)

print(chinese_zodiac[year % 12])

print('鼠' in chinese_zodiac)

print(chinese_zodiac + "连接")

print(chinese_zodiac * 3)

print(chinese_zodiac[1:2])


