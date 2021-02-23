# 推特允许用户发推特的时候连带地理坐标，我们将使用这些信息绘制地理信息图

# GeoJSON是一个储存地理信息的数据结构，这个数据结构可以储存多种信息并用来绘制地图
# 我们仅需要一个point含有经纬度信息

# 在GeoJSON中我们可以把一个对象视作一个Feature或者一个FeatureCollection
# Feature is basically a geometry with additional properties
# FeatureCollection is a list of features

# 推特数据组可以视作一个FeatureCollection，每一条推特可以是做一个连带地理信息的Feature

# 以下是一个JSON格式范本

"""
{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [some_latitude, some_longitude]
            },
            "properties": {
                "text": "This is sample a tweet",
                "created_at": "Sat Mar 21 12:30:00 +0000 2015"
            }
        },
        /* more tweets ... */
    ]
}
"""
# 假设所有数据储存在一个文件中，我们只需要iterate所有推特查找 "coordinates" 一栏

# 所有推特数据储存在 "fname"
with open(fname, 'r') as f:
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        tweet = json.loads(line)
        if tweet['coordinates']:
            geo_json_feature = {
                "type": "Feature",
                "geometry": tweet['coordinates'],
                "properties": {
                    "text": tweet['text'],
                    "created_at": tweet['created_at']
                }
            }
            geo_data['features'].append(geo_json_feature)

# Save geo data
with open('geo_data.json', 'w') as fout:
    fout.write(json.dumps(geo_data, indent=4))

# 如此这般地理位置信息已经取得

# Javascript可以用来实现python的可视化，尤其是在浏览器方面