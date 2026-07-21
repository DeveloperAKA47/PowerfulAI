# 编写函数：函数接收一段英文文本，统计每个单词出现的次数。
# 1. 不区分大小写，`Python` 和 `python` 视为同一个单词。
# 2. 忽略以下标点符号：, . ! ? : ;
# 3. 使用字典保存统计结果。
# 4. 返回结果中只保留出现次数大于等于2次的单词。
# 5. 空字符串或只包含空格时，返回空字典。
# 6. 不允许使用第三方模块。

import re
#定义一个文本
text = "Python is good, Python is easy. Good code is important!"
#定义空字典，用来存放遍历的text字符串
counts = {}
#构造函数
def word_statistics(text):
    #将text全部转小写，然后从字符串开头匹配
    result = re.findall(r'\w+', text.lower())
    #for循环遍历，统计单词出现次数
    for word in result:
        counts[word] = counts.get(word, 0) + 1
    #定义一个空字典，用来存放次数>2的单词
    dict = {}
    # 筛选次数>=2的单词，生成结果放入字典
    for word,count in counts.items():
        if count >= 2:
            dict[word] = count
    return dict
#测试
if __name__ == '__main__':
    print(word_statistics(text))




