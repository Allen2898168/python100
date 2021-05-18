"""
    十方教育面试题

    一份txt文件格式如下：
    url|get|post|body|header       从txt文件解析请求并写入响应码到txt文件， 统计成功200次数，失败次数

"""
import requests

# 解析txt文件,请求获取响应code
file_path = r"D:\test.txt"
with open(file_path) as f:
    txt = f.read().split("|")
url = txt[0]
get = txt[1]
post = txt[2]
body = txt[3]
header = txt[4]
if txt[1] == 'get':
    reps = requests.get(url=url, data=body, header=header)
    code = []
    code.append(reps.status_code)

# 假如请求响应码如下  写入txt文件：
code = ["200", "400", "500", "200", "200", "200", "500", "404", "200"]

with open(file_path, "w", ) as f:
    for i in code:
        f.write(str(i) + '\n')



# 读取txt文件，统计200次数
with open(file_path, "r") as f:
    print(f.read().count("200"))
