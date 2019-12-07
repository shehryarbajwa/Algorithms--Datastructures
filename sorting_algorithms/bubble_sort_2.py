###Problem 2
###Sam doesnt always go to sleep in the same hour. 
# Given the following times Sam has gone to sleep, sort the times from latest to earliest

sleep_times= [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def bubble_sort_2(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this_hour, this_min = l[index]
            prev_hour, prev_min = l[index - 1]

            #If previous hour is greater than this_hour, we break the loop and move to next iteration
            #Since we are sorting by latest to earliest
            #If previous hour and this hour are the same
            #and prev minute is greater than this min
            #e.g 23.11 > 23.05 then we break the loop 
            #Since they are already sorted
            if prev_hour > this_hour or (prev_hour == this_hour and prev_min > this_min):
                continue
            
            #Swap values
            #e.g 23.01, 24.05
            #l[index] = 24.05
            #l[index-1]= 23.01
            l[index] = (prev_hour, prev_min)
            l[index - 1] = (this_hour, this_min)

bubble_sort_2(sleep_times)

print(sleep_times[0])
print(sleep_times[1])
print(sleep_times[2])
print(sleep_times[3])
print(sleep_times[4])