class Solution:
    def merge(self, intervals):
        # Step 1: Sort intervals by starting time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If merged is empty or there's no overlap, just append
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap: update the end of the last interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
