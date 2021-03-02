"""
第三题:
这道题好像没在地里看到过. 统计点击广告的数量以及最后购买的数量. given 三个 list, 包括 purchasedUser(所有购买用户id), ipaddressUser(IP地址和用户对应列表), history(浏览记录, 包括IP地址, 时间 和 商品(广告)). 应该就 split 一下, 然后提取一下所有的数据, 遍历一下 history 就好.
第三题相当于是这样
String[] purchasedUser = ["203948535", "56856", "b86785"]
String[] history = ["234.64.23.123,2018.10.3,item A",
"234.457.45.123,2018.10.3,item A",
"34.62.34.3,2018.10.3,item B"]
String[]  
]
比如 item A 有两个点击记录, 但实际上对应的 ip 地址所对应的用户 id 只有一人最终购买, 所以输出的就是这样的形式:
1 of 2 item A
给出两个pair vector
{访问者ip和对应访问网站的text}
{用户id和对应ip}
再加上购买者的id vector
返回每个网站text 所对应购买数和访问数
"""
# Time Complexity O(n)
# Space Complexity O(n)
purchasedUser = ["203948535", "56856", "b86785"]  # user id
history = ["234.457.2345.123,2018.10.3,item A",  # ip, time, item
"234.457.2345.123,2018.10.3,item A",
"234.64.23.123,2018.10.3,item B"]
ipaddressUser = ["203948535,234.457.2345.123", # user id, ip
"56856,234.457.2345.123",
"b86785,234.64.23.123"]
# for each item get num of unique visits(users) num of visits

ip_user = dict()
for pair in ipaddressUser:
    user_id, ip = pair.split(',')
    ip_user[ip] = user_id

record_user = dict()
record_cnt = dict()
for record in history:
    ip,time, item = record.split(',')
    record_user[item] = record_user.setdefault(item,set())
    record_cnt[item] = record_cnt.setdefault(item,0) # user, count
    record_user[item].add(ip_user[ip])
    record_cnt[item] += 1

for item in record_cnt.keys():
    print(f'{len(record_user[item])} of {record_cnt[item]} : {item}')


