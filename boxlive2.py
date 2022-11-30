'''
听说这个游戏最大成活率可以有31%！群体需要跑好几次房间得到统计平均成活率数据。有的时候跑出来比如10轮都存活了！
[一道非常反直觉的数学题目](https://www.bilibili.com/video/BV1kt4y1t75F?spm_id_from=333.337.search-card.all.click)
'''
from itertools import count
import matplotlib.pyplot as plt
import random
value=[]
x=[]
y=[]
p=100 #人数和箱子数设置，同一个值
t=50 #每人尝试次数设置
death=0
survival=0
print("Here we begin the expriment!")
for n in range(1000): #试验次数设置，作图步长为1，n为横轴试验次数
    # print("\n***The {}th run is started".format(n+1))
    for i in range(p): #创建p个箱子
        value=random.sample(range(0,100),100) #箱子内部值设置（随机方法）
    count=0
    for j in range(p): #群体按个体轮流进行
        z=j  #关键赋值
        for k in range(t):
            if j == value[z]:
                print("Number {} find the box!".format(j+1))
                break   #找到了对应自己编号值的箱子就跳出k尝试循环出门
            else:
                z = value[z]
                #value[z]=value[value[z]] #寻找编号为此箱子值的下一个箱子，继续if判断
        else:
            print("Number {} died".format(j+1))
            count+=1
    if count!=0: #只有全部人都在尝试次数内都成功找到自己的箱子才能使得全队生存！一个人没找到全队死亡！
        death+=1
        print("{} people died during this {}th run cause whole team death!".format(count,n))
    else:
        survival+=1
        print("{} died during this {}th run cause whole team survive!".format(count,n))
    value=[]
    x.append(n+1)
    y.append(survival/(n+1)) #以试验次数为自变量，对群体成活率进行研究，实验次数越多应该趋于概率的稳定值。
    print("-----\n{} runs of expriments have been done and the survival rate is {}/{}".format(n+1,survival,death+survival))
plt.grid(True)
plt.title("The Game of {} people survival".format(p))
plt.xlabel("Runs")
plt.ylabel("Survival rate")
plt.plot(x,y,'bo-')
plt.axhline(sum(y)/len(y))
plt.show()
yr=y[-5:]
print("The approaching possibility is {}".format(sum(yr)/len(yr))) #求最终的趋近值，随着实验次数越多，应该区域一个概率值
# plt.savefig()

