class Solution(object):
    def merge(self, intervals):
        
        intervals.sort()

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            last_merged = merged[-1]
            current = intervals[i]

            if current[0] <= last_merged[1]:
                last_merged[1] = max(current[1], last_merged[1])
            else:
                merged.append(current)
            
        return merged
    
s = Solution()

intervals = [[1,4],[2,6],[5,10],[15,20],[16,18]]

print(s.merge(intervals))
        