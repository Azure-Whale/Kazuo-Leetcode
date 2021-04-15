# This is a variation of https://leetcode.com/problems/merge-k-sorted-lists/

given_list = [1,2,3,'13',5,6,'10',7,8,11,12]  # get an ascending list with O < O(nlogn)
import heapq # use it to implement a priority queue
def solution(given_list): #O(Nlogk) # k the number of changed number
    # Key:
    # it's just a sort, but the time complexity could be reduced into logk since most of them are sorted using PQ
    # first, split thte list into K+1 lists, where there is one sorted list
    # then do the jobs same as https://leetcode.com/problems/merge-k-sorted-lists/
    # use pq to store the smallest element of each nodes
    # could also be solved by Divide And Conquer
    temp = []
    sorted_temp = []
    for ele in given_list:
        
        if type(ele) != int:
            heapq.heappush(temp,int(ele))
        else:
            sorted_temp.append(ele)
    ans = []
    for ele in sorted_temp:
        if temp and temp[0]<=ele:
            ans.append(heapq.heappop(temp))
        else:
            ans.append(ele)
    while temp:
        ans.append(heapq.heappop(temp))
    print(ans)
solution(given_list)