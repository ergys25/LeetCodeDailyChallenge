class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0

        while j < len(nums2) and i < len(nums1):
            if nums1[i] == nums2[j] and nums1[i] not in result:
                result.append(nums1[i])

            elif nums1[i] > nums2[j]:
                j += 1
            elif nums2[j] > nums1[i]:
                i += 1
            else:
                j += 1
                i += 1
        return result

        
# Space: O(n)
# Time: O(n)
