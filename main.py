class Solution:

  def threeSum(self, nums):
    # time O(N * O(twoSum))
    # memory O(N + memory O(twoSum))

    print('hello')

    self.ans = set()

    nums.sort()

    for i in range(len(nums)):
      target = -nums[i]
      firstIndex = i + 1
      self.twoSum(nums, firstIndex, target)

    return self.ans

  def twoSum(self, nums, firstIndex, target):
    # time O(N)
    # memory O(N)

    # a + b = target
    # a = target - b
    # { a }
    seen = set()

    for i in range(firstIndex, len(nums)):
      diff = target - nums[i]

      if diff in seen:
        print('found solution', target, nums[i], diff)
        self.ans.add((target, nums[i], diff))

      seen.add(nums[i])


my = Solution()

# find all a+b+c = 0
n = [-1, 0, 1, 2, -1, -4]

ansTrue = [[-1, -1, 2], [-1, 0, 1]]

ans = my.threeSum(n)

print('ANS: ', ans, ans == ansTrue)
'''
-----------------------------
a + b + c = 0

a + b = -c

twoSum: a + b = target
'''
# find all a+b+c = 0
