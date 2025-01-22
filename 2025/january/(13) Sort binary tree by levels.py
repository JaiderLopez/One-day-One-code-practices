#problem (codewars)
"""
You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, 
then root children (from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:

                 2
            8        9
          1  3     4   5
Should return following list:

[2,8,9,1,3,4,5]
Example 2 - following tree:

                 1
            8        4
              3        5
                         7
Should return following list:

[1,8,4,3,5,7]
"""

#What I think I gonna do
"""
Initialize the Queue
Level Traversal
Use a while loop to process nodes in the queue
Remove the current node from the queue and add its value to a result list
Add the left and right children of the current node to the queue, if they exist.
Return the list with the node values
"""

#First implementation
class Node:
   def __init__(self, L, R, n):
      self.left = L
      self.right = R
      self.value = n

def tree_by_levels(node):
   if node is None:
      return []
   
   result, queue = [], [node]   

   while queue:
      current = queue.pop(0)
      result.append(current.value)

      if current.left is not None:
         queue.append(current.left)

      if current.right is not None:
         queue.append(current.right)

   return result
   
#clean code
# no more clean code than before code for this problem (well, I don't thing so)
print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))