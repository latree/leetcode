# island 问题是matrix dfs 的一类
# 关于island 的题最主要的一个核心就是dfs的方向是四个方向还是八个方向。
# 如果是八个方向那么这个set还要加四个((r + 1, c + 1),(r + 1, c - 1),(r - 1, c - 1),(r - 1, c + 1))
directions = ((r + 1, c),(r - 1, c),(r, c + 1),(r, c - 1))
for nr, nc in directions:
    # 通常还需要有额外的限制条件比如 if (r, c) not in seen and grid[r][c] == 1
    if 0 <= nr < m and 0 <= nc < n:
        res += dfs(nr, nc)

# example question:
# 695. Max Area of Island
# 827	Making A Large Island
