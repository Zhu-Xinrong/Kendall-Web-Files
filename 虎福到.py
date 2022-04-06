import turtle as t    #导入模块turtle，在以下代码简写为t

#开始设定基本参数
t.bgcolor('orange')    #设置背景颜色为橙色
t.setup(600,700)    #设置窗口大小：宽600px，长700px

t.fillcolor('yellow')    #设置填充颜色为黄色

#开始制作门
t.penup()    #抬笔
t.goto(-175,225)    #移动至-175,225坐标位置
t.pendown()    #隐藏画笔
t.begin_fill()    #开始填充
for i in range(2):    #循环2次：
    t.forward(350)        #前进350px
    t.right(90)        #右转90度
    t.forward(525)        #前进525px
    t.right(90)        #右转90度
t.end_fill()    #结束填充

t.fillcolor('red')    #设置填充颜色为红色

t.penup()    #抬笔
t.goto(-150,-300)    #移动至-150,-300坐标位置
t.pendown()    #隐藏画笔
t.left(90)    #左转90度
t.forward(500)    #前进500px
t.right(90)    #右转90度
t.forward(300)    #前进500px
t.right(90)    #右转90度
t.forward(500)    #前进500px

t.left(90)    #左转90度

#开始制作福字
#开始制作福字样式
t.penup()    #抬笔
t.goto(0,125)    #移动至0,125坐标位置
t.pendown()    #隐藏画笔
t.pencolor("black")    #设置画笔颜色为黑色
t.begin_fill()    #开始填充
t.right(45)    #右转45度
t.forward(200)    #向前200px
for i in range(3):    #循环三次：
    t.right(90)        #右转90度
    t.forward(200)        #向前200px
t.end_fill()    #结束填充
#开始制作福字文字
t.penup()
t.goto(-40,-60)
t.pendown()
t.write('福',font = ("Verdana",60,"normal"))

#开始制作对联

#开始制作上联
#开始制作上联样式
t.penup()    #抬笔
t.goto(-200,325)    #移动至-200,325坐标位置
t.pendown()    #隐藏画笔
t.begin_fill()    #开始填充
t.left(135)    #左转135度
for i in range(2):    #循环两次：
    t.forward(75)    #向前75px
    t.left(90)        #左转90度
    t.forward(625)        #向前625度
    t.left(90)        #左转90度
t.end_fill()    #结束填充
#开始制作上联文字
t.penup()
t.goto(-255,190)
t.pendown()
t.write('虎',font = ("Verdana",30,"normal"))    
t.penup()
t.goto(-255,90)
t.pendown()
t.write('啸',font = ("Verdana",30,"normal"))
t.penup()
t.goto(-255,-10)
t.pendown()
t.write('风',font = ("Verdana",30,"normal"))
t.penup()
t.goto(-255,-110)
t.pendown()
t.write('声',font = ("Verdana",30,"normal"))
t.penup()
t.goto(-255,-210)
t.pendown()
t.write('远',font = ("Verdana",30,"normal"))

#开始制作下联
#开始制作下联样式
t.penup()    #抬笔
t.goto(200,325)    #移动至200,325坐标位置
t.pendown()    #隐藏画笔
t.begin_fill()    #开始填充
t.left(90)    #左转90度
for i in range(2):    #循环两次：
    t.forward(625)        #向前625px
    t.left(90)        #左转90度
    t.forward(75)        #向前75px
    t.left(90)        #左转90度
t.end_fill()    #结束填充
#开始制作下联文字
t.penup()
t.goto(220,190)
t.pendown()
t.write('龙',font = ("Verdana",30,"normal"))
t.penup()
t.goto(220,90)
t.pendown()
t.write('翔',font = ("Verdana",30,"normal"))
t.penup()
t.goto(220,-10)
t.pendown()
t.write('海',font = ("Verdana",30,"normal"))
t.penup()
t.goto(220,-110)
t.pendown()
t.write('浪',font = ("Verdana",30,"normal"))
t.penup()
t.goto(220,-210)
t.pendown()
t.write('高',font = ("Verdana",30,"normal"))

#开始制作横批
#开始制作横批样式
t.penup()    #抬笔
t.goto(-175,325)    #移动至-175,325坐标位置
t.pendown()    #隐藏画笔
t.begin_fill()    #开始填充
for i in range(2):    #循环两次：
    t.forward(75)        #向前75px
    t.left(90)        #左转90度
    t.forward(350)        #向前350px
    t.left(90)        #左转90度
t.end_fill()    #结束填充
t.penup()
t.goto(-150,265)
t.pendown()
t.write('虎',font = ("Verdana",30,"normal"))
t.penup()
t.goto(-65,265)
t.pendown()
t.write('跃',font = ("Verdana",30,"normal"))
t.penup()
t.goto(20,265)
t.pendown()
t.write('龙',font = ("Verdana",30,"normal"))
t.penup()
t.goto(105,265)
t.pendown()
t.write('腾',font = ("Verdana",30,"normal"))

t.hideturtle()    #隐藏画笔
t.done()    #完成时不关闭窗口

#代码中所有的
#t.penup()    #抬笔
#t.goto(x,y)    #移动至x，y坐标位置
#t.pendown()    #隐藏画笔
#t.write('a',font = ("Verdana",b,"normal"))    #用Verdana字体，写一个b大小的“a”字
#的注释都统一写在此处

#Copyright (c) 2022 ZhuXinrong. All rights reserved.
