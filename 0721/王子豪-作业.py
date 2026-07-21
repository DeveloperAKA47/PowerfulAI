import re
def word_statistics(text: str):
    answer = {}
    if not text or text.isspace():
        return answer
    else:
        a  = re.findall(r'[A-Za-z]+', text.lower())
        b = list(set(a))
        for i in b:
            if a.count(i) >= 2:
                answer[i] = a.count(i)
            else:
                pass
    for word, count in answer.items():
        print(f"{word}: {count}")
word_statistics("Python is good, Python is easy. Good code is important!")
#=========
