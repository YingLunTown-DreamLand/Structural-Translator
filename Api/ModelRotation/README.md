# 作为 `Api` 使用

## 实现方法
假设需要被旋转建筑的 `WhiteWallJson` 文件放于 `C:\test.json` ，那么执行下述 `样例代码` 后，程序会在控制台打印 `旋转结果` 。
```python
from Api.ModelRotation.main import ModelRotation
demo = ModelRotation('C:\\test.json',xBot=90,yBot=0)
demo.main()
# ModelRotation

print(demo.resultList)    # result: list
# Print
```
有关相应的使用说明及详细使用，请见有关函数的注释。