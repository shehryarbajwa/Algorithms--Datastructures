import heapq
def meeting_rooms(intervals):
    if not intervals:
        return 0
    
    free_rooms = []

    heapq.heappush(free_rooms, intervals[0][1])

    for interval in intervals[1:]:
        start_time = interval[0]
        end_time = interval[1]

        if free_rooms[0] <= start_time:
            heapq.heappop(free_rooms)

        heapq.heappush(free_rooms, end_time)

    return len(free_rooms)

#Example Meeting 1 runs from 9.00 - 10.00
#Meeting II runs from 10.15 - 11.30
#We can check the root of heap and check whether 10.00 is less than 10.15
#Since it is, we pop it since now this room is available
#Then we add this interval's ending time i.e 11.30 to our rooms that it is booked till then
#If instead we have a meeting 9.00 - 10.00
#Second meeting from 9.45 - 10.30, we know that we cant accomodate this so we will add 10.30 end time to our min-heap
#In the end our min heap denotes all rooms absolutely needed to accomodate the meetings

        
        
    
    