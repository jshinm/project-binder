# A heap is a specialized tree-based data structure that satisfies the
# heap property, which is defined as follows: For a min-heap, the value
# of each node must be greater than or equal to the value of its parent
# node, and for a max-heap, the value of each node must be less than or
# equal to the value of its parent node. In other words, the root node
# of a min-heap contains the minimum value of all the nodes in the heap,
# while the root node of a max-heap contains the maximum value of all the
# nodes in the heap.

# Heaps are commonly used to implement priority queues, which are data 
# structures that allow elements to be inserted and deleted in order of 
# their priority. The most common operations on a heap include inserting 
# a new element, deleting the minimum or maximum element, and updating 
# the value of an existing element.

# There are two main types of heaps: binary heaps and d-ary heaps. Binary 
# heaps are trees where each node has at most two children, while d-ary heaps 
# have d children for each node. Binary heaps are typically used because 
# they can be efficiently implemented using an array, whereas d-ary heaps 
# require more complex data structures.

# There are also two main ways to implement a heap: using an array or using 
# a tree. When using an array, the heap is represented as a complete binary 
# tree, where the values are stored in an array and the children of each node 
# can be computed using simple arithmetic. When using a tree, the heap is 
# represented as a regular binary tree, where each node has pointers to its 
# left and right children.

# Heaps have a number of important applications, including sorting algorithms 
# (e.g., heapsort), graph algorithms (e.g., Dijkstra's shortest path algorithm),
# and memory management in operating systems.

import heapq

tasks = [(3, 'Task 1'), (1, 'Task 2'), (2, 'Task 3'), (1, 'Task 4')]

# creates heap inplace
heapq.heapify(tasks)

next_task = heapq.heappop(tasks)

# prints `Task 2` as it's the highest priority
print(next_task)