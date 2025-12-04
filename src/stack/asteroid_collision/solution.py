class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            while asteroid:
                try:
                    left_asteroid = stack.pop()
                    if asteroid > 0 or (asteroid < 0 and left_asteroid < 0):
                        stack.extend([left_asteroid, asteroid])
                        asteroid = None
                    else:
                        if abs(asteroid) == abs(left_asteroid):
                            asteroid = None
                        elif abs(asteroid) < abs(left_asteroid):
                            stack.append(left_asteroid)
                            asteroid = None
                except IndexError:
                    stack.append(asteroid)
                    asteroid = None
        return stack
