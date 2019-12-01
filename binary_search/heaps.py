## Heaps are elements arranged in increasing or decreasing order
## Max is where the parent must have a value greater than the child
## Min is where the parent must have a value less than the child

#Input data: 4, 10, 3, 5, 1
         #10(0)
        /  \
     #5(1)  3(2)
    /   \
 #4(3)    1(4)

#The above is a max heap where parent 10 is greater than its children i.e 5 and 3
#4 and 1 are greater than 5

#Min heap
        #2(0)
        /  \
     #3(1)  4(2)
    /   \
 #4(3)    5(4)

#Above is a min heap

#Since heaps are not binary trees, the peek is the parent root i.e 2 and 10 in min max
#A heap is complete when all levels except the last one are completely full
#In our examples above both 3 and 4 and 5 and 3 are full
#If the level isnt totally full, we add elements from the left to right

#The Big(O) notation for search in a min max heap tree is O(n)
#For example we will take the search of 1 in our max heap
#Worst case, we will have to traverse left and right of 10
#That is 2 steps
#Then we traverse left and right of 5 that is 2 steps until we hit 1
#In the worst case getting to 1 will take 5 steps. However, it can be done in 4
#O(n) 4/5 n is still 0.8 n which is O(n) to be approximate
#However, in the best case, we can also have it to be O(n/2). If we know the target is 6
#Then we start at 10, we traverse down
#We have 5 and 3
#We know 6 > 5 and 3 so we dont need to check the roots since 5 and 3's roots are smaller than 5 and 3
#Therefore we can do it in half the steps i,e O(n/2) which is still O(n) when approximated

#A priority queue is 