# Draw-with-turtle 
### 利用turtle函数绘制分形几何*（我想画的是漂亮的花，但这画出来跟我设想的有点不一样TAT）*

关于Turtle的基本语法我参考的是官方说明文档：
[想参考点这里](https://docs.python.org/3/library/turtle.html?highlight=turtle#module-turtle)

根据这个文档我设置好了画笔颜色、粗细等等

然后大概设想了一下绘制过程，大致可以分为：

1. 绘制一个基础四边形

2. 利用用循环在360°内绘制10个一样的四边形，构成基本的花的形状

3. 利用递归思想调用当前函数改变边长（每次+10）重复绘制，设置一个最大值

画出的图形如下：

![avatar]


