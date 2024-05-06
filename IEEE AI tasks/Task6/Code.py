from typing import List
from itertools import accumulate
import bisect
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        sample = {idx: cnt for idx, cnt in enumerate(count) if cnt}
        maximum, minimum, maxCount = max(sample.keys()), min(sample.keys()), max(sample.values())
        totalCount, totalSum = sum(sample.values()), sum(key * value for key, value in sample.items())
        mean, median, mode, medianCtr = totalSum / totalCount, 0, 0, 0
        for num in sample:
            if sample[num] == maxCount: mode = num
        count = list(accumulate(count))
        median1 = bisect.bisect(count, (totalCount - 1) / 2)
        median2 = bisect.bisect(count, totalCount / 2)
        median = (median1 + median2) / 2.0
        return [float(minimum), float(maximum), float(mean), float(median), float(mode)]
    
    