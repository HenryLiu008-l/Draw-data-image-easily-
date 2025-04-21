
# 项目介绍
本项目用于方便生成数据**可视化图像**
欢迎各位大佬莅临指导
## 项目缘由
由于本人没有编程基础的同学在进行数学建模的时候用ai写的python进行可视化数据的程序无法运行，又不会改。所以我写了这样一个可视化操作程序，方便将数据可视化

# 依赖环境

- pandas

- tkinter

- matplotlib

# 环境部署

```python

pip install pandas

pip install tkinter

pip install matplotlib

```

# 使用说明
### 直接生成图像

直接运行代码后点击**文件**打开文件选择窗口

  
![]([images/introduction1.jpg at main · HenryLiu008-l/images](https://github.com/HenryLiu008-l/images/blob/main/introduction1.jpg))

 
选择一个表格文件

  
![]([images/file_exmple.png at main · HenryLiu008-l/images](https://github.com/HenryLiu008-l/images/blob/main/file_exmple.png))

 
在选择好后点击**读取**以读取表格文件

然后在x轴与y轴选区中输入要选择的那一列(如下图)

  ![]([images/exmple.png at main · HenryLiu008-l/images](https://github.com/HenryLiu008-l/images/blob/main/exmple.png))
  随后点击**生成**即可看到生成的可视化数据图像
  ![]([images/graph.png at main · HenryLiu008-l/images](https://github.com/HenryLiu008-l/images/blob/main/graph.png))
  ### 增加or修改值
  如果要对表格中的数据进行计算或者更改，可以点击**增删**
  ![]([images/introduction3.jpg at main · HenryLiu008-l/images](https://github.com/HenryLiu008-l/images/blob/main/introduction3.jpg))
  随后在该窗口中，**对象1**和**对象2**可以输入要进行计算的列，
  随后**增加列名**里输入二者计算后的值作为新增加的列的名称
  ![]([images/2.png at main · HenryLiu008-l/images](https://github.com/HenryLiu008-l/images/blob/main/2.png))
  之后点击**执行**即可
  若是要修改值,只需在**对象1**里输入要进行修改的列名，
  **对象2**里输入要赋予的新值
