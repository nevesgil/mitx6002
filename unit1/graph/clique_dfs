A clique is an unweighted graph where each node connects to all other nodes. We denote the clique with 
nodes as KN. Answer the following questions in terms of n.

1. How many edges are in KN? 
In a directed graph, each node would connect to all other nodes, yielding n*(n-1) edges. 
ans: In our undirected graph, an edge from A to B and from B to A are the same edge, so there are, in fact, half as many.
Then n*(n-1)/2

2. Consider the new version of DFS. This traverses paths until all non-circular paths from the source to the 
destination have been found, and returns the shortest one.
Let A be the source node, and B be the destination in KN. How many paths of length 2 exist from A to B?
ans: (n-2)
We have a source A and a destination B. Paths of length 2 contain exactly three three nodes. We must select one more node to place in the middle of our path. 
As we cannot select the A or B, we are left with N - 2 choices to construct a path.

3. How many paths of length 3 exist from A to B?
ans: (n-2)*(n-3) 
Use the same reasoning as used for the previous problem. After knowing our source and destination, we must travel through 2 additional nodes without touching any node twice. For the first node, we have (n-2) 
choices, and for the second, we have (n-3) choices.
Note that this is equivalent to (n-2)!/(n-4)!

4. Continuing the logic used above, calculate the number of paths of length M from A to B, where 1 <= M <= (n-1), and 
write this number as a ratio of factorials.
To indicate a factorial, please enter fact(n) to mean n!; fact(n+2) to mean (n+2)!, etc.
ans: (n-2)!/(n-m-1)!

5. too complicated to post here 
