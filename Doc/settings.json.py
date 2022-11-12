# 本文件的后缀名应当是 json ，但为了方便注释，所以本处以 py 作后缀名。
# 本文件的文件名应当是 settings.json ，且需要跟 Translator.exe 或 Translator.py 置于同一目录才可启用高级选项。
# 本文件的“全局设置”描述的是默认配置，且通常情况下都是按照此默认配置来进行翻译。
# 你提供的 settings.json 不需要包含所有的选项，你只需要填写你需要改动的选项即可。
# 对于此样例的其中一个纯 json 形式，请见当前文件夹下的 settings.json 文件。



import os

{
    "全局设置":
    {
        "文件搜索路径": os.path.normpath(os.getcwd()),
        # 从程序所在路径搜索 bdx 或 whitewall 文件
        # 这个路径必须是绝对路径
        "文件输出路径": os.path.normpath(f"{os.path.normpath(os.getcwd())}\\Output"),
        # 输出在程序所在文件夹下的 Output 文件夹内
        # 这个路径必须是绝对路径
        "组件 - 替换方块ID": [
            "B;minecraft:double_stone_block_slab,-1,minecraft:double_stone_slab,-1",
            "B;minecraft:double_stone_block_slab2,-1,minecraft:double_stone_slab2,-1",
            "B;minecraft:double_stone_block_slab3,-1,minecraft:double_stone_slab3,-1",
            "B;minecraft:double_stone_block_slab4,-1,minecraft:double_stone_slab4,-1",
            "B;minecraft:stone_block_slab,-1,minecraft:stone_slab,-1",
            "B;minecraft:stone_block_slab2,-1,minecraft:stone_slab2,-1",
            "B;minecraft:stone_block_slab3,-1,minecraft:stone_slab3,-1",
            "B;minecraft:stone_block_slab4,-1,minecraft:stone_slab4,-1",
            "B;minecraft:sea_lantern,-1,minecraft:sealantern,-1",
            "C;minecraft:double_stone_block_slab,-1,minecraft:double_stone_slab,-1",
            "C;minecraft:double_stone_block_slab2,-1,minecraft:double_stone_slab2,-1",
            "C;minecraft:double_stone_block_slab3,-1,minecraft:double_stone_slab3,-1",
            "C;minecraft:double_stone_block_slab4,-1,minecraft:double_stone_slab4,-1",
            "C;minecraft:stone_block_slab,-1,minecraft:stone_slab,-1",
            "C;minecraft:stone_block_slab2,-1,minecraft:stone_slab2,-1",
            "C;minecraft:stone_block_slab3,-1,minecraft:stone_slab3,-1",
            "C;minecraft:stone_block_slab4,-1,minecraft:stone_slab4,-1",
            "C;minecraft:sea_lantern,-1,minecraft:sealantern,-1"
        ],
        # C开头代表替换容器内的物品，B开头代表替换调色板中的方块
        # 以 B;minecraft:double_stone_block_slab,-1,minecraft:double_stone_slab,-1 为例，这句话指的是把 minecraft:double_stone_block_slab 变为 minecraft:double_stone_slab ，且不匹配数据值是否相同，也不改变数据值
        # 以 C;minecraft:x,1,minecraft:y,2 为例，这句话指的是把容器内数据值为 1 的 minecraft:x 物品改变为数据为 2 的 minecraft:y 物品
        # 以 B;minecraft:x,1,minecraft:y,-1 为例，这句话指的是把调色板内数据值为 1 的 minecraft:x 方块改变为 minecraft:y 方块，但不改变数据值
        # 以 B;minecraft:x,-1,minecraft:y,9 为例，这句话指的是把调色板内任意数据值的 minecraft:x 方块改变为数据值为 9 的 minecraft:y 方块
        "是否跳过空气": True,
        # 如果建筑物需要海底导入，我们建议设置为 False
        # 设置为 False 后将会在导入时导入空气
        # 通常情况下我们建议您设置为 True
        "开发者选项 - 是否启用": False    # 这个东西的作用就是输出 json 格式的 mcstructure 文件；此功能只会在翻译 mcstructure 文件时才会生效
    },
    "自定义配置": 
    [
        {
            "文件输入路径": ["demo1.bdx","test/demo2.json"],
            # 可以看到这是一个列表，因为很有可能多个文件都采用一个自定义配置
            # 这里要求提供相对路径（相对于全局配置下“文件搜索路径”的路径）
            # 这里的键名是“文件输入路径”，而不是全局配置下的“文件搜索路径”
            "文件输出路径": "E:/output/",
            # 这里要求填写绝对路径
            "组件 - 替换方块ID": [],    # 此处不会使用全局配置下的表，而是采用这张空的表
            "是否跳过空气": False,    # 此处不会使用全局配置下的配置，而是采用此配置，也就是不会跳过空气
            "开发者选项 - 是否启用": True    # 此处不会使用全局配置下的配置，而是采用此配置，也就是启用开发者选项
        }
    ]
}