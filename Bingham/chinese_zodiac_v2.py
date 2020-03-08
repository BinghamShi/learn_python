# 控制台输入
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = int(input('Please input the year of birth: '))

# print(chinese_zodiac[year % 12])
if chinese_zodiac[year % 12] == '鼠' :
    print("maybe not rat")

# for 语句
# for cz in chinese_zodiac :
#     print(cz)

# for i in range(1,13) :
#     print(i)

for one_year in range(2000, 2019) :
    print("%s 年的生肖是 %s" % (one_year, chinese_zodiac[one_year % 12]))