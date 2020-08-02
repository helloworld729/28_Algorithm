"""
我们在两条独立的水平线上按给定的顺序写下 A 和 B 中的整数。
现在，我们可以绘制一些连接两个数字 A[i] 和 B[j] 的直线，
只要 A[i] == B[j]，且我们绘制的直线不与任何其他连线（非水平线）相交。
以这种方法绘制线条，并返回我们可以绘制的最大连线数。
示例 1：
输入：A = [1,4,2], B = [1,2,4]
输出：2
链接：https://leetcode-cn.com/problems/uncrossed-lines

思路：连线最多==>最长公共子序列
"""