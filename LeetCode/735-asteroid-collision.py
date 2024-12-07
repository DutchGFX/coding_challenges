class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        """
        Determines which asteroids will survive a series of collisions

        Parameters
        ----------
        asteroids : list[int]
            list of asteroids where the magnitude gives the size and
            the sign gives direction of travel (+ is right)

        Returns
        -------
        stack : list[int]
            asteroids that survive the collisions
        """
        stack = []
        for a in asteroids:  # for each asteroid
            stack.append(a)  # push the new asteroid onto the stack

            # while this new asteroid and the previous asteroid would collide
            # they only collide if the asteroid on the left is moving to the right
            # and the asteroid on the right is moving to the left
            while (len(stack) >= 2) and (stack[-2] > 0 > stack[-1]):
                # pop the two asteroids off the stack,
                v_curr = stack.pop(-1)
                v_prev = stack.pop(-1)
                if abs(v_curr) > abs(v_prev):
                    stack.append(v_curr)
                elif abs(v_curr) < abs(v_prev):
                    stack.append(v_prev)

        return stack
