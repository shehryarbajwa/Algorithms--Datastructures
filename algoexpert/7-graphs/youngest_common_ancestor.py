class AncestralTree:
    def __init__(self,name):
        self.name = name
        self.ancestor = None


#Time Complexity O(d) since for worst case we have to traverse the entire tree to reach the leaf node
#space complexity O(1) since we are doing it iteratively and not storing much just depth which is a constant time operation
def get_youngest_common_ancestor(top_ancestor, descendant_one, descendant_two):
    depthOne = calculateDescendantDepth(descendant_one, top_ancestor)
    depthTwo = calculateDescendantDepth(descendant_two, top_ancestor)
    if depthOne > depthTwo:
        return backtrack_ancestor(descendant_one, descendant_two, depthOne - depthTwo)
    else:
        return backtrackancestor(descendant_two, descendant_one, depthTwo - depthOne)

def calculate_descendant_depth(lower_descendant, top_ancestor):
    depth = 0
    while lower_descendant != top_ancestor:
        depth += 1
        lower_descendant = lower_descendant.ancestor
    return depth

def backtrack_ancestor(lower_descendant, top_descendant, difference):
    while difference > 0:
        lower_descendant = lower_descendant.ancestor
        difference -= 1
    while lower_descendant != top_descendant:
        lower_descendant = lower_descendant.ancestor
        top_descendant = top_descendant.ancestor
    return lower_ancestor


        

    