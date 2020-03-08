#Given an array of integers, compare whether each element is greater than the next element

#Given a set of time intervals in any order, 
# merge all overlapping intervals into one and output the result which should have only mutually exclusive intervals. 
# Let the intervals be represented as pairs of integers for simplicity.


# Example: For example, let the given set of intervals be {{1,3}, {2,4}, {5,7}, {6,8} }. The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1, 4}. 
# Similarly {5, 7} and {6, 8} should be merged and become {5, 8}

# Are all intervals sorted?
# Are all intervals in an array?
# Are all intervals with a start and end and only contains these two points?
# 



import unittest

def merge_intervals(intervals):

    intervals.sort(key=lambda x: x)

    result = [intervals[0]]

    for interval in intervals[1:]:
        interval_2 = result[-1]

        if do_overlap(interval, interval_2):
            merged_front = min(interval[0], interval_2[0])
            merged_back = max(interval[1], interval_2[1])
            result[-1] = [merged_front, merged_back]

        else:
            result.append(interval)

    return result

        
# Overlap happens when there exists an interval within an another interval
# To calculate it, we can pictorially see that by calcuating the maxiumum value of the start.
# Then calculating the minimum value of the end. If there difference is positive, that means there exists an interval between them

# e.g 1 event starts at 1 pm and ends at 4 pm.
# e.g 2nd event starts at 2 pm but ends at 3 pm.

# Intuitively, we know that 2 - 3 pm falls between the first interval.
# So we calculate the maximum value of the start. That way we know which event started later.
# Then we calculate the minimum value of the end. That way we know which event ended earliest. out of both intervals
# Taking their difference ending - starting we can find the intersection of the interval.

def do_overlap(interval1, interval2):

    start_time = max(interval1[0], interval2[0])
    end_time = min(interval1[1], interval2[1])
    return end_time - start_time >= 0



class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(merge_intervals([[1,2],[2,4]]), [[1,4]])

    def test_case_2(self):
        self.assertEqual(merge_intervals([[1,2],[3,4]]), [[1,2], [3,4]])


if __name__ == '__main__':
    unittest.main()

    