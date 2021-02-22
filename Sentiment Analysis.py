# 本章涉及一个稍微深层次的分析

# 首先我们须要定义一个词的Semantic Orientation来显示它和正向情绪和负向情绪的关联度
# 我们需要了解他到底有多好又有多坏，我们需要用Pointwise Mutual Infomation来衡量
# 见PMI.png

# SO通过PMI的拓展可得
# 见SO.png

# In order to compute the probability of observing the term t and
# the probability of observing the terms t1 and t2 occurring together
# we can re-use some previous code to calculate term frequencies and term co-occurrences

# 见Pt

# This is how we can compute the probabilities:

# n_docs is the total n. of tweets
p_t = {}
p_t_com = defaultdict(lambda: defaultdict(int))

for term, n in count_stop_single.items():
    p_t[term] = n / n_docs
    for t2 in com[term]:
        p_t_com[term][t2] = com[term][t2] / n_docs

# 定义两组好坏词组

positive_vocab = [
    'good', 'nice', 'great', 'awesome', 'outstanding',
    'fantastic', 'terrific', ':)', ':-)', 'like', 'love',
    # shall we also include game-specific terms?
    # 'triumph', 'triumphal', 'triumphant', 'victory', etc.
]
negative_vocab = [
    'bad', 'terrible', 'crap', 'useless', 'hate', ':(', ':-(',
    # 'defeat', etc.
]

# 我们可对成对关键字进行pmi计算，然后进行SO值计算，来衡量

pmi = defaultdict(lambda: defaultdict(int))
for t1 in p_t:
    for t2 in com[t1]:
        denom = p_t[t1] * p_t[t2]
        pmi[t1][t2] = math.log2(p_t_com[t1][t2] / denom)

semantic_orientation = {}
for term, n in p_t.items():
    positive_assoc = sum(pmi[term][tx] for tx in positive_vocab)
    negative_assoc = sum(pmi[term][tx] for tx in negative_vocab)
    semantic_orientation[term] = positive_assoc - negative_assoc

# The Semantic Orientation of a term will have a positive (negative) value if the term is often
# associated with terms in the positive (negative) vocabulary. The value will be zero for neutral
# terms, e.g. the PMI’s for positive and negative balance out, or more likely a term is never
# observed together with other terms in the positive/negative vocabularies.

# We can print out the semantic orientation for some terms:

semantic_sorted = sorted(semantic_orientation.items(),
                         key=operator.itemgetter(1),
                         reverse=True)
top_pos = semantic_sorted[:10]
top_neg = semantic_sorted[-10:]

print(top_pos)
print(top_neg)
print("ITA v WAL: %f" % semantic_orientation['#itavwal'])
print("SCO v IRE: %f" % semantic_orientation['#scovire'])
print("ENG v FRA: %f" % semantic_orientation['#engvfra'])
print("#ITA: %f" % semantic_orientation['#ita'])
print("#FRA: %f" % semantic_orientation['#fra'])
print("#SCO: %f" % semantic_orientation['#sco'])
print("#ENG: %f" % semantic_orientation['#eng'])
print("#WAL: %f" % semantic_orientation['#wal'])
print("#IRE: %f" % semantic_orientation['#ire'])
