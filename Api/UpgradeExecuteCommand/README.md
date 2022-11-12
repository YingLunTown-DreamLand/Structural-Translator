# 常规使用

## 要升级的 `JSON` 文件
要解析的一个或多个 `input.json` 文件请置于 `Api/UpgradeExecuteCommand` 文件夹下。<br>
> 注意事项<br>
> 此 `JSON` 文件须可被 `WhiteWall` 解析。

## 输出位置
解析后的文件输出在 `Api/UpgradeExecuteCommand` 文件夹下，且可以被 `WhiteWall` 解析。

## 运行源代码
请通过 `Visual Studio Code` 打开 `Api` 文件夹的上一级目录，然后运行 `Api/UpgradeExecuteCommand/Batch.py` 即可。





# 作为 `Api` 使用

## 实现方法
假设需要被解析的 `WhiteWallJson` 文件放于 `C:\test.json` ，那么执行下述 `样例代码` 后，程序会在控制台分别打印 `解析结果` 和 `解析日志` 。
```python
from Api.UpgradeExecuteCommand.main import UpgradeExecuteCommand
demo = Parse('C:\\test.json')
demo.main()
# Upgrade Execute Command

print(demo.resultList)    # result: dict
print(demo.logList)    # logs: list
# Print
```

## 注意事项
此 `Api` 使用了其自身模块中的 `全局变量` ，因此您应当注意到部分情况下您不能在您的代码下使用此 `Api` 。