"""
Given intervals, find max number of overlapping intervals
(1,2), (2,3) overlaps

The approach:
1. sort x and sort y coordinates
2. go through x coordinate

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""
def merge(intervals):
        # Sort by start time
        # go through the times
        # DOES not merge when end time of A is less than start time
        # (e.g.) (0,9) (10, 11), 9 < 10, do not overlap
        # However, if (0,9) (9,11), merge
        # merge = simplily saying (same x, new 11 (max of the two))
        # sort by order so order can be used
        intervals.sort(key=lambda x: x[0])
        merged = []
        count = 0
        for time in intervals:
            start, end = time[0], time[1]
            if not merged or merged[-1][1] < start:
                merged.append(time)
            else:
                # overlappable
                buffer = merged[-1][1]
                merged[-1][1] = max(merged[-1][1], end)
                if buffer != merged[-1][1] and start != merged[-1][0]:
                    count += 1
        print(count)
        return merged

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
