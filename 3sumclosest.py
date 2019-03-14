class Solution:
    def threesumclosest(self, num, target):
        if len(num) < 3:
            return 0
        num.sort()
        error = float("infinity")
        for i in range(0, len(num)-2):
            begin = i+1
            end = len(num)-1
            while begin < end:
                if abs(num[i] + num[begin] + num[end] - target) < error:
                    error = abs(num[i] + num[begin] + num[end] - target)
                    solution = num[i] + num[begin] + num[end]

                if num[i] + num[begin] + num[end] > target:
                    end -= 1
                else:
                    begin += 1

        return solution


if __name__ == "__main__":
    num = [-1, 2, 1, 4]
    print(Solution().threesumclosest(num, 2))

