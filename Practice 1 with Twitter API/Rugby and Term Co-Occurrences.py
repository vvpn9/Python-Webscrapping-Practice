# 这部分侧重于数据的持续收集和相关性研究

# 以博客博主橄榄球比赛数据为例子
# 关键词有时候不是单独出现，以比赛为例常有对手成对出现等等

# 我们创建包含计数的Co-occurrence矩阵

from collections import defaultdict

# Todo: remember to include the other import from the previous post

com = defaultdict(lambda: defaultdict(int))

# f是json文件中的指针
for line in f:
    tweet = json.loads(line)
    terms_only = [term for term in preprocess(tweet['text'])
                  if term not in stop  # stop是创建的语义停止词list（无意义过滤）
                  and not term.startswith(('#', '@'))]

    # 创建相关性矩阵
    for i in range(len(terms_only) - 1):
        for j in range(i + 1, len(terms_only)):
            w1, w2 = sorted([terms_only[i], terms_only[j]])
            if w1 != w2:
                com[w1][w2] += 1

# 确保二元因子矩阵中顺序无关，所以inner loop使用i+1构建三角矩阵

# 对于每个关键词组（二元矩阵）我们获取频次最高的前五组

com_max = []
for t1 in com:
    t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
    for t2, t2_count in t1_max_terms:
        com_max.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
print(terms_max[:5])

# 对于特定关键字的检索，我们可以找出与之成对出现的最高次数的词组（词）
# 运用scipy中的sparse

# Todo: 下列一行有歧义，仍需要时间去理解和消化
search_word = sys.argv[1]  # 传递一个关键字作为系统级命令
count_search = Counter()
for line in f:
    tweet = json.loads(line)
    terms_only = [term for term in preprocess(tweet['text'])
                  if term not in stop
                  and not term.startswith(('#', '@'))]
    if search_word in terms_only:
        count_search.update(terms_only)
print("Co-occurrence for %s:" % search_word)  # string method
print(count_search.most_common(20))
