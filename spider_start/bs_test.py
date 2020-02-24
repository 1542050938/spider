from bs4 import BeautifulSoup

html = '''
<head>
    <meta charset="UTF-8">
    <title>bobby基本信息</title>
    <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
</head>
<body>
    <div id="info">
        <p style="color: blue">讲师信息</p>
        <div  class="teacher_info info">
            python全栈工程师，7年工作经验，喜欢钻研python技术，对爬虫、
            web开发以及机器学习有浓厚的兴趣，关注前沿技术以及发展趋势。
            <p class="age">年龄: 29</p>
            <p class="name bobbyname" data-bind="bobby bobby2">姓名: bobby</p>
            <p class="work_years">工作年限: 7年</p>
            <p class="position">职位: python开发工程师</p>
        </div>
        <p style="color: aquamarine">课程信息</p>
        <table class="courses">
          <tr>
            <th>课程名</th>
            <th>讲师</th>
            <th>地址</th>
          </tr>
          <tr>
            <td>django打造在线教育</td>
            <td>bobby</td>
            <td><a href="https://coding.imooc.com/class/78.html">访问</a></td>
          </tr>
          <tr>
            <td>python高级编程</td>
            <td>bobby</td>
            <td><a href="https://coding.imooc.com/class/200.html">访问</a></td>
          </tr>
          <tr>
            <td>scrapy分布式爬虫</td>
            <td>bobby</td>
            <td><a href="https://coding.imooc.com/class/92.html">访问</a></td>
          </tr>
          <tr>
            <td>django rest framework打造生鲜电商</td>
            <td>bobby</td>
            <td><a href="https://coding.imooc.com/class/131.html">访问</a></td>
          </tr>
          <tr>
            <td>tornado从入门到精通</td>
            <td>bobby</td>
            <td><a href="https://coding.imooc.com/class/290.html">访问</a></td>
          </tr>
        </table>
    </div>

</body>
</html>

'''
# bs = BeautifulSoup(html, "html.parser")
# 点取标签，取出的是Tag类，只能取到第一个满足要求的标签
# bs_title = bs.title
# bs_div=bs.div
# print(bs_title)
# print(bs_title.string)
# print(bs_div.string)
# print(bs_div)
import re

# find()找到满足要求的第一个元素,取得是从<div>到</div>的所有内容
# bs_div=bs.find("div")
# bs_div=bs.find("div")
# bs_div=bs.find(id="info")
# bs_div=bs.find("div",id="info")
# 按正则查找
# bs_div=bs.find("div",id=re.compile("info\d{4}"))
# 按字符内容取，取出来的是NavaigableString类型(表格的td下的一个类型)
# bs_div = bs.find(string="tornado从入门到精通")
# print(bs_div)
# 找到所有满足要求的tag，返回list
# find_all用法和find一样
# divs=bs.find_all("div")
# for div in divs:
#     print(div)


# bs_div = bs.find(id="info")
# 获取子元素
# bs_children=bs_div.contents
# 获取子元素和子元素里面的子元素
# bs_children=bs_div.descendants
# 回车换行符会被当做NavaigableString
# for child in bs_children:
#     把None过滤掉
#     if child.name:
#         print(child.name)

# 获取父元素
# parent=bs.find('p',{"class":"name"}).parent
# print(parent)
# tag_parents=bs.find('p',{"class":"name"}).parents
# for parent in tag_parents:
#     print(parent)
# pass

# 获取后面的兄弟元素，返回list
# siblings=bs.find('p',{"class":"name"}).next_siblings
# 获取前面的兄弟元素，会把div下的内容也一并获取到
# siblings=bs.find('p',{"class":"name"}).previous_siblings

# for sibling in siblings:
#     print(sibling.string)
# pass
# 不加s只获取一个，但是换行等NavaigableString也会被当做节点
# sibling=bs.find('p',{"class":"name"}).previous_sibling
# sibling=bs.find('p',{"class":"name"}).next_sibling
# print(sibling.string)

# 获取属性
# name_tag = bs.find('p', {"class": "name"})
# 获取方法和dict相同，
# name_tag['data']如果没找到的话，会抛KeyError: 'data'异常
# name_tag.get('class')则不返回内容
# 多值属性的返回list,其他返回字符串
# duoz = name_tag['class']
# danz = name_tag['data-bind']
# print(name_tag['class'])
# print(name_tag['data-bind'])
# print(name_tag.get('class'))

from scrapy import Selector

sel = Selector(text=html)

# Selector.xpath，获取的是list
# 外面是双引号的时候，里面用单引号
# extract()取到获取到的html list
# text()把html部分提取成文本
# 获取完的html第一个标签是xpath最后一个
# tag1=sel.xpath("//*[@id='info']/div/p[1]")
# tagx=sel.xpath("//*[@id='info']/div/p[1]/text()")
# tag2=sel.xpath("//*[@id='info']/div/p[1]").extract()[0]
# tag3=sel.xpath("//*[@id='info']/div/p[1]/text()").extract()[0]
# tag=sel.xpath("//div[@id='info']/div/p[1]/text()").extract()[0]
# 可配置化
# tag_text="//div[1]/div[1]/p[1]/text()"
# tag=""
# tag_text_list=sel.xpath(tag_text).extract()
# if tag_text_list:
#     tag=tag_text_list[0]
#     print(tag)

# pass
# xpath原生的@属性只能完全匹配内容，contians可以匹配包含
# last()获取最后一个，last()-1获取倒数第二个
# teacher_tag = sel.xpath("//div[@class='teacher_info info']/p").extract()[0]
# teacher_tag = sel.xpath("//div[contains(@class,'teacher_info')]/p").extract()[0]
# teacher_tag = sel.xpath("//div[contains(@class,'teacher_i')]/p[last()-1]/text()").extract()[0]
# teacher_info_class= sel.xpath("//div[contains(@class,'teacher_i')]/@class").extract()[0]
teacher_info_class= sel.xpath("//div[contains(@class,'teacher_i')]/*").extract()

# teacher_info= sel.xpath("//p[@class='age']|//p[@class='name bobbyname']").extract()


pass
