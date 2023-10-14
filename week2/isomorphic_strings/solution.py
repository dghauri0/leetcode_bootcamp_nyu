class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        output_flag = False
        s_char = []
        t_char = []

        # Use python's first index return of char.
        for i in s:
            s_char.append(s.index(i))
        for i in t:
            t_char.append(t.index(i))

        # If the indexes match, one-to-one mapping.
        if s_char == t_char:
            output_flag = True
            return output_flag

        return output_flag
