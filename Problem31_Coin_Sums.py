candidates = [1,2,5,10,20,50,100,200]
n = len(candidates)
target = 200
global res
res = 0
def dfs(i, curr):
    global res
    if i >= n or curr > target:
        return
    if curr == target:
        res += 1
        return
    dfs(i, curr + candidates[i])
    dfs(i+1, curr)

dfs(0, 0)
print(res)