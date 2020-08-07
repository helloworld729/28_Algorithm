class Solution:
    def rob(self, root) -> int:
        def rob_money(root):
            if not root: return 0

            choose_1 = root.val

            if root.left:
                choose_1 += rob_money(root.left.left) + rob_money(root.left.right)
            if root.right:
                choose_1 += rob_money(root.right.left) + rob_money(root.right.right)

            choose_2 = rob_money(root.left) + rob_money(root.right)
            return  max(choose_1, choose_2)

        return rob_money(root)

    def rob2(self, root) -> int:
        def _rob(root):
            if not root: return 0, 0

            ls, ln = _rob(root.left)   # 偷左子树、不偷左子树的收益
            rs, rn = _rob(root.right)  # 偷右子树、不偷右子树的收益

            return root.val + ln + rn, max(ls, ln) + max(rs, rn)  # 偷root/不偷root的最大收益

        return max(_rob(root))

def binary(num):
    back = num
    count = 0
    pre = num % 2
    num //= 2

    while num > 0:
        rest = num % 2
        num //= 2
        # print(pre, rest, count)
        if rest and pre:
            count += 1
        pre = rest
    # print(num,count)
    return back + 1 - count
