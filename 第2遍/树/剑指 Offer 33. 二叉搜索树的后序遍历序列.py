"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，
否则返回 false。假设输入的数组的任意两个数字都互不相同。
参考以下这颗二叉搜索树：
        5
      / \
    2   6
  / \
1   3
输入: [1,6,3,2,5]
输出: false
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
方法：结合后序遍历与搜索树的特点，寻找分割点，然后分治
"""
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        ll = len(postorder)
        def recur(i, j):  # could catch
            # 为什么加大于号，正常情况下m属于右子树，所以需要减1，
            # 但是假如上来就是右子树m-1为负，即符合大于号
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            if p < j: return False
            return recur(i, m-1) and recur(m, j-1)
        return recur(0, ll-1)

    def verifyPostorder2(self, postorder: [int]) -> bool:
        ll = len(postorder)
        def recur(i, j):  # could catch
        # 由于是存在性问题，所以当切分后的子树长度小于等于2，就必然有
        # 与之对应的搜索树，以长度Wie2为例，大于根可为右子树，小于为左
            if j-i<=1: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            if p < j: return False
            return recur(i, m-1) and recur(m, j-1)
        return recur(0, ll-1)

    def verifyPostorder3(self, postorder: [int]) -> bool:
        """单调栈：还没有研究
        https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/
        """
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while (stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True

