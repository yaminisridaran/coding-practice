class Node:
      def __init__(self, value, left=None, right=None):
           self.value=value
           self.left=left
           self.right=right

def kthSmallest(root, k):
     stack = []
     while root or stack:
           while root:
                 stack.append(root)
                 root = root.left

           root = stack.pop()        
           k -= 1
           if k == 0:
                 break
           root = root.right

     return root.value

if __name__ == '__main__':
     node1 = Node(10)
     node2 = Node(5)
     node3 = Node(15)
     node4 = Node(2)
     node5 = Node(7)
     node6 = Node(12)
     node7 = Node(17)

     node1.left, node1.right = node2, node3
     node2.left, node2.right = node4, node5
     node3.left, node3.right = node6, node7

     print(kthSmallest(node1, 3))
     


          
