from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        max_altitude = 0

        for change in gain:
            current_altitude += change
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude
