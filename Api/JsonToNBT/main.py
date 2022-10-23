import sys
sys.path.append(".")
import Api.JsonToNBT.function
import json
import nbtlib
# 载入依赖项

path = 'Api/JsonToNBT/input.json'
outputPath = 'Api/JsonToNBT/ans.txt'
# 输入文件路径

with open(path,"r+",encoding='utf-8') as file:
    ans = nbtlib.serialize_tag(
        Api.JsonToNBT.function.JSONCompound(
            json.load(file)
        )
    )
with open(outputPath,"w+",encoding='utf-8') as file:
    file.write(ans)
# 输出 NBT

print('SUCCESS - All down!')
print(f'SUCCESS - 转换结果保存在 {outputPath} 下.')
# 输出成功提示