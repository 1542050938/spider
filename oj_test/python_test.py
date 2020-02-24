# from collections import defaultdict
# nums = [0, 1, 0, 3, 12, -1]
# a.remove()
# nums.sort(key=bool,reverse=True)
# print(nums)
# for i in a:
#     print(bool(i))
# i=0
# for i in range(i + 2, len(nums)):
#     print(i)
# 问题：
# sorted 按dict值进行排序怎么写,labda表达式
# for item in dict_num:
# 怎样找item.key
# 怎样找item.value
# 或者根据下标查找key和value

# mat = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
# k = 3
# arr= [1,2,3,4,5,6,7,8,9,10]
# lenth = len(arr)
# num_dict = {}
# for i in range(lenth):
#     if arr[i] in num_dict:
#         num_dict[arr[i]] = num_dict[arr[i]] + 1
#     else:
#         num_dict[arr[i]] = 1
# new_num_list = []
# lenth_new_dict = len(num_dict)
# for i in num_dict:
#     new_num_list.append(num_dict[i])
#
# new_list = sorted(new_num_list, reverse=True)
# sum = 0
# lenth_list = len(new_list)
# lenth_w = (lenth / 2)
# num = 1
# for i in range(lenth_list):
#     sum += new_list[i]
#     if sum >= lenth_w:
#         num = i + 1
#         break
# return num
# nums = [3, 2, 1, 5, 6, 4]

# nums=[2,0,2,1,1,0]
# nums=[1,2,3,4,5]
# nums=[5,4,3,2,1]
# nums = [0, 1, 2, 0, 1, 12]
# def quicksort(nums,l,r):
#     # index默认设置为l
#     # [l,l)为当前小于index_num的区间，(r,r]为当前大于等于index_num的区间
#     if l<r:
#         index_num = nums[l]
#         start_l=l
#         start_r=r
#         # print(l,r)
#         while (l < r):
#             # print(nums)
#             while nums[r] >= index_num  and l < r:
#                 r -= 1
#             nums[l] = nums[r]
#             while nums[l] < index_num and l < r:
#                 l += 1
#             nums[r] = nums[l]
#
#         nums[l] = index_num
#         quicksort(nums,start_l,l-1)
#         quicksort(nums,l+1,start_r)
# def quick_sort_3(nums, l, r):
#     if l<r:
#         # [l+1,lt]<v, [lt+1,i)==v, [gt,r]>v,v为选取的基准值
#         lt = l
#         gt = r + 1
#         i = l + 1
#         v = nums[l]
#         while (i < gt):
#             if nums[i] > v:
#                 nums[i], nums[gt - 1] = nums[gt - 1], nums[i]
#                 gt -= 1
#             elif nums[i] == v:
#                 i += 1
#             elif nums[i] < v:
#                 nums[lt+1], nums[i] = nums[i], nums[lt+1]
#                 lt += 1
#                 i += 1
#         nums[l], nums[lt] = nums[lt], nums[l]
#         quick_sort_3(nums, l, lt - 1)
#         quick_sort_3(nums, gt, r)
#         return nums
# k = 2


# import random
# def quicksort(nums, l, r):
#     if l < r:
#         start_l = l
#         start_r = r
#         pivot_index = random.randint(l,r)
#         nums[l], nums[pivot_index] = nums[pivot_index], nums[l]
#         index = nums[l]
#         print(l,r)
#         while (l < r):
#
#             while (nums[r] <= index and l < r):
#                 r -= 1
#             nums[l] = nums[r]
#             while (nums[l] > index and l < r):
#                 l += 1
#             nums[r] = nums[l]
#         nums[l] = index
#         print(nums)
#         if l < (k - 1):
#             quicksort(nums, l + 1, start_r)
#         elif l > (k - 1):
#             quicksort(nums, start_l, l - 1)

# numbers=[2,7,11,15]
# target=9
# def ef(l, r, key):
#     while (l < r):
#         index = int(l + (l + r) / 2)
#         if numbers[index] == key:
#             return index
#         elif numbers[index] < key:
#             l = index + 1
#         elif numbers[index] > key:
#             r = index - 1
#     if l == r and (numbers[l] == key):
#         return l
#     else:
#         return -1
# def isPalindrome(s: str):


# 思路：双指针，排除非数字和字母的组合，进行比较
# 一：
# lenth_str = len(s)
# if lenth_str == 0:
#     return True
# i = 0
# j = lenth_str - 1
# # is_palindrome=True
# while (i < j):
#     # while (i < j and not (
#     #         (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= '0' and s[i] <= '9'))):
#     while (i < j and not s[i].isalnum()):
#         i += 1
#     # while (i < j and not (
#     #         (s[j] >= 'a' and s[j] <= 'z') or (s[j] >= 'A' and s[j] <= 'Z') or (s[j] >= '0' and s[j] <= '9'))):
#         j -= 1
#     if i < j:
#         # char_i = s[i]
#         # char_j = s[j]
#         # if (char_i >= 'a' and char_i <= 'z'):
#         #     char_i =
#         # if (char_j >= 'a' and char_j <= 'z'):
#         #     char_j = chr(ord(char_j) - 32)
#         if s[i].upper() != s[j].upper():
#             return False
#         i += 1
#         j -= 1
# return True
# s = [*filter(str.isalnum, s.lower())]
# return s == s[::-1]

# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         # [i,j]为筛选区间，区间长度为p
#         num_list = []
#         i = 0
#         lenth_s = len(s)
#         lenth_p = len(p)
#         p = sorted(p)
#         j = lenth_p - 1
#         while (j < lenth_s):
#             test = s[i:j]
#             test = sorted(test)
#             if test == p:
#                 num_list.append(i)
#             i += 1
#             j += 1
#
#
# def minSubArrayLen(s, nums):
#     # lenth 为最后一个数字的坐标
#
#     lenth = len(nums) - 1
#     if lenth >= 0:
#     # [i,j)为sum>=s的区间
#         i = 0
#         j = 0
#         sum = 0
#         min_num = lenth + 2
#         while (i <= lenth):
#             if (sum < s):
#                 if j > lenth:
#                     break
#                 sum += nums[j]
#                 j += 1
#
#             elif (sum >= s):
#                 min_num = min(j - i, min_num)
#                 sum -= nums[i]
#                 i += 1
#
#         return min_num
#     return 0
# def findAnagrams(s, p):
#     # [i,j]为筛选区间，区间长度为p
#     num_list = []
#     i = 0
#     lenth_s = len(s)
#     lenth_p = len(p)
#     p = sorted(p)
#     j = lenth_p - 1
#     while (j < lenth_s):
#         test = s[i:j+1]
#         test = sorted(test)
#         if test == p:
#             num_list.append(i)
#         i += 1
#         j += 1
#     return num_list

# def findAnagrams(s, p):
#     num_list = []
#     i = 0
#     lenth_s = len(s)
#     lenth_p = len(p)
#     dict_p = {}
#     for v in p:
#         if v in dict_p:
#             dict_p[v] += 1
#         else:
#             dict_p[v] = 1
#     j = 0
#     dict_s = {}
#     num = 0
#     # [1,j)为筛选区间
#     while (j<lenth_s):
#         if s[j] in p:
#             if s[j] in dict_s:
#                 dict_s[s[j]] += 1
#
#             else:
#                 dict_s[s[j]] = 1
#             j += 1
#             num += 1
#         else:
#             i = j + 1
#             j = i
#             dict_s = {}
#             num = 0
#
#         if (num ==lenth_p):
#             # print(dict_s,dict_p,i,j,num,lenth_p)
#             if dict_p==dict_s:
#                 num_list.append(i)
#             # print(i,j,s[i],dict_s,num)
#             if dict_s[s[i]] > 1:
#                 dict_s[s[i]] -= 1
#             else:
#                 dict_s.pop(s[i])
#             i += 1
#             num -= 1
#
#     return num_list

# def minWindow(s, t):
#     lenth_s, lenth_t = len(s), len(t)
#     dict_t = {}
#     dict_s = {}
#     for k in t: dict_t[k] = dict_t.get(k, 0) + 1
#     # [i,j)为符合要求的空间
#     i = j = 0
#     frist_list = []
#     min_lenth = lenth_s + 1
#     min_i = 0
#     min_j = 0
#     num = 0
#     while (j < lenth_s):
#         if s[j] in t:
#             dict_s[s[j]] = dict_s.get(s[j], 0) + 1
#             num += 1
#             frist_list.append(j)
#             if num >= lenth_t:
#                 has = True
#                 while(has):
#                     for i in dict_t:
#                         if (i not in dict_s) or (dict_s[i] < dict_t[i]):
#                             has = False
#                             break
#                     if has:
#                         i = frist_list.pop(0)
#                         if (j - i + 1) < min_lenth:
#                             # print(dict_s,dict_t,i,j,min_lenth,j-i)
#                             min_lenth = j - i + 1
#                             min_i = i
#                             min_j = j
#                         dict_s[s[i]] -= 1
#                         num -= 1
#
#         j += 1
#
#     if min_lenth == lenth_s + 1:
#         return ""
#     return s[min_i:min_j + 1]
# def minWindow(s, t):
#     if (not s) or (not t):
#         return ""
#     lenth_s = len(s)
#     dict_t = {}
#     dict_s = {}
#     for k in t: dict_t[k] = dict_t.get(k, 0) + 1
#     lenth_t=len(dict_t)
#     # [i,j)为符合要求的空间
#     i = j = 0
#     frist_list = []
#     min_lenth = lenth_s + 1
#     min_i = 0
#     min_j = 0
#     num = 0
#     while (j < lenth_s):
#         if s[j] in t:
#             dict_s[s[j]] = dict_s.get(s[j], 0) + 1
#             if dict_s[s[j]]==dict_t[s[j]]:
#                 num += 1
#             frist_list.append(j)
#         j += 1
#
#         while (i<j and num >= lenth_t):
#             i = frist_list.pop(0)
#             if (j - i ) < min_lenth:
#                 # print(dict_s,dict_t,i,j,min_lenth,j-i)
#                 min_lenth = j - i
#                 min_i = i
#                 min_j = j-1
#             dict_s[s[i]] -= 1
#             if dict_s[s[i]]<dict_t[s[i]]:
#                 num -= 1
#
#
#
#     if min_lenth == lenth_s + 1:
#         return ""
#     return s[min_i:min_j + 1]

# def intersect( nums1, nums2) :
# 方法一：哈希
# num_dict={}
# num_list=[]
# for i in nums1:
#     num_dict[i]=num_dict.get(i,0)+1
# for j in nums2:
#     if j in num_dict and num_dict[j]>0:
#         num_list.append(j)
#         num_dict[j]-=1
# return num_list
# 方法二：双指针
# nums1.sort()
# nums2.sort()
# lenth1=len(nums1)
# lenth2=len(nums2)
# num_list=[]
# i=0
# j=0
# while(i<lenth1 and j<lenth2):
#     if nums1[i]<nums2[j]:
#         i+=1
#     elif nums1[i]==nums2[j]:
#         num_list.append(nums1[i])
#         i+=1
#         j+=1
#     else:
#         j+=1
# return num_list
# 方法三：二分查找
# def binary_search(num1,l,r,key):
#     while(l<=r):
#         mid=l+int((r-l)/2)
#         if nums1[mid]==key:
#             num1.pop(mid)
#             return True
#         elif nums1[mid]<key:
#             l=mid+1
#         else:
#             r=mid-1
#     return False
# nums1.sort()
# nums2.sort()
# num_list=[]
# for i in nums2:
#    if binary_search(nums1,0,len(nums1)-1,i):
#        num_list.append(i)
# return num_list

from collections import Counter

# def wordPattern(pattern: str, str: str) -> bool:
#     list_pattern = list(Counter(pattern).values())
#     list_pattern.sort()
#
#     list_num_str = str.split(' ')
#     list_str = list(Counter(list_num_str).values())
#     list_str.sort()
#     return list_pattern==list_str
#
#         # list_pattern == list_num_str
# def wordPattern(pattern: str, str: str) -> bool:
#     dict_bij1 = {}
#     dict_bij2 = {}
#     list_str = str.split(' ')
#     lenth = len(pattern)
#     if lenth != len(list_str):
#         return False
#     else:
#         for i in range(lenth):
#             if pattern[i] in dict_bij1:
#                 print(pattern[i], str[i])
#                 if dict_bij1[pattern[i]] != list_str[i]:
#                     return False
#             else:
#                 dict_bij1[pattern[i]] = list_str[i]
#         for i in range(lenth):
#             if list_str[i] in dict_bij2:
#                 print(pattern[i], str[i])
#                 if dict_bij2[list_str[i]] != pattern[i]:
#                     return False
#             else:
#                 dict_bij2[list_str[i]] = pattern[i]
#         return True
# def frequencySort(s: str) -> str:
#     counter_s = Counter(s).most_common()
#     x=""
#     for i in counter_s:
#         x=x.join(i[0]*i[1])
# def fourSum(nums, target):
#     ans_set = set([])
#     nums.sort()
#     lenth = len(nums)
#     # 起始条件：len>=4
#     if lenth < 4:
#         return []
#     for i in range(lenth):
#         if i == 0 or i > 0 and nums[i] != nums[i - 1]:
#             if i + 1 < lenth and ((nums[i] + 3 * nums[i + 1]) > target):
#                 break
#             if (nums[i] + 3 * nums[-1]) < target:
#                 continue
#             # 判断边界
#             # 去重：相邻两个不相等
#             for j in range(i + 1, lenth):
#                 if (j == i + 1 or j > i + 1 and nums[j] != nums[j - 1]):
#
#                     if j + 1 < lenth and ((nums[j] + 2 * nums[j + 1]) < (target - nums[i])):
#                         break
#                     if (nums[j] + 2 * nums[-1]) < (target - nums[i]):
#                         continue
#                     # 判断边界
#                     # 去重：相邻两个不相等
#                     # [l,r]是查找区间
#                     tag = target - nums[i] - nums[j]
#                     l = j + 1
#                     r = lenth - 1
#                     while (l < r):
#                         if nums[l] + nums[r] < tag:
#                             l += 1
#                         elif nums[l] + nums[r] == tag:
#                             ans_set.add((nums[i], nums[j], nums[l], nums[r]))
#                             l += 1
#                         else:
#                             r -= 1
#     return list(ans_set)
# def checkIfExist(arr):
#     lenth=len(arr)
#     for i in range(lenth):
#         for j in range(lenth):
#             if i!=j and 2*arr[i]==arr[j] or 2*arr[j]==arr[i]:
#                 return True
#     return False

# from collections import defaultdict


# def groupAnagrams( strs):
#     lenth = len(strs)
#     dict_str = defaultdict(list)
#     for i in strs:
#         j = str(sorted(i))
#         dict_str[j].append(i)
#     return [v for k, v in dict_str.items()]
# def numberOfBoomerangs( points):
#     lenth = len(points)
#     num = 0
#     dict_point = defaultdict(int)
#     for a, b in points:
#         for c, d in points:
#             if a != c or b != d:
#                 dist = (a - c) * (a - c) + (b - d) * (b - d)
#                 dict_point[dist] += 1
#         for i in dict_point:
#             num += (dict_point[i] * (dict_point[i] - 1))
#     return num\
# def gcd(x, y):
#     while (y != 0):
#         mon = x % y
#         x = y
#         y = mon
#     return x


# def maxPoints(points):
#
#
#     if points == []:
#         return 0
#     # points=Counter(points)
#     max_point = 0
#     for i in points:
#         num = 0
#         xlv_dict = defaultdict(int)
#         a ,b = i[0], i[1]
#         for j in points:
#             # if i != j:
#                 c,d = j[0],j[1]
#                 if a == c and b == d:
#                     num += 1
#                     if num > max_point:
#                         max_point = num
#                     continue
#                 if a == c and b != d:
#                     gcd_x = 0
#                     gcd_y = 1
#                 else:
#                     xlv = gcd(c - a, d - b)
#                     gcd_x = (c - a) / xlv
#                     gcd_y = (d - b) / xlv
#                 xlv_dict[(gcd_x, gcd_y)] += 1
#                 if xlv_dict[(gcd_x, gcd_y)] + num > max_point:
#                     max_point = xlv_dict[(gcd_x, gcd_y)] + num
#     return max_point
# def maxPoints(points):
#     if points == []:
#         return 0
#     max_point = 0
#     dict_points = (tuple(a) for a in points)
#     dict_point = Counter(dict_points)
#     dict_key =tuple(dict_point.keys())
#     lenth = len(dict_key)
#     if lenth == 1:
#         return dict_point[dict_key[0]]
#     for i in range(lenth):
#         x1, y1 = dict_key[i][0], dict_key[i][1]
#         xlv_dict = defaultdict(int)
#         for j in range(i + 1, lenth):
#             x2, y2 = dict_key[j][0], dict_key[j][1]
#             dx = x2 - x1
#             dy = y2 - y1
#             if dx != 0:
#                 gcd_value = gcd(dx, dy)
#                 dx //= gcd_value
#                 dy //= gcd_value
#             else:
#                 dy = 1
#             xlv_dict[(dy, dx)] += dict_point[dict_key[j]]
#             max_point = max(max_point, xlv_dict[(dy, dx)] + dict_point[dict_key[i]])
#     return max_point
from collections import defaultdict


# def containsNearbyAlmostDuplicate(nums, k, t):
#     lenth=len(nums)
#     for i in range(lenth):
#         for j in range(i+1,lenth):
#             if (abs(nums[i]-nums[j])<=t) and (j-i<=k):
#                 return True
#     return False
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def creat_linked_list(arr, n):
    if n == 0:
        return None
    head = ListNode(arr[0])
    cur = head
    for i in range(1, n):
        node = ListNode(arr[i])
        cur.next = node
        cur = node
    return head


def print_linked_list(head: ListNode):
    cur = head
    while (cur != None):
        print("%d -> " % cur.val, end='')
        cur = cur.next
    print("NULL")


# class Solution:
#     def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
#         # 特判
#         if m==n:
#             return head
#         # 找m点、pre_m点
#         pre_m=None
#         k=1
#         x=head
#         while(x!=None and k<=m):
#             if k==m-1:
#                 pre_m=x
#             if k==m:
#                 m_node=x
#             x=x.next
#             k+=1
#         # 翻转，因k已经到next节点了，所以需要挪回来一位
#         pre=pre_m
#         cur=m_node
#         k-=1
#         # k代表这次翻转的节点
#         while(k<=n):
#             tem=cur.next
#             cur.next=pre
#             pre=cur
#             cur=tem
#             k+=1
#         # cur指向n+1位置，pre指向n节点，
#         # 将原来的m节点的next指向cur
#         m_node.next=cur
#         # 将pre_m和指向n的节点拼接起来
#         if pre_m!=None:
#             pre_m.next=pre
#         else:
#             head=pre
#
#         return head
# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         dummy_head = ListNode(0)
#         dummy_head.next = head
#         p = dummy_head
#         cur = head
#         while (cur and cur.next):
#             left = cur
#             con = k
#             pre = None
#             while (con and cur):
#                 con -= 1
#                 nextt = cur.next
#                 cur.next = pre
#                 pre = cur
#                 cur = nextt
#             print_linked_list(dummy_head)
#             if con == 0:
#                 p.next = pre
#                 left.next = cur
#                 p = left
#                 print_linked_list(dummy_head)
#             else:
#                 # cur.next=None
#                 # cur = pre.next
#                 cur,pre=pre,cur
#                 while (cur):
#                     nextt = cur.next
#                     cur.next=pre
#                     pre = cur
#                     cur = nextt
#                 p.next = pre
#                 # print_linked_list(dummy_head)
#                 break
#         return dummy_head.next
# class Solution:
#     def pinjie(self, head, head1, head2):
#         cur = head
#         # print_linked_list(head1)
#         while (head1 or head2):
#             if head2 == None:
#                 cur.next = head1
#                 cur = cur.next
#                 head1 = head1.next
#                 continue
#             elif head1 == None:
#                 cur.next = head2
#                 cur = cur.next
#                 head2 = head2.next
#                 continue
#
#             if head1.val <= head2.val:
#                 cur.next = head1
#                 cur = cur.next
#                 head1 = head1.next
#             else:
#                 cur.next = head2
#                 cur = cur.next
#                 head2 = head2.next
#         return cur
#
#     def sortList(self, head: ListNode) -> ListNode:
#         if head == None:
#             return None
#
#         dummy_head = ListNode(0)
#         dummy_head.next = head
#         cur = head
#         lenth = 1
#         while (cur.next):
#             cur = cur.next
#             lenth += 1
#         # step,每次分割的步长
#
#         step = 1
#         # new_head是当前链表已完成排序和拼接部分的尾结点
#
#         while (step < lenth):
#             new_head = dummy_head
#             cur = new_head.next
#             while cur:
#                 # 找到第一段的头和尾部
#                 h1 = cur
#                 con = 1
#                 while (cur.next and con < step):
#                     cur = cur.next
#                     con += 1
#                 # 如果长度不够第一段，或者第二段的开头是None，那就不用拼接了
#                 if con < step or cur.next == None:
#                     break
#                 wei1 = cur
#                 cur = cur.next
#                 wei1.next = None
#                 # 找到第二段的头和尾部
#                 h2 = cur
#                 con = 1
#                 while (cur.next and con < step):
#                     cur = cur.next
#                     con += 1
#
#                 wei2 = cur
#                 cur = cur.next
#                 wei2.next = None
#                 # 拼接，并返回最后一个元素当做新的new_head
#                 new_head = self.pinjie(new_head, h1, h2)
#                 new_head.next = cur
#             step *= 2
#         return dummy_head.next

# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         if head==None or head.next==None:
#             return head
#         lenth=0
#         cur=head
#         while(cur):cur,lenth=cur.next,lenth+1
#         mid=int(lenth/2+0.5)
#         cur=head
#         while(mid>1): cur,mid=cur.next,mid-1
#         dummy_head=ListNode(0)
#         dummy_head.next=cur.next
#         cur.next=None
#         new_head=dummy_head
#         print_linked_list(head)
#         print_linked_list(new_head)
#         while(dummy_head.next):
#             nextt=head.next
#             new_cur=new_head
#             pre=new_cur
#             while(new_cur.next):
#                 pre=new_cur
#                 new_cur=new_cur.next
#             pre.next=None
#             head.next=new_cur
#             head.next.next=nextt
#             head=nextt
# class Solution:
#     def evalRPN(self, tokens) -> int:
#         num = 0
#         # stack_left=[]
#         stack = []
#         fristhead = 0
#         have_num = False
#         options = ['+', '-', '*', '/']
#         for i in tokens:
#             if i in options:
#                 x =int(stack.pop())
#                 if not have_num:
#                     fristhead = len(stack)
#                     num = int(stack.pop())
#                     have_num = True
#
#                 if len(stack) < fristhead:
#                     x, num = num, x
#                     fristhead = len(stack)
#                 if i == '/':
#                     num = int(num / x)
#                 elif i == '+':
#                     num += x
#                 elif i == '-':
#                     num -= x
#                 elif i == '*':
#                     num *= x
#             else:
#                 stack.append(i)
#         return num
class Solution:
    def isrun(self, year):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        return False

    def com(self, mon, day, run):
        la=[1,3,5,7,8,10,12]
        num = 0
        if mon in la :
            num += 31 - day + 1
            mon += 1
        else:
            if mon == 2 and run:
                num += 29 - day + 1
            elif mon == 2 and not run:
                num += 28 - day + 1
            else:
                num += 30 - day + 1
        return num

    def daysBetweenDates(self, date1: str, date2: str) -> int:

        # 分割，年份小的在前面
        date_list1 = date1.split('-')
        date_list2 = date2.split('-')
        for i in range(len(date_list1)):
            date_list1[i] = int(date_list1[i])
            date_list2[i] = int(date_list2[i])

        if date_list1[0] > date_list2[0]:
            date_list1, date_list2 = date_list2, date_list1
        elif date_list1[0] == date_list2[0] and date_list1[1] > date_list2[1]:
            date_list1, date_list2 = date_list2, date_list1
        elif date_list1[0] == date_list2[0] and date_list1[1] == date_list2[1] and date_list1[2] > date_list2[2]:
            date_list1, date_list2 = date_list2, date_list1
        num = 0
        # 年份相差大于1年时，计算整年差距
        year1 = date_list1[0]
        year2 = date_list2[0]
        run1 = self.isrun(year1)
        newyear=year1+1
        while (newyear < year2):

            if self.isrun(newyear):
                num += 366
            else:
                num += 365
            newyear += 1
        # 计算当年到年底是多少天
        mon1 = date_list1[1]
        mon2 = date_list2[1]
        day1 = date_list1[2]
        day2 = date_list2[2]
        x1 = x2 = 0
        x1 += self.com(mon1, day1, run1)
        while (mon1 < 12):
            mon1 += 1
            x1 += self.com(mon1, 1, run1)
        run2 = self.isrun(year2)
        x2 += self.com(mon2, day2, run2)
        while (mon2 < 12):
            mon2 += 1
            x2 += self.com(mon2, 1, run2)
        # 如果是同一年就相减，不再同一年就相加
        if year1 < year2:
            if run2:
                x2 = 366 - x2 + 1
            else:
                x2 = 365 - x2 + 1
            num += (x1 + x2 - 1)
        elif year1 == year2:
            num += (x1 - x2)
        return num


if __name__ == '__main__':
    # head_1 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+",""]
    s = Solution()
    # head2 = s.daysBetweenDates("2019-06-29","2019-06-30")
    # head2 = s.daysBetweenDates("2020-01-15", "2019-12-31")
    head2 = s.daysBetweenDates("1971-06-29","2010-09-23")
    # head2 = s.daysBetweenDates("1971-06-29","1972-01-01")
    # head2 = s.daysBetweenDates("2010-09-23","2011-01-01")
    print(head2)
    # print(','.join(head_1))
    # list1=[1,2,3]
    # print(list1.reverse())
    # print(list1)
    # if []:
    #     print([[]])




    # head_1 = creat_linked_list([1,2,3,4,5], 5)
    # print_linked_list(head_1)
    # s = Solution()
    # head2 = s.reorderList(head_1)
    # print_linked_list(head2)
    # print(6//(-123))
    # l1=[1]
    # l2=[]
    # x=l1 or l2
    # print(x)
    # while l2 or l1 or l2:
    #     print("hhh")
    # print(1//10)
    # print(l1.pop())
    # print(l1.pop())
    # print(containsNearbyAlmostDuplicate([1,2,3,1],3,0))
    # print(containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))
    # print(containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
    # print(containsNearbyAlmostDuplicate([], 1, 0))
    # print(containsNearbyAlmostDuplicate([1], 0, 0))
    # print(containsNearbyAlmostDuplicate([1,2,1], 1, 0))
    # print(containsNearbyAlmostDuplicate([4,1,6,3],5,1))
    # a=set()
    # print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # print(groupAnagrams(["eat","eat","eat"]))
    # print(groupAnagrams(["cac","aca","bbb","bb","cc","acc"]))
    # print(groupAnagrams([]))
    # print(numberOfBoomerangs([[0,0],[1,0],[2,0]]))
    # print(maxPoints([[1,1],[2,2],[3,3]]))
    # print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
    # print(maxPoints([[1,1],[2,2],[3,3],[2,1],[3,2]]))
    # print(maxPoints([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]))
    # print(maxPoints([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3],[4,4]]))
    # print(maxPoints([[1,1],[2,2]]))
    # print(maxPoints([[1,1]]))
    # print(maxPoints([]))
    # print(maxPoints([[1,1],[1,1]]))
    # print(maxPoints([[1,1],[1,1],[2,2],[2,2]]))
    # print(maxPoints([[0,0],[94911151,94911150],[94911152,94911151]]))
    # print(gcd(-1, 2), gcd(2, -1))
    # dict_x={1:'y',2:'x'}
    # print(sorted(dict_x.values()))
    # print(sorted(dict_x.items(),key=lambda x:x[1]))
    # print(frequencySort("tree"))
    # s="abc"
    # s=['a','b','c']
    # s=('a','b','c')
    # print(fourSum([1,0,-1,0,-2,2],0))
    # print(checkIfExist([-10,12,-20,-8,15]))
    # s={"a":1,'b':2}
    # print("-".join(i*j for i,j in s.items()))
    # print("".join("a"*2))
    # print(wordPattern("abba","dog cat cat dog"))
    # print(wordPattern("ba","cat cat"))
    # pattern = "bab"
    # print([*map(pattern.index,pattern)])
    # print(intersect([1,2,2,1],[2,2]))
    # print(intersect([4,9,5],[9,4,9,8,4]))
    # quicksort(nums, 0, len(nums) - 1)
    # x= quick_sort_3(nums, 0, len(nums) - 1)
    # lenth = len(numbers)
    # for i in range(lenth):
    #     if (numbers[i] + numbers[lenth - 1] >= target):
    #         x = ef(i, lenth, target - numbers[i])
    #         if x != -1:
    #             print(i, x)
    #             break
    # print(nums[k-1])
    # iss=isPalindrome("    ")

    # iss=isPalindrome("A man, a plan, a canal: Panama")
    # print(iss)
    # s=["1","2","3"]
    # # print(str(s))
    # print(minSubArrayLen(2, [9, 1, 4, 5]))
    # print(minSubArrayLen(3, [1,1,1,3,5]))
    # print(minSubArrayLen(3,[1,2,3,4,5]))
    # print(minSubArrayLen(100,[]))
    # dict = {"a": "apple", "b": "banana", "o": "orange"}
    # for i in dict:
    #     print(i, dict[i])

    # l = {'a': {'xx':"bb"}, 'b': 2, 'c': 3}
    # for k, v in l.items():
    #     print(k, v)
    # a_dict = {"x": '0001', "y": '002'}
    # a_dict ={'a':1,'b':2,'c':3}
    # print(list(a_dict.keys()))  # key 列表
    # print([list(a_dict.values()).index(1)])  # 对应的索引值
    # print(list(a_dict.keys())[list(a_dict.values()).index(1)])
    # print(findAnagrams("cbaebabacd","abc"))
    # a_dict ={'a': 1, 'b': 1}
    # b_dict = {'b': 1, 'a': 1}
    # print(a_dict==b_dict)
    # print(findAnagrams("cbaebabacd", "abc"))
    # print(minWindow("ADOBECODEBANC","ABC"))
    # print(minWindow("ADOBECODEBANC","ABBC"))
    # # print(minWindow("aaaaaaaaaaaabbbbbcdd","abcdd"))
    #     s = set([1, 2, 3])
    # s.add({22: 3})

    # dict没有默认值，会报错
    # dicti = {}
    # print(dicti['a'])
    # dicti['a'] = 2
    # print(dicti.get('a'))
    # print(dicti.pop('a'))
    # print(dicti.get('a',1))
    # print(dicti.setdefault('a',3))
    # print(dicti['a'])

    # defaultdict 可以设置默认值
    # from collections import defaultdict,OrderedDict,Counter
    # dicti = defaultdict(int)
    # dicti={}
    # dicti['a']='a'
    # dicti['b']='c'
    # dicti['c']='b'
    # print(dicti)
    # for i in dicti:
    #     print(i,dicti[i])
    # d1 = {'a': 'A', 'c': 'C','b': 'B', 'd': 'D'}
    # # d1['a'] = 'A'
    # # d1['b'] = 'B'
    # # d1['c'] = 'C'
    # # d1['d'] = 'D'  # 此时的d1 = {'a':'A','b':'B','c':'C','d':'D'}
    # print(d1)
    # for k, v in d1.items():
    #     print(k, v)

    # Ordereddict = OrderedDict()
    # Ordereddict["name"] = "xiejiangpeng"
    # Ordereddict["sex"] = "boy"
    # Ordereddict["age"] = "32"
    # Ordereddict["hobby"] = "eat food"
    #
    # comDict = {'name': 'xiejiangpeng',
    #            'sex': 'boy',
    #            'age': '32',
    #            'hobby': 'eat food'}
    # print(Ordereddict)
    # print(comDict)
    # dicti={'a':2,'b':3}
    # dict1=OrderedDict(dicti)
    # for i in dict1:
    #     print(i,dict1[i])

    # dict2 = defaultdict(float)
    # dict3 = defaultdict(str)
    # dict4 = defaultdict(list)
    # print('a'in dicti)
    # # print(dicti.pop('a'))
    # print(dicti['a'])
    # print('a' in dicti)
    # print(dicti.pop('a'))
    # print(dicti.pop('a',None))
    # print(dicti.pop('a',1))
    # del dicti['a']
    # print('a' in dicti)
    # dicti['a']=2
    # del dicti['a']
    # print('a' in dicti)
    # print(dicti['a']
    # l=4
    # r=5
    # mid = l + (r - l) / 2
    # print(mid)
    # print(2**4)
    # s='1008611'
    # t=Counter(s)
    # print(t)
    # print(list(t.elements()))
