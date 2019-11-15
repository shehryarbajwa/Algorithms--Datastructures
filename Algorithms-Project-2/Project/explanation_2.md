### Problem 2 - File Recursion

### Explanation

I will be using a list to append to all the files that are found with the given extension name. Since we are going to be iterating over file and folders, this problem can be best solved via recursion. 

### Efficiency
n -represents the size of the input
m - represents the size of the recursion call function

Append has the time complexity of O(1) while Extend has the time complexity of O(k). Traversing through a tree will be done in O(n) time. The space complexity of the function will depend on how deep the recursion tree is. If each function call of the file recursion take O(m) space and the maximum depth of recursion tree is n then space complexity of recursive algorithm would be O(mn) 