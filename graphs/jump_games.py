def jump_games(array, start):
    seen = set()
    return dfs(array, start, seen)

def dfs(array, idx, seen):

    if idx < 0 or idx >= len(array) or idx in seen:
        return False

    if array[idx] == 0:
        return True
    seen.add(idx)
    return dfs(array, idx + array[idx], seen) or dfs(array, idx - array[idx], seen)
