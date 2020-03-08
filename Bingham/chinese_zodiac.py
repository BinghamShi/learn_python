
# 序列的基本操作操作 --- 字符串

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = 2020
print(chinese_zodiac[year % 12])
print(year % 12)

# 成员关系操作符 ------ in, not int
# 对象 [not] in 序列
print('龙' in chinese_zodiac)

# 连接操作符 ------ +
# 序列 + 序列
print('生肖: ' + chinese_zodiac + '。')

# 重复操作符 ------ *
# 序列 * 整数
print(chinese_zodiac * 2)

# 切片操作符 ------ [:]
# 序列[0:整数]
print(chinese_zodiac[0:5])