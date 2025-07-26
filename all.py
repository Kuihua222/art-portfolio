import os

# 配置文件夹路径和年份
folder_path = './images/2024'  # 替换为你的图片文件夹路径
year = '2024'  # 替换为文件夹对应的年份

# 获取文件夹中的所有图片文件
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

# 按文件名排序
image_files.sort()

# 生成 JavaScript 对象格式的文本
output = f"const imageCategories = {{\n"
output += f"    {year}: [\n"
for file in image_files:
    output += f"                './images/{year}/{file}',\n"
output = output.rstrip(',\n') + '\n    ]\n};'

# 打印输出
print(output)

# 保存到文件
output_file = 'image_list.js'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(output)
print(f'\n已将结果保存到 {output_file}')