import sys
sys.path.append(".")
import Api.SearchForCommand.function
# 载入依赖项

path = 'Api/SearchForCommand/input.json'
outputPath = 'Api/SearchForCommand/ans.json'
outputLogPath = 'Api/SearchForCommand/search.log'
# 输入文件之路径

Api.SearchForCommand.function.run(path,outputPath,outputLogPath)
# 提纯出具体的命令并生成文件

print('SUCCESS - All down!')
print(f'SUCCESS - 提纯结果保存在 {outputPath} 下.')
print(f'SUCCESS - 提纯日志保存在 {outputLogPath} 下.')
# 输出成功提示