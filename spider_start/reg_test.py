# 1998年10-1
# 1998-10-1
# 1998 10 1
# 1998_10 1
# 1998\10\1
# 1998.10 1
# 1b0
# bby
# z
# zoo
# bobbbycb
# bo
# hi him history
# hi-him
# mhi-him
# b* 代表匹配b 0次或多次，0次时为空？
# b+匹配的是每行每组符合要求的最长的字符串
# o|cb代表匹配o 或者cb
# \d{4}[年 .\-_]中括号中的-是a-z的-，需要匹配-的时候需要加转义字符,其他字符不需要转义仅代表字符
import re

# 提取字符串
# 替换
# 搜索
#
# info = "姓名:bobby1987 生日:1987年10月1日 本科:2005年9月1日"
# # 别忘记传目标字符串info
# # findall 返回list
# print(re.findall("生日.\d{4}",info))
# # match从头部开始匹配，返回的是re.Match对象，且默认匹配一行
# match_result=re.match(".*生日.\d{4}",info)
# print(match_result)
# # 还可以分组
# match_result=re.match(".*生日.(\d{4}).*本科.(\d{4})",info)
# print(match_result.group(),)
# print(match_result.group(1))
# print(match_result.group(2))
#
# sub_result=re.sub("\d{4}","2019",info)
# print(info)
# print(sub_result)
# # search不限定从最开始搜索，默认匹配多行
# match_result=re.search("生日.(\d{4}).*本科.(\d{4})",info)
# print(match_result.group(),)
# print(match_result.group(1))
# print(match_result.group(2))

name = """i am bobby1,your name is  bobby2,
his name is bobby3
"""
# re模块IGNORECASE忽略大小写
# search默认匹配多行,贪婪匹配到行末，返回第一个匹配成功的,
# group(0)和group() 匹配正则匹配出的完整内容，group(1)匹配分组里面的内容
# print(re.search("Bobby",name,re.IGNORECASE).group())
x = re.search("am.*(bobby.)", name)
y = x.group(0)
z = x.group(1)
print(y)
print(z)
pass

# match默认从开始位置匹配到回车换行符就结束了，DOTALL不会因为回车换行符就结束
# print(re.match("Bobby",name,re.DOTALL).group())
pass
