# WPI_mat_to_txt
3.格式转换步骤
首先要先做一些准备工作。查看WPI文件夹，可以发现标注文件和图片文件命名并不一致。为了保持一致，需要做出相应修改：

将labels内标注文件命名改为对应的seqX.mat；

将trainval内序号从0X改为X.

改好后，文件树结构应为：

└─WPI
├─test
│ ├─labels
│ │ seq1.mat
│ │ seq2.mat
│ │ …
│ │ seq17.mat
│ │ readme.txt
│ ├─seq1
│ ├─seq2
│ ├─…
│ ├─seq17
│
└─trainval
├─labels
│ readme.txt
│ seq1.mat
│ …
│ seq7.mat
├─seq1
├─…
└─seq7
————————————————
版权声明：本文为CSDN博主「Atarasin」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Azahaxia/article/details/108330265
