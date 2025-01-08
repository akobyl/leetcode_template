"""
strategy:
- we basically have a tree, where the top node contains all the regions as children
- we can then find the smallest common ancestor of the two
- every region has one parent, but every parent can have any number of children (or none)
- assuming there is only 1 "root" parent
- we can create a simple hashmap of the child -> parent
- start with region1/region2, and look up parents until we get to the top
- pop each list and compare the parents until the are not equal
"""


class Solution:
    def findSmallestRegion(
        self, regions: list[list[str]], region1: str, region2: str
    ) -> str:
        parents = {}
        for region in regions:
            parent = region[0]
            for child in region[1:]:
                parents[child] = parent

        parent_list_1 = []
        parent_list_2 = []

        region = region1
        while region in parents:
            parent_list_1.append(region)
            region = parents[region]
        parent_list_1.append(region)

        region = region2
        while region in parents:
            parent_list_2.append(region)
            region = parents[region]
        parent_list_2.append(region)

        r1 = parent_list_1.pop()
        r2 = parent_list_2.pop()
        lowest_common = r1

        while len(parent_list_1) > 0 and len(parent_list_2) > 0:
            r1 = parent_list_1.pop()
            r2 = parent_list_2.pop()
            if r1 == r2:
                lowest_common = r1

        return lowest_common


def test1():
    regions = [
        ["Earth", "North America", "South America"],
        ["North America", "United States", "Canada"],
        ["United States", "New York", "Boston"],
        ["Canada", "Ontario", "Quebec"],
        ["South America", "Brazil"],
    ]
    region1 = "Quebec"
    region2 = "New York"
    assert Solution().findSmallestRegion(regions, region1, region2) == "North America"


def test2():
    regions = [
        ["Earth", "North America", "South America"],
        ["North America", "United States", "Canada"],
        ["United States", "New York", "Boston"],
        ["Canada", "Ontario", "Quebec"],
        ["South America", "Brazil"],
    ]
    region1 = "Canada"
    region2 = "Quebec"
    assert Solution().findSmallestRegion(regions, region1, region2) == "Canada"
