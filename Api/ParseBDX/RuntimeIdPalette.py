import json
# 载入依赖项

with open("Api/ParseBDX/resources/blockRuntimeIDs/netease/runtimeIds_2_1_10.json") as file:
    version2110 = json.loads("".join(file.readlines()))
# 2_1_10
with open("Api/ParseBDX/resources/blockRuntimeIDs/netease/runtimeIds_2_2_15.json") as file:
    version2215 = json.loads("".join(file.readlines()))
# 2_2_15
with open("Api/ParseBDX/resources/blockRuntimeIDs/netease/runtimeIds_117.json") as file:
    version117 = json.loads("".join(file.readlines()))
# 117