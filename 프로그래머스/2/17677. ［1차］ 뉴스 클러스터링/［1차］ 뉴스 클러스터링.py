from collections import Counter

def make_multiset(s):
    s = s.lower()
    multiset = []
    for i in range(len(s) - 1):
        pair = s[i:i+2]
        if pair.isalpha():
            multiset.append(pair)
    return Counter(multiset)

def solution(str1, str2):
    set1 = make_multiset(str1)
    set2 = make_multiset(str2)
    
    # 교집합
    inter = set1 & set2
    # 합집합
    union = set1 | set2
    
    inter_size = sum(inter.values())
    union_size = sum(union.values())
    
    # 공집합
    if union_size == 0:
        return 65536
    
    return int((inter_size / union_size) * 65536)
