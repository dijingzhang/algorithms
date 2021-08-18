# Permutation ([1, 2] != [2, 1])
def permute(nums):
    if not nums:
        return []

    permutations = []
    visited = set()
    permutation_dfs(nums, [], permutations, visited)
    return permutations

def permutation_dfs(nums, permutation, permutations, visited):
    if len(nums) == len(permutation):
        permutations.append(list(permutation))

    for num in nums:
        if num in visited:
            continue
        visited.add(num)
        permutation.append(num)
        permutation_dfs(nums, permutation, permutations, visited)
        visited.remove(num)
        permutation.pop()

# Combination ([1, 2] = [2, 1])
def combine(nums):
    combinations = []
    nums.sort()
    combination_dfs(nums, 0, [], combinations)

def combination_dfs(nums, k, combination, combinations):
    combinations.append(list(combinations))
    for i in range(k, len(nums)):
        if i != k and nums[i - 1] == nums[i]:
            continue
        combination.append(nums[i])
        combination_dfs(nums, i, combination, combinations)
        del combination[-1]

