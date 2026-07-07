class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        # Count characters of s1
        for c in s1:
            s1_counts[ord(c) - ord('a')] += 1

        # Count first window in s2
        for i in range(n1):
            s2_counts[ord(s2[i]) - ord('a')] += 1

        if s1_counts == s2_counts:
            return True

        left = 0

        # Slide the window
        for right in range(n1, n2):
            # Add new character
            s2_counts[ord(s2[right]) - ord('a')] += 1

            # Remove old character
            s2_counts[ord(s2[left]) - ord('a')] -= 1

            left += 1

            if s1_counts == s2_counts:
                return True

        return False