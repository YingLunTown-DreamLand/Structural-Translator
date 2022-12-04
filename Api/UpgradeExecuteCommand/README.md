# 常规使用

## 要被升级 `Execute` 命令格式的 `JSON` 文件
要被升级的一个或多个 `JSON` 文件请置于 `Api/UpgradeExecuteCommand` 文件夹下。<br>
> 注意事项<br>
> 此 `JSON` 文件须可被 `WhiteWall` 解析。

## 输出位置
解析后的文件输出在 `Api/UpgradeExecuteCommand` 文件夹下，且可以被 `WhiteWall` 解析。

## 运行源代码
请通过 `Visual Studio Code` 打开 `Api` 文件夹的上一级目录，然后运行 `Api/UpgradeExecuteCommand/Batch.py` 即可。





# 升级 `WhiteWallJson` 中的 `Execute` 命令 & 作为 `Api` 使用

## 实现方法
假设需要被解析的 `WhiteWallJson` 文件放于 `C:\test.json` ，那么执行下述 `样例代码` 后，程序会在控制台分别打印 `解析结果` 和 `解析日志` 。
```python
import sys
sys.path.append('.')
from Api.UpgradeExecuteCommand.main import UpgradeExecuteCommand
demo = UpgradeExecuteCommand('C:\\test.json')
demo.main()
# Upgrade Execute Command

print(demo.resultList)    # result: dict
print(demo.logList)    # logs: list
# Print
```





# 将 `字符串` 中的 `Execute` 命令升级为新格式 & 作为 `Api` 使用

## 实现方法
假设需要被升级命令格式的 `字符串` 存放于变量 `Command` 中，那么执行下述 `样例代码` 后，程序会在控制台打印 `升级结果` 。
```python
import sys
sys.path.append('.')
from Api.UpgradeExecuteCommand.translateCommand import run
demo = run(Command)
# Upgrade Execute Command

print(demo)    # result - demo: str
# Print Result
```