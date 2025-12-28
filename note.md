![alt text](image-1.png)
# 1.输入：
按出现次数排序
汉字编码的问题：1 + 2 = 3，其实语义不满足 -->改为独热编码

## 词嵌入：Word Embedding
![alt text](image.png)
![alt text](image-2.png)
![alt text](image-3.png)
## 位置编码：Position Encoding
![alt text](image-4.png)
![alt text](image-5.png)


输入的x为：[batch_size,ctx_length,d_model]
           批次，     文字长度，   学习维度
只有后两个维度和W做计算
## 自注意力机制
![alt text](image-6.png)
1.计算输入x之间的关联程度
2.根据关联程度提取x的有用信息
3.输出包含不同注意力分配的信息
![alt text](image-7.png)
***多头***
![alt text](image-14.png)
这里不是切分而是投影
![alt text](image-8.png)
***掩码***
![alt text](image-9.png)

## 层归一化
![alt text](image-10.png)
![alt text](image-13.png)

## 因果掩码
![alt text](image-11.png)

## 交叉注意力机制
![alt text](image-12.png)
