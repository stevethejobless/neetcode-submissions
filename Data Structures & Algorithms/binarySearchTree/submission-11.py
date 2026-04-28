class TreeNode:
    def __init__(self, val = None, left = None, right=None, key=None):
        self.val = val
        self.left = left
        self.right = right
        self.key = key

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key=key, val=val)
            return
        cur = self.root
        while cur:
            if key > cur.key:
                if not cur.right:
                    cur.right = TreeNode(key=key,val=val)
                    return
                cur = cur.right
            if key < cur.key:
                if not cur.left:
                    cur.left = TreeNode(key=key,val=val)
                    return
                cur = cur.left
            if key == cur.key:
                cur.val = val
                return

    def get(self, key: int) -> int:
        cur = self.root
        while cur:
            if key > cur.key: 
                cur = cur.right
            elif key < cur.key:
                cur = cur.left
            elif key == cur.key:
                return cur.val
        return -1


    def getMin(self) -> int:
        if not self.root:
            return -1
        return self._getMin(self.root).val

    
    def _getMin(self,root):
        while root.left:
            root = root.left
        return root

    def getMax(self) -> int:
        cur = self.root
        if not cur:
            return -1
        while cur.right:
            cur = cur.right
        return cur.val

    def remove(self, key: int) -> None:
        self.root = self._remove(self.root,key)
        
    def _remove(self, root, key):
        if not root:
            return
        if key > root.key:
            root.right = self._remove(root.right,key)
            return root
        if key < root.key:
            root.left = self._remove(root.left, key)
            return root
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            min_node = self._getMin(root.right)            
            root = self._remove(root, min_node.key)
            print(min_node.val,min_node.key)
            root.val = min_node.val
            root.key = min_node.key
            return root


    def getInorderKeys(self) -> List[int]:
        keys_asc = []
        def inorder(cur):
            if not cur:
                return
            inorder(cur.left)
            keys_asc.append(cur.key)
            inorder(cur.right)
        inorder(self.root)
        return keys_asc
