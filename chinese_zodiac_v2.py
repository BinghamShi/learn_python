# 测试用户输入，条件判断语法，for循环语法
import time
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊猴鸡狗猪'
current_year = 2020
year = int(input("请输入年份："))
print("你输入的年份是" + chinese_zodiac[year % len(chinese_zodiac)] + "年")
if year < current_year:
    print("过去的就让它过去吧！")
elif year == current_year:
    print("活在当下！")
else:
    print("向前看！")

# for循环语法
for cz in chinese_zodiac:
    print(cz)
for i in range(100):
    print(i)
for i in (1, 100):
    print(i)
for year in range(2000, 2020):
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))

# while语法 从1打印到100 中间不打印10
num = 0
while True:
    num = num + 1
    if (num == 10):
        continue
    if (num > 100):
        break
    print(num)
    time.sleep(1)


