#Given a set of time intervals in any order, 
# merge all overlapping intervals into one and output the result which should have only mutually exclusive intervals. 
# Let the intervals be represented as pairs of integers for simplicity.


# Example: For example, let the given set of intervals be {{1,3}, {2,4}, {5,7}, {6,8} }. The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1, 4}. 
# Similarly {5, 7} and {6, 8} should be merged and become {5, 8}

# Sort the intervals based on increasing order of starting times
# Use a stack. LIFO
# Push the first interval on top of the stack
# For each interval
# If the current interval doesnot overlap with the stack top, push it

def merge_intervals(intervals):

    intervals.sort(key=lambda x: x[0])

    saved_interval = intervals[0]
    print(saved_interval)

    for interval in intervals[1:]:
        #Compare interval with the second interval.
        print(interval)



    


        

print(merge_intervals([[1,2], [3,4], [5,6]]))


