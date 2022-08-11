# Structural-Translator(结构翻译器)
A software that translates `.mcstructure` into `.bdx` .<br>
这是一个翻译软件，用于将 `.mcstructure` 文件转换为 `.bdx` 格式。

## How to use(如何使用)?
1. Download the file named `Translator.exe` and put it with `input.mcstructure` .
   - [Download link](https://github.com/Happy2018new/Structural-Translator/raw/main/Translator.exe)
2. Then run this program.
***
1. 下载`Translator.exe`并把它和`input.mcstructure`放在一起。
   - [下载链接](https://github.com/Happy2018new/Structural-Translator/raw/main/Translator.exe)
2. 然后运行这个程序。
## Language(语言)
This program only supports Chinese.<br>
这个程序只支持中文。
## 已加入的功能(This is not translated into English)
- 基本的翻译功能
- 读取命令方块的数据并写入到生成的 `.bdx` 文件中
- 大部分方块的方块状态(数据值)
- 替换方块ID(根据方块池，将一种方块ID变更为另外一种，支持数据值检测)
- 跳过空气(要求最终生成的 `.bdx` 不绘制空气，是一个 `可选` 选项)
- 蛇形翻译(以最大 `16 * 16` 的区域为基础来进行翻译，且方向是蛇形的，便于后续的导入)
- 支持超大文件(如大小达到 `500 MB` 的结构)
- 显示翻译进度
## 什么是 `.mcstructure` 和 `.bdx` ?(This is not translated into English)
1. `.mcstructure` 是 `Minecraft Bedrock Edition` 的原版文件，因此可以在电脑端通过 `结构方块` 导出。
2. `.bdx` 是 `FastBuilder` 支持的文件格式，用于将 `.bdx` 内记录的建筑物数据导入到 网易我的世界中国版 · 基岩版租赁服。
3. 你可以在这里访问 `FastBuilder` 的库：
   - [PhoenixBuilder](https://github.com/LNSSPsd/PhoenixBuilder/)
4. 如果你想要购买 `FastBuilder` ，您可以前往：
   - [用户中心](https://uc.fastbuilder.pro/)
   - [官网](https://fastbuilder.pro/)
## About Me(联系我)
You can contact me through `QQ` , my `QQ` is `3527679800` .<br>
您可以通过 `QQ` 联系我，我的 `QQ` 是 `3527679800` 。
## 更新日志(This is not translated into English)
- `v22.0 - 2022/08/11 Afternoon`
   - 在一定程度上支持了 白墙(`作弊类软件`) 导出的建筑文件(`JSON`) & 于 [3642335](https://github.com/Happy2018new/Structural-Translator/commit/36423355547af1d0141ebb8bc867e364408e272c) 更新
- `v20.5 - 2022/08/11 Morning`
   - 现在在移动画笔时使用了其他类型的命令，一定程度上优化了解压后的文件大小 & 于 [f6cf5ee](https://github.com/Happy2018new/Structural-Translator/commit/f6cf5ee559551f63e6dda714193dbd01c39f32ef) 更新
- `v20.2 - 2022/08/10 Morning`
  - 修复了无法正常解析 `minecraft:planks` 的数据值的问题 & 于 [359a7ba](https://github.com/Happy2018new/Structural-Translator/commit/359a7bacc32c9c479fc88600f03f740e6c3d0e27) 修复
- `v20.1 - 2022/08/09 Night`
  - 修复了无法正常解析 `minecraft:stone` 的数据值的问题 & 于 [359a7ba](https://github.com/Happy2018new/Structural-Translator/commit/359a7bacc32c9c479fc88600f03f740e6c3d0e27) 和 [895ac42](https://github.com/Happy2018new/Structural-Translator/commit/895ac4285c2ee1415236905a2017d9ddc06e82f2) 修复
