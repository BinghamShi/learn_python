# 计算星座
# 使用元组，元组也是序列的一种
# 元组可以嵌套
# 元组存的是数字时大小比较，可以看作是数字的加和比较
# 列表存的内容可变更，元组不可变更
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座',
               u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23),
               (11, 23), (12, 23))

int_month = int(input("请输入月份："))
int_day = int(input("请输入日期："))

zodiac_day = filter(lambda x: x <= (int_month, int_day), zodiac_days)
zodiac_len = len(list(zodiac_day)) % 12
print(zodiac_name[zodiac_len])

for zd in range(len(zodiac_days)):
    if (int_month, int_day) < zodiac_days[zd]:
        print(zodiac_name[zd])
        break
    elif int_month == 12 and int_day >= 23:
        print(zodiac_name[0])
        break

# 利用for循环嵌套if，else语句实现filter功能


# 列表可以增加和修改数据

a_list = ["abc", "def"]
a_list.append("ghi")
print(a_list)
# 如果删除的元素不在列表会报错
a_list.remove("def")
print(a_list)
b_list = ["def"]
print(a_list + b_list)
print("def" in a_list)
print(a_list[0:1])
print(a_list * 3)
