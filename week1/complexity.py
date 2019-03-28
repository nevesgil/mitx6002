def get_all_subsets(some_list):
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        return [[]]
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt
    for partial_subset in get_all_subsets(rest_list):
        subsets.append(partial_subset)
        next_subset = partial_subset[:] + [first_elt]
        subsets.append(next_subset)
    return subsets

NUMBER = 3
def look_for_all_the_things(myList):
    """Looks at all subsets of this list"""
    # Make subsets
    all_subsets = get_all_subsets(myList)
    for subset in all_subsets:
        if sum(subset) == NUMBER:
            return True
    return False
    
```
Explanation: 
The point of this exercise was to get you thinking about the complexity of functions, specifically the complexity 
of different ways to enumerate items. Keep these complexities in mind as you continue throughout this lecture sequence. 
It might sound great to always get the very best solution by enumerating all possible choices - but the downside to this 
approach is the terribly high complexity!
O (2^n) is the complexity for the final question because we are enumerating all 
possible subsets of a set, known as the "power set" of a set. We will talk about power sets more in the next videos. 
Technically, the complexity is actually O(n * 2^n) because the sum() is O(n)
, but (2^n) is already large enough that we can ignore the multiplier.
```
