# 由 New Bing 编写
# 导入re模块和random模块
import re
import random

# 读取文件内容
with open("setting.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 使用列表推导式创建一个字典，将每一行的第一个元素作为键，将剩余的元素组成一个列表作为值
replace_dict = {line.split(",")[0]: line.split(",")[1:] for line in lines if not line.startswith(("#", "["))}

# 让用户选择是从text.txt内读取还是直接输入文字
choice = input("请选择从文本内读取还是直接输入文字（输入1或2来选择，如果文本有换行务必选1）：")

# 如果用户选择1，就从text.txt内读取文字
if choice == "1":
    # 读取text.txt文件内容
    with open("text.txt", "r", encoding="utf-8") as f:
        text = f.read()
# 如果用户选择2，就让用户输入文字
elif choice == "2":
    # 获取用户输入的文字
    text = input("请输入一段文字：")
# 如果用户选择其他，就提示错误并退出程序
else:
    print("错误的选择，请重新运行程序")
    exit()

# 使用splitlines函数将文字按照换行符分割成一个列表，添加一个参数keepends=True，保留换行符
text_list = text.splitlines(keepends=True)

# 创建一个空列表，用来存储处理后的文字
new_text_list = []

# 遍历文字列表中的每一个元素
for text in text_list:
    # 遍历字典中的每一对键值
    for key, value in replace_dict.items():
        # 使用random模块中的choice函数从值的列表中随机选择一个元素作为替换的目标
        target = random.choice(value)
        # 将文字中的键替换成目标，忽略大小写
        text = re.sub(key, target, text, flags=re.IGNORECASE)

    # 读取setting.txt文件的第一行，并赋值给一个变量
    line = open("setting.txt", "r", encoding="utf-8").readline()
    # 获取冒号后面的部分，并赋值给一个变量
    symbols = line.split("=")[1]
    # 去掉字符串两端的空格或换行符
    symbols = symbols.strip()

    # 创建一个空字符串，用来存储插入符号后的文字
    new_text = ""

    # 初始化一个变量，用来记录当前的位置
    index = 0

    # 遍历文字中的每一个字
    for char in text:
        # 将当前的字添加到新字符串中
        new_text += char
        # 更新当前的位置
        index += 1

        # 判断当前的字是否是换行符，如果是的话，就不要插入符号，直接添加到新字符串中，并重置当前的位置为零
        if char == "\n":
            index = 0
            continue

        # 如果当前的位置等于或超过了随机生成的间隔
        if index >= random.randint(1, 7):
            # 从symbols变量中随机选择一个符号，并添加到新字符串中
            new_text += random.choice(symbols)
            # 重置当前的位置为零
            index = 0

    # 将处理后的文字添加到新列表中
    new_text_list.append(new_text)

# 使用join函数将新列表重新连接成一个字符串
new_text = "".join(new_text_list)


# 打印处理后的文字
print(new_text)

# 将处理后的文字保存到文件中
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(new_text)
