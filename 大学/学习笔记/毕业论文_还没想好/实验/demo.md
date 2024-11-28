---
mindmap-plugin:
---
实验环境
GPU：4070ti
CPU：
内存：32g 4800ghz DDR5






---
池化层

```python

```

pytorch 池化层 核移动 默认不重合（可以指定）












----
输出每一层

```python
X = torch.rand(size=(1, 1, 28, 28),dtype=torch.float32)  
for layer in net:  
    X = layer(X)  
    print(layer.__class__.__name__, "output shape :\t", X.shape)
```
