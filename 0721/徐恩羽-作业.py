import re
#定义空字典
zd={}
#构造函数
def word_statistics(text):
    #利用正则表达式查找单词
    result = re.findall(r"\w+",text.lower())# .lower转小写
    #遍历列表，根据单词出现次数写入字典
    for word in result:
        zd[word] = zd.get(word,0)+1
    #找到出现次数大于等于2的单词输出
    a={x:y for x,y in zd.items() if y>=2}
    print(a)
word_statistics("Python is good, Python is easy. Good code is important!")
