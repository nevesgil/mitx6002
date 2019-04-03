'''
Write a generator that returns every arrangement of items such that each is in one or none of two different bags. 
Each combination should be given as a tuple of two lists, the first being the items in bag1, and the second being the items in bag2.
'''

# Answer:
def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each item is in one or zero bags.
    Yields a tuple, (bag1, bag2), where each bag is represented as a list of which item(s) are in each bag.
    """
    N = len(items)
    # Enumerate the 3**N possible combinations   
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)
        
        
# grader's answer...

'''
I was never a math guy but I'll try to explain it in the way I managed to understand it (without that bits or "trits" thingy).
If j=0, the value i // 3^j is just i and goes like 0, 1, 2, 3, 4, 5, ..., 80.
If j=1, it slows down to 1/3 'speed' and goes like 0, 0, 0, 1, 1, 1, 2, 2, 2, ..., 26, 26, 26.
If j=2, it slows down to 1/9 'speed' and goes like (nine 0's), (nine 1's), (nine 2's), ..., (nine 26's)
If j=3, now it's at 1/27 'speed' and goes like (twenty seven 0's), (twenty seven 1's), (twenty seven 2's)
Now if you do the '% 3' operation and get the remainders, it looks like this:
j=0: 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, .... (changes every iteration)
j=1: 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, .... (changes every 3 iterations)
j=2: 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, .... (changes every 9 iterations)
j=3: 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, .... (changes every 27 iterations)
Now if you look at the four numbers that are on the same vertical line, you'll see that they together represent one 
of the 81 possible combinations and there are all of them. So you can create all 81 subsets with them.
'''
