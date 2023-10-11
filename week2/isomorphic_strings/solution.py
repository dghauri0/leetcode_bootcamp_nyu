
class Solution:
    # Check for one-to-one mappings. If one-to-many: false.
    def isIsomorphic(self, s: str, t: str) -> bool:
        comp_dict = Dictionary()
        count = 0
        for i in s:
            comp_dict.add(i, t[count])
            count = count + 1

        output_flag = True
        for i in t:
            if i not in comp_dict.values():
                output_flag = False
                return output_flag

        return output_flag


class Dictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value
