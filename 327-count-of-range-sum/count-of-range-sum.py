class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        sums = [0]
        s = 0

        for num in nums:
            s += num
            sums.append(s)

        def merge_sort(left, right):
            if right - left <= 1:
                return 0

            mid = (left + right) // 2
            count = merge_sort(left, mid)
            count += merge_sort(mid, right)

            j = k = mid

            for i in range(left, mid):
                while j < right and sums[j] - sums[i] < lower:
                    j += 1

                while k < right and sums[k] - sums[i] <= upper:
                    k += 1

                count += k - j

            sums[left:right] = sorted(sums[left:right])

            return count

        return merge_sort(0, len(sums))