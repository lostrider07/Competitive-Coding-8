#Time complexity O(n)
#Space complexity: O(h)

#Recursion dfs approach
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            #base
            if not root:
                return None
            
            #logic
            lefttail = dfs(root.left)
            righttail = dfs(root.right)
            
            if root.left:
                lefttail.right = root.right
                
                root.right = root.left
                
                root.left = None
                
            last_node = righttail or lefttail or root
            
            return last_node
        
        dfs(root)
            
