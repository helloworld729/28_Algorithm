# -*- coding:utf-8 -*-
# Author:Knight
# @Time:2021/1/19 10:10

# 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
# 连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。
# 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。

from typing import List
from collections import defaultdict


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 最小生成树算法
        # 构建包含 邻接边权重的 邻接表

        def calDistance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        adjacent = defaultdict(list)
        length = len(points)
        for i in range(length):
            for j in range(i+1, length):
                adjacent[str(points[i][0]) + "_" + str(points[i][1])].append(
                    (calDistance(points[i], points[j]), str(points[j][0]) + "_" + str(points[j][1]))  # 距离，邻接点
                )
                adjacent[str(points[j][0]) + "_" + str(points[j][1])].append(
                    (calDistance(points[i], points[j]), str(points[i][0]) + "_" + str(points[i][1]))  # 距离，邻接点
                )

        def prim(v):
            mst = {str(p[0]) + "_" + str(p[1]): None for p in points}
            cans = [(0, v, v)]  # 非联通区候选值 距离，前节点，后节点
            count = 0
            while cans and count < length:
                w, vi, vj = cans.pop()  # 最优联通边
                if mst[vj]: continue  # 已经在联通区的话
                count += 1
                mst[vj] = w
                for (vk_weight, vk) in adjacent[vj]:
                    if mst[vk] is None:
                        cans.append((vk_weight, vj, vk))
                cans.sort(reverse=True)
            return mst

        minLen = float("inf")
        for node in points:
            mst = prim(str(node[0]) + "_" + str(node[1]))
            print(mst)
            dis = sum(mst.values())

            minLen = min(minLen, dis)

        return minLen

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(Solution().minCostConnectPoints(points))

# 这个是O(n**3)的多源点最短路径算法， 超时间了

