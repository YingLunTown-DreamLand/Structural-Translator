# 常规使用

## 要解析的 `BDX` 文件
要解析的一个或多个 `BDX` 文件请置于 `Api/ParseBDX` 文件夹下。

## 输出位置
解析后的文件输出在 `Api/ParseBDX/Output` 文件夹下，且可以被 `WhiteWall` 解析。

## 运行源代码
请通过 `Visual Studio Code` 打开 `Api` 文件夹的上一级目录，然后运行 `Api/ParseBDX/Batch.py` 即可。





# 作为 `Api` 使用

## 实现方法
假设需要被解析的 `BDX` 文件放于 `C:\test.bdx` ，那么执行下述 `样例代码` 后，程序会在控制台分别打印 `解析结果` 和 `解析日志` 。
```python
from Api.ParseBDX.main import ParseBDX
demo = Parse('C:\\test.bdx')
demo.main()
# Parse BDX files

print(demo.resultList)    # result: dict
print(demo.logList)    # logs: list
# Print
```

## 注意事项
此 `Api` 使用了其自身模块中的 `全局变量` ，因此您应当注意到部分情况下您不能在您的代码下使用此 `Api` 。