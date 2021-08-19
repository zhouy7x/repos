1. 安装apps目录中的jdk-16, python3, tesseract-ocr。python3安装时注意勾选“add python to PATH”，安装成功是win+R输入cmd，然后回车，在命令行输入python -V, 得到结果3.7.9;
2. 将apps\下面的tessdata解压并复制到tesseract-ocr的安装目录C:\Program Files\Tesseract-OCR，覆盖同名目录；
3. 解压jTessBoxEditor-1.4.zip，这是修改识字结果的图形工具，双击train.bat运行，先设置font为中文黑体,然后
	（1）打开jTessBoxEditor，选择Tools->Merge TIFF，进入训练样本所在文件夹“0808\门派”，文件类型选所有文件，全部选中要参与训练的样本图片；
	（2）点击 “打开” 后弹出保存对话框，选择保存在当前路径下，文件命名为 “lan3.test.exp0.tif” ，格式只有一种 “TIFF” 可选。
	（3）cmd下切换路径到 “0808\门派”, 运行 `python traindata.py makebox lan3 chi_sim`,这会在当前目录下生成一个.box文件；
	（4）使用jTessBoxEditor矫正.box文件的错误，参考https://bbs.huaweicloud.com/blogs/143914 的第4条的第（4）小条；
	（5）纠正一个image，就点Save先保存；
	（6）全部完成后，cmd命令行下运行`python traindata.py debug lan3`, 看看有没有报错，就是显示乱码的字在第几行错了，按照行数，使用jTessBoxEditor再次矫正，实在纠正不了，就删除这行，然后重复运行debug命令，直到没有错误；
	（7）无错后，cmd命令行下运行`python traindata.py train lan3`, 当前目录下得到一堆文件，其中一个是lan3.traineddata，把这个复制到C:\Program Files\Tesseract-OCR\tessdata目录中去，就可以使用了；
4.做完门派的，再去同样的做名字的，就好了，换个名字lan4, 我需要这得到的两个lan3.traineddata和lan4.traineddata，然后跟我做好的数字识别lan2.traineddata的合并，就可以使用另一个脚本，自动识别处理结果了。
5.完结撒花~

附：
1.jdk16 link: https://www.oracle.com/java/technologies/javase/jdk16-archive-downloads.html#license-lightbox