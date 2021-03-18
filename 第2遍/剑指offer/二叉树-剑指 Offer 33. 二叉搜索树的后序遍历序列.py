from typing import List

# 功能：判断一个列表的数据是不是某二叉搜索树的后序遍历结果

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # 搜索树的特点：所有的左子树 小于 根节点 小于 右子树
        # 那么根据根节点，定位出左右子树，然后递归即可
        def checkPostorder(postList, i, j):
            if i >= j: return True

            cut_idx = i
            root_value = postorder[j]
            while cut_idx <= j:
                if postorder[cut_idx] >= root_value:
                    break
                cut_idx += 1

            for k in range(cut_idx + 1, j):
                if postList[k] < root_value:
                    return False

            return checkPostorder(postList, i, cut_idx - 1) and \
                   checkPostorder(postList, cut_idx, j - 1)

        return checkPostorder(postorder, 0, len(postorder) - 1)
