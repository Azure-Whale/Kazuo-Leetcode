"""
第一题:
给广告在每个domain上被click的次数. 要求返回domain及其所有sub domain 被click的总次数.
leetcode811 上有原题: https://leetcode.com/problems/subdomain-visit-count/

第二题:
给每个user访问历史记录，找出两个user之间longest continuous common history.

第三题:
这道题好像没在地里看到过. 统计点击广告的数量以及最后购买的数量. given 三个 list, 包括 purchasedUser(所有购买用户id), ipaddressUser(IP地址和用户对应列表), history(浏览记录, 包括IP地址, 时间 和 商品(广告)). 应该就 split 一下, 然后提取一下所有的数据, 遍历一下 history 就好.
第三题相当于是这样
String[] purchasedUser = ["203948535", "56856", "b86785"]
String[] history = ["234.64.23.123,2018.10.3,item A",
"234.457.45.123,2018.10.3,item A",
"34.62.34.3,2018.10.3,item B"]
String[] ipaddressUser = ["203948535,234.457.2345.123",
"74545,234.457.2345.123"
"2347,234.64.23.123"
]
比如 item A 有两个点击记录, 但实际上对应的 ip 地址所对应的用户 id 只有一人最终购买, 所以输出的就是这样的形式:
1 of 2 item A
给出两个pair vector
{访问者ip和对应访问网站的text}
{用户id和对应ip}
再加上购买者的id vector
返回每个网站text 所对应购买数和访问数
"""

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # Time : O(n)  Space: O(n)
        ans = dict()
        for pair in cpdomains:
            count, visit = pair.split(' ')
            visit_histroy = visit.split('.')
            for i in range(len(visit_histroy)):
                temp_domain = '.'.join(visit_histroy[i:])
                ans[temp_domain] = ans.setdefault(temp_domain,0) + int(count)
        
        return [f'{cnt} {domain}' for domain,cnt in ans.items()]
    