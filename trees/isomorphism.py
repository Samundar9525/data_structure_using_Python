def isIsomorphic(self, root1, root2):
    # code here.

    def solution(node1, node2):
        if node1 == None and node2 == None:
            return True
        if node1 == None or node2 == None:
            return False

        if node1.data != node2.data:
            return False
        case1 = solution(node1.left, node2.left) and solution(node1.right, node2.right)
        case2 = solution(node1.left, node2.right) and solution(node1.right, node2.left)
        return case1 or case2

    return (solution(root1, root2))
