# 在取得数据和粗略文字处理推特数据之后我们讲进行一些频率分析

# 我们首先可以制作一个自己需要的词法分析器，类似于Text Processing里头的简版

# import operator
import json
from collections import Counter

fname = 'mytweets.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_all = [term for term in preprocess(tweet['text'])]  # 参照上一章preprocess
        # 如果我们制作了自己的list则可以用如下表达式

        # terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]

        # Update the counter
        count_all.update(terms_all)
    # Print the first 5 most frequent words
    print(count_all.most_common(5))

# 在每一种语言中有些词非常普遍但却没有实际意义
# 我们可以自己制作一个包含这些词的list，也可以从NLTK中找到包含英语的list

# 实际应用中仍有不包含在标准库里头的无意义词比如"转发"，"转"等
from nltk.corpus import stopwords
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']

# 如此这般我们可以获得更有意义的关键词

# 更多过滤条件
# 查看关键词类别总量
terms_single = set(terms_all)

# 查看所有#开头的关键词
terms_hash = [term for term in preprocess(tweet['text'])
              if term.startswith('#')]

# 查看所有不含有#和@开头的关键词
terms_only = [term for term in preprocess(tweet['text'])
              if term not in stop and
              not term.startswith(('#', '@'))]

# from nltk import bigrams
#
# term_bigram = bigrams(terms_stop)
# 暂时没有找到bigram的作用故不做实验和跟进

# bigrams可以用来查找相关性比较高的关键词（成对出现）
