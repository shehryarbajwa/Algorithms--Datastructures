#Go through elements side by side.
#Compare first element with the second element
#If first is bigger, switch
#Keep moving on doing it for each element

#Compare elements in the array side by side and switch

# Iteration #           1       2       3       4
# # of comparisons     n-1      n-1     n-1    n-1

#Efficiency (n-1)*(n-1) = n^2 - 2n + 1
#Thus efficiency is O(n^2)

#Worst case is O(n^2)
#Average case is O(n^2)
#Best case can be O(n)
#This can be when the array is already sorted
#Or when just 1 element needs to be sorted
#Space complexity is O(1)

#Same records when he wakes up each morning
#Assuming Sam always wakes up in the same hour, use bubble sort to sort by earliest to latest

wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]

def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            #For bubble sort to work, previous should be greater than next and then we swap
            if prev <= this:
                #When this is the case that previous is smaller than next, we continue
                #And donot proceed and run the next condition of the for loop
                continue
            
            #This is where we swap
            #We put the current index value of array to be previous
            #We put index - 1, the previous value to be the current value
            #that way we swap
            l[index] = prev
            l[index - 1] = this

bubble_sort_1(wakeup_times)
print(wakeup_times[0])
print(wakeup_times[1])
print(wakeup_times[-1])