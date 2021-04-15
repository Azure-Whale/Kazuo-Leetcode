from typing import Collection


from collections import defaultdict
test_case_1 = 'bdsajbfodbogbvpgrpgprghprg'
ans = defaultdict(int)
for alpha in test_case_1:
    ans[alpha] += 1
print(ans)