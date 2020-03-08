# 列表 [123, 'abc'] 列表里的元素的内容是可变更的
# 元组 ('abc', 'def') 元组中元素的内容是不可变更的
# 列表和元组中的内容都可以存在不同类型

# u 代表Unicode
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座',
               u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23),
               (11, 23), (12, 23))

# a = (1, "a")
# print(a)

# a = (1, 3, 5, 7)
# b = 4
# filter(lambda x: x < b, a)
# print(filter(lambda x: x < b, a))
# print(list(filter(lambda x: x < b, a))) # 取出a中小于4的元素
# print(len(list(filter(lambda x: x < b, a))))

(month, day) = (2, 16)
zodiac_days = filter(lambda x: x <= (month, day), zodiac_days)

zodiac_len = len(list(zodiac_days)) % 12
print(zodiac_name[zodiac_len]) # output: 水瓶座

a_list = ['abc', 'xyz']
a_list.append(123)
print(a_list)
a_list.remove('xyz')
print(a_list)