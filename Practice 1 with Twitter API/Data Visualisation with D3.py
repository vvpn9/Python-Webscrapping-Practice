# 这里摘录一些基础的数据可视化代码和想法
# 随后可能会有自己/学校的补充

# 使用D3.js进行可视化工作（完全没有接触过）
# 后续将尝试R语言进行可视化工作
# 实际运用中可能R在实际情况中运用不多
# 如果要做成产品可能需要运用大家都有的工具

# 如果没有vincent，则安装
# pip3 install vincent

# 从上一章 Co-Occurrence 继续

import vincent

word_freq = count_terms_only.most_common(20)  # 这是什么type的文件 需要弄清楚
labels, freq = zip(*word_freq)
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx='x')
bar.to_json('term_freq.json')

# 也可以用如下命令直接生成html文件
bar.to_json('term_freq.json', html_out=True, html_path='chart.html')

# At this point, the file term_freq.json will contain a description
# of the plot that can be handed over to D3.js and Vega

# 此处将一段代码保存为chart.html
# 然后启动Python web server

# python -m http.server 8888 # Python 3
# 然后login到http://localhost:8888/chart.html看图

# 安装pandas
# pip3 install pandas

import pandas
import json

dates_ITAvWAL = []  # 意大利对阵威尔士
# f是json文件中的指针
for line in f:
    tweet = json.loads(line)
    # 关注#开头的关键词
    terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#')]
    # 抓取#开头的关键词发出时间
    if '#itavwal' in terms_hash:
        dates_ITAvWAL.append(tweet['created_at'])
    # 此处可以用在股票信息抓取
    # 同时匹配股价变化

# 创建一个只含有1的list来计数
ones = [1] * len(dates_ITAvWAL)
# Series的index
idx = pandas.DatetimeIndex(dates_ITAvWAL)
# 实际Series
ITAvWAL = pandas.Series(ones, index=idx)

# Resampling / bucketing
per_minute = ITAvWAL.resample('1Min', how='sum').fillna(0)

# 最后一行给予我们计频的能力
# The series is re-sampled with intervals of 1 minute
# 这奖导致在同一份中内的推特信息将在这一分钟内相叠加，见how='sum'
# 如果在一分钟内没有推特的话 讲用fillna填写为0

# 以下代码可以在Vincent下构建时间序列图
time_chart = vincent.Line(ITAvWAL)
time_chart.axis_titles(x='Time', y='Freq')
time_chart.to_json('time_chart.json')

# 除开在同一时间观察一个序列
# 我们可以在同一时间观察多个对象并作图（在同一画幅上）

# 同时观测三组数据
match_data = dict(ITAvWAL=per_minute_i, SCOvIRE=per_minute_s, ENGvFRA=per_minute_e)
# 利用Pandas中的Dataframe来储存多个时间序列
all_matches = pandas.DataFrame(data=match_data,
                               index=per_minute_i.index)
# 对以上序列进行Resample
all_matches = all_matches.resample('1Min', how='sum').fillna(0)

# 作图
time_chart = vincent.Line(all_matches[['ITAvWAL', 'SCOvIRE', 'ENGvFRA']])
time_chart.axis_titles(x='Time', y='Freq')
time_chart.legend(title='Matches')
time_chart.to_json('time_chart.json')
