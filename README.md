# Structural-Translator
A software that translates `.mcstructure` into `.bdx`





## How to use?
1. Download the file named `Translator.exe` and put it with `input.mcstructure`
   - [Download link](https://github.com/Happy2018new/Structural-Translator/releases/download/Alpha(v71.0)/Translator.exe)
2. Then run this program





## Run this program from the source code in `Termux`
Download and first use
1. Execute this command in `Termux`
```shell
apt update && apt upgrade && apt install python && apt install git && pip install brotli && MATHLIB=m pip install numpy && pip install nbtlib && cd /sdcard && git clone https://github.com/Happy2018new/Structural-Translator/ && cd Structural-Translator
```
2. Then put `input.mcstructure` or `input.json` in the path `/storage/emulated/0/Structural-Translator`<br>
3. Execute `python Translator.py` in `Termux`
***
Subsequent Use
1. Execute command `cd /sdcard/Structural-Translator` in `Termux`
2. Put the `input.mcstructure` file or the `input.json` file in the path `/storage/emulated/0/Structural-Translator`
3. Execute `python Translator.py` in `Termux`
***
Remove
```shell
cd /sdcard && rm -r Structural-Translator
```
***
Update or Upgrade
```shell
apt update && apt upgrade && apt install python && apt install git && pip install brotli && MATHLIB=m pip install numpy && pip install nbtlib && cd /sdcard && rm -r Structural-Translator && git clone https://github.com/Happy2018new/Structural-Translator/
```





## Advanced Functions
We support batch mode as advanced functions. The sample documentation [here](https://github.com/Happy2018new/Structural-Translator/blob/main/Doc/settings.json.py) shows you how to use these advanced options.





## Language
This program only supports Chinese<br>





## Existing Features
- Basic translation function
- Get the command blocks data and write them into the `.bdx` file
- Block States
- `Experimental - The items of the container`
- Replace thr block id or thr block state to another
- `Optional options - Skip the air`
- Based on the `16 * 16` areas
- Support large `.mcstructure` files
- Display translation progress
- `Advanced Functions - Batch mode`





## Api
See [Api](https://github.com/Happy2018new/Structural-Translator/tree/main/Api) for more infomation





## What is `.mcstructure` and `.bdx` ?
1. You can export the `.mcstructure` files from `Minecraft Bedrock Edition`
2. `FastBuilder` support `.bdx` files, so you can use `FastBuilder` to import buildings in `China - Minecraft Bedrock Edition Server`
3. You can access `FastBuilder` repository through this link
   - [PhoenixBuilder](https://github.com/LNSSPsd/PhoenixBuilder/)
4. If you want to buy and use `FastBuilder` , the following links may help you
   - [User Center](https://uc.fastbuilder.pro/)
   - [Official Website](https://fastbuilder.pro/)





## Contact
You can contact me through the following links
   - [QQ](https://qm.qq.com/cgi-bin/qm/qr?k=zxS4AyUXd5M3ktypIKmBf9KQCGTSAwwI&noverify=0&personal_qrcode_source=3)
   - [Bilibili](https://space.bilibili.com/320298121)
   - [Email](mailto:chenbo79800@163.com)





## Update Logs
_For the update logs of previous versions, please go to link [Old Update Logs](https://github.com/Happy2018new/Structural-Translator/blob/main/Old%20Update%20Logs.md)_
***
- `v71.0 - 2022/11/13 Noon`
   - Fixed a path issue with Android and output failure prompts are now supported & Updated and fixed in [a7cdc01](https://github.com/Happy2018new/Structural-Translator/commit/a7cdc014eebf2a2dd28cc0fa138906474ac8694e)
- `v70.2 - 2022/11/12 Night`
   - Fix a bug that output wrong logs & Fixed in [d71251c](https://github.com/Happy2018new/Structural-Translator/commit/d71251cd33aa66dec2d6795924a73db88906bd32)
- `v70.1 - 2022/11/12 Night`
   - Fix a bug that can not translate json files & Fixed in [4126bdc](https://github.com/Happy2018new/Structural-Translator/commit/4126bdccc6da71df17d6c009203e6276622a533c)
- `v70.0 - 2022/11/12 Afternoon`
   - Support Batch mode. See [Advanced Functions](https://github.com/Happy2018new/Structural-Translator#advanced-functions) and [settings.json](https://github.com/Happy2018new/Structural-Translator/blob/main/Doc/settings.json.py) for more infomation & Updated in [215cc8d](https://github.com/Happy2018new/Structural-Translator/commit/215cc8dda8cba8d4ae1feca0392ea42bd2c4ca16)
- `v46.1 - 2022/10/30 Afternoon`
   - A small change of add `Operation 39(recordBlockEntityData)` to the output `BDX` files & Updated in [701aecd](https://github.com/Happy2018new/Structural-Translator/commit/701aecd9f70bef778cb075e2da010045f8b0b975)
- `v46.0 - 2022/10/29 Noon`
   - Support `Operation 39(recordBlockEntityData)` & Updated in [4afadf4](https://github.com/Happy2018new/Structural-Translator/commit/4afadf447c2ca890bb18458d080d63bec1c6fa14)
- `v43.0 - 2022/10/25 MidNight`
   - Full `.mcstructure` files parsing and reverse parsing are supported and fix some bugs & Updated and fixed in [afcd812](https://github.com/Happy2018new/Structural-Translator/commit/afcd812e12c301152af52806e31d42bec8e7cc2c)
- `v42.0 - 2022/10/21 Night`
   - Rewrite the main function which translate the `WhiteWallJson` files & Updated in [6bc8325](https://github.com/Happy2018new/Structural-Translator/commit/6bc832594685b6cae448a6397c0afd7f7eadaa68)





## LICENSE
See [LICENSE](https://github.com/Happy2018new/Structural-Translator/blob/main/LICENSE) for more infomation