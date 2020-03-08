# while语句

import time

num = 5
while True :
    num = num + 1
    if num == 20 : # stop when num is 20
        break
    if num == 10 : # skip when num is 10
        continue
    print(num)
    time.sleep(1)