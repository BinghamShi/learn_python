# try:
#    <监控异常>
# except Exception[, reason]:
#    <异常处理代码>
# finally:
#    <无论异常是否发生都执行>
#

# try:
#     year = int(input('input year:'))
# except ValueError:
#     print("年份需要输入数字")
#
# try:
#     a = 123
#     a.append()
# except AttributeError:
#     print("数字没有append函数")


# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print(' 0不能做除数 %s' % e)
#
# try:
#     print(1/'a')
# except Exception as e:
#     print(' %s ' % e)

# 自定义错误
# try:
#     raise NameError('helloError')
# except Exception as e:
#     print(' %s ' % e)


# finally 无论如何都会执行
try:
    a = open('name.txt')
except Exception as e:
    print(' %s ' % e)
finally:
    a.close()







