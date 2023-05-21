import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents.copy()

        balls_drawn = []
        for _ in range(num_balls):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            balls_drawn.append(ball)

        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        expected_balls_copy = copy.deepcopy(expected_balls)

        success = True
        for color in balls_drawn:
            if color in expected_balls_copy:
                expected_balls_copy[color] -= 1
                if expected_balls_copy[color] == 0:
                    del expected_balls_copy[color]

            if len(expected_balls_copy) == 0:
                break

        if len(expected_balls_copy) == 0:
            num_successful_experiments += 1

    return num_successful_experiments / num_experiments
