# 猜数游戏2
# Coding 常征
import random
secret = random.randint(1,10)#生成1~10之间的一个随机整数
times = 4#最多有4次机会
print('-----------------酸饺子学Python-----------------')
temp = input('您好，猜猜酸饺子心里想的数字，在1~10之间：\n')
if temp.isdigit():
    guess = int(temp)
    if guess == secret:
        print('卧槽！你是酸饺子肚子里的蛔虫吗？')
        print('奖励你个大大的赞！')
    else:
        i = 1
        while i <= times:#最多只能猜4次
            if guess > secret:
                print('哥，大了大了~~~')
            else:
                print('嘿，小了小了！！')
            temp = input('Come on！再猜一次：\n')
            if temp.isdigit():
                guess = int(temp)
                if guess == secret:
                    print('猜对啦！')
                    print('哼！猜对了也没有奖励！')
                    break
            else:
                print('这不是数字吧大哥~~')
            i += 1
    if guess != secret:
        print('我累个擦……大哥你是智障么？？')
    print('游戏结束，不玩啦~~')
else:
    print('大哥你不识数吗？？不跟你玩了~~')
