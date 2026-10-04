class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m - 1
        second = n - 1
        write = m + n - 1

        # Fill nums1 from the end so its existing values are not overwritten.
        while second >= 0:
            if first >= 0 and nums1[first] > nums2[second]:
                nums1[write] = nums1[first]
                first -= 1
            else:
                nums1[write] = nums2[second]
                second -= 1
            write -= 1