### matplotlib基本功能详解

### 基本绘图

#### 绘图核心API

案例：绘制一条余弦曲线

```python
import numpy as np
import matplotib.pyplot as mp

mp.plot(xarray,yarray)
#显示图表
mp.show()
```



#### 绘制水平线与垂直线

```python
import numpy as np
import matplotlib.pyplot as mp

#hortical 绘制水平线
mp.hlines(xval,xmin,xmax)
mp.hlines([10,20,30,40],[1,2,3,4],[2,3,4,5])
#vertical 绘制垂直线
mp.vlines(yval,ymin,ymax)
mp.vlines(4,10,35)

mp.show()
```



#### 线型、线宽和颜色

案例：绘制一条正弦曲线

```python
#linestyle:线形  '-' '--' '-.' ':'
#linewidth:线宽
#color:英文单词或#495434或(1,1,1)
#alpha: 透明度

import numpy as np
import matplotlib.pyplot as mp

#线性拆分1000个点
x = np.linspace(-np.pi,np.pi,1000)
# print(x,x.shape,'--->x')
sinx = np.sin(x)
# print(sinx,sinx.shape,'--->sinx')
#余弦曲线 cos(x)/2
cosx = np.cos(x)/2

mp.plot(x,sinx,linestyle='--',linewidth=20,color='orangered',alpha=0.8)
mp.plot(x,cosx,linestyle='-.',linewidth=2,color='dodgerblue',alpha=0.9)
mp.show()
```



#### 设置坐标轴范围

案例：把坐标轴范围设置为 -π ~ π

