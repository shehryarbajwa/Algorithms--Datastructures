### Problem 4 - User in Group

### Explanation

Here we can use use recursion similar to how we check for path in File Recursion. We can check whether a user exists in the existing group. If not, we can check if there exists a group within a group and we can check there. At most each element will be checked atleast once

### Efficiency

The algorithm will run in O(n) time beacuse each group and user will be checked atleast once during the recursive calls.