# Structural-Translator(结构翻译器)
A software that translates `.mcstructure` into `.bdx` .<br>
这是一个翻译软件，用于将 `.mcstructure` 文件转换为 `.bdx` 格式。

## 置顶内容(This is not translated into English)
请勿将本工具用于有版权建筑，一切都应该取得建筑原作者的授权！！！！！！<br>
本工具的目的是为了导入“有灵魂”的建筑物，所以我十分建议自己造！！！<br>
如果侵权事件仍然发生，那么未来将不会考虑支持更多功能(指的是 `JSON` 方面)，而是将相应功能从库中删除。

## How to use(如何使用)?
1. Download the file named `Translator.exe` and put it with `input.mcstructure` .
   - [Download link](https://github.com/Happy2018new/Structural-Translator/raw/main/Translator.exe)
2. Then run this program.
***
1. 下载`Translator.exe`并把它和`input.mcstructure`放在一起。
   - [下载链接](https://github.com/Happy2018new/Structural-Translator/raw/main/Translator.exe)
2. 然后运行这个程序。
## Run the program on source code(For `Termux` )
Download and First Use
1. Execute the following command
```
apt update && apt upgrade && apt install python && apt install git && pip install brotli && cd /sdcard && git clone https://github.com/Happy2018new/Structural-Translator/ && cd Structural-Translator
```
2. Then put `input.mcstructure` in the path `/storage/emulated/0/Structural-Translator` and run command `python Translator.py` .
***
Subsequent Use
1. Run command `cd /sdcard/Structural-Translator` .
2. Then put `input.mcstructure` in the path `/storage/emulated/0/Structural-Translator` .
3. Run command `python Translator.py` .
***
Remove
```
cd /sdcard && rm -r Structural-Translator
```
***
Update
```
cd /sdcard && rm -r Structural-Translator && git clone https://github.com/Happy2018new/Structural-Translator/
```
## 从源代码运行程序(对于 `Termux` )
下载和首次使用
1. 在 `Termux` 执行此命令：
```
apt update && apt upgrade && apt install python && apt install git && pip install brotli && cd /sdcard && git clone https://github.com/Happy2018new/Structural-Translator/ && cd Structural-Translator
```
2. 将 `input.mcstructure` 或 `input.json` 放置在路径 `/storage/emulated/0/Structural-Translator` ，然后在 `Termux` 执行命令 `python Translator.py` 。
***
后续的使用
1. 在 `Termux` 执行命令 `cd /sdcard/Structural-Translator` 。
2. 将 `input.mcstructure` 或 `input.json` 放置在路径 `/storage/emulated/0/Structural-Translator` 。
3. 在 `Termux` 执行命令 `python Translator.py` 。
***
移除
```
cd /sdcard && rm -r Structural-Translator
```
***
更新
```
cd /sdcard && rm -r Structural-Translator && git clone https://github.com/Happy2018new/Structural-Translator/
```
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
- `v31.0 - 2022/08/18 Noon`
   - 支持了 `潜影盒` 中的物品(仅限 `物品数据值` ) & 于 [bcbc0dd](https://github.com/Happy2018new/Structural-Translator/commit/bcbc0dd727bf7a1d6698653dddecf47b074db0f4) 更新
- `v30.0 - 2022/08/18 Morning`
   - `实验性功能` - 支持了容器中的物品(仅限 `物品数据值` )，具体如下 & 于 [e7d8f4a](https://github.com/Happy2018new/Structural-Translator/commit/e7d8f4ab88f4584de79ab773b41dbe339956049a) 更新
   ```
   高炉(燃烧的高炉)
   烟熏炉(燃烧的烟熏炉)
   熔炉(燃烧的熔炉)
   木桶
   箱子
   陷阱箱
   讲台
   漏斗
   发射器
   投掷器
   炼药锅(岩浆炼药锅)
   唱片机
   酿造台
   ```
- `v26.4 - 2022/08/13 Afternoon`
   - 修复了在使用 `组件 - 替换方块ID` 时会打印 `方块池` 列表的问题 & 于 [31e43eb](https://github.com/Happy2018new/Structural-Translator/commit/31e43eb705d9b9eb5cc63fd33e7c75c9419ee569) 修复
- `v26.3 - 2022/08/13 Afternoon`
   - 修复了在使用 `组件 - 替换方块ID` 时 `摆烂` 数据会丢失的问题，同时机制变更为如下 & 于 [4b4347b](https://github.com/Happy2018new/Structural-Translator/commit/4b4347b9b368657427b872f03bac33ecb3a51636) 修复
     - 当替换了 `minecraft:double_plant` 时，此方块若原本存在 `摆烂` 标记，则标记会丢失。
     - 如果 `replaceBlockId.txt` 未提到正确的替换 `minecraft:double_plant` 的命令，则相关的 `摆烂` 标记会予以保留。
- `v26.0 - 2022/08/12 Night`<br>
   - 修复了 `minecraft:double_plant` 在放置后会被破坏为掉落物的问题(恢复了原有的 `摆烂` 机制) & 于 [a2fb041](https://github.com/Happy2018new/Structural-Translator/commit/a2fb041a07ce5aa1b1bbd84b434df6ed8766945a) 修复
   - 当被翻译的结构存在 `含水方块` 时，会在翻译即将结束时打印警告 & 于 [a2fb041](https://github.com/Happy2018new/Structural-Translator/commit/a2fb041a07ce5aa1b1bbd84b434df6ed8766945a) 更新
   - 修复了无法正常解析 `带釉陶瓦` 这一类方块的数据值的问题 & 于 [a2fb041](https://github.com/Happy2018new/Structural-Translator/commit/a2fb041a07ce5aa1b1bbd84b434df6ed8766945a) 修复
- `v25.1 - 2022/08/12 Night`
   - 修复了无法正常解析 `minecraft:portal` 的数据值的问题 & 于 [82d043f](https://github.com/Happy2018new/Structural-Translator/commit/82d043ff42741f49bb910a126ecf15a75be78bb7) 和 [fe7eb74](https://github.com/Happy2018new/Structural-Translator/commit/fe7eb749909081234c518739af90b38ed3487db8) 修复
- `v25.0 - 2022/08/12 Afternoon`
   - 修复了无法正常解析下述方块的方块状态的问题 & 于 [9dc98f3](https://github.com/Happy2018new/Structural-Translator/commit/9dc98f3f2930a9257fc6bdb87bed8b4dbc1d8f9c) 修复<br>
      ```
      minecraft:dirt
      minecraft:stained_glass_pane
      minecraft:stained_hardened_clay
      minecraft:carpet
      minecraft:bedrock
      minecraft:cobblestone_wall
      minecraft:lantern
      minecraft:fence
      minecraft:chain
      minecraft:monster_egg
      minecraft:lightning_rod
      minecraft:stripped_warped_hyphae
      minecraft:crimson_hyphae
      minecraft:warped_hyphae
      minecraft:stripped_crimson_hyphae
      minecraft:mangrove_wood
      minecraft:stripped_mangrove_wood
      minecraft:sand
      ```
- `v23.0 - 2022/08/11 Night`
   - 修复了 白墙( `作弊类软件` ) 导出的建筑文件( `JSON` )不能被正常翻译的问题 & 于 [d8f640f](https://github.com/Happy2018new/Structural-Translator/commit/d8f640fb7eada15946f2cb79ac7a2c2393d3b1ca) 修复
- `v22.0 - 2022/08/11 Afternoon`
   - 在一定程度上支持了 白墙( `作弊类软件` ) 导出的建筑文件( `JSON` ) & 于 [3642335](https://github.com/Happy2018new/Structural-Translator/commit/36423355547af1d0141ebb8bc867e364408e272c) 更新
- `v20.5 - 2022/08/11 Morning`
   - 现在在移动画笔时使用了其他类型的命令，一定程度上优化了解压后的文件大小 & 于 [f6cf5ee](https://github.com/Happy2018new/Structural-Translator/commit/f6cf5ee559551f63e6dda714193dbd01c39f32ef) 更新
- `v20.2 - 2022/08/10 Morning`
  - 修复了无法正常解析 `minecraft:planks` 的数据值的问题 & 于 [359a7ba](https://github.com/Happy2018new/Structural-Translator/commit/359a7bacc32c9c479fc88600f03f740e6c3d0e27) 修复
- `v20.1 - 2022/08/09 Night`
  - 修复了无法正常解析 `minecraft:stone` 的数据值的问题 & 于 [359a7ba](https://github.com/Happy2018new/Structural-Translator/commit/359a7bacc32c9c479fc88600f03f740e6c3d0e27) 和 [895ac42](https://github.com/Happy2018new/Structural-Translator/commit/895ac4285c2ee1415236905a2017d9ddc06e82f2) 修复
## 免责声明(This is not translated into English)
- 若因为使用本软件而造成了任何可能的问题，我不会对此负责。（例如侵权等恶性事件）
- 本工具的初衷是更高效的创作以及保留租赁服内的建筑物，而非实施其他可能的违法事件。
- 同时，作者保留有关此工具的所有解释权。
- 特别应当注意的是，您不得将本工具用于盈利用途，除非得到作者的授权。
