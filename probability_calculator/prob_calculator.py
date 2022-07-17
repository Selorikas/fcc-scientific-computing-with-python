import copy
import random

class Hat:
    # Initialise hat with a variable number of colours and their count
    def __init__(self, **kwargs):
        self.contents = []
        for color, number in kwargs.items():
            for _ in range(number):
                self.contents.append(color)

    # draw a random number of balls from the hat
    def draw(self, number):
        if number > len(self.contents):
            return self.contents

        balls = []
        for _ in range(number):
            drawn = random.randrange(len(self.contents))
            balls.append(self.contents.pop(drawn))
        return balls

# calculate the probability of drawing a predefined assortment of balls when performing N experiments
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # initialize the expected assortment
    expected = []
    for index in expected_balls:
        expected.append(expected_balls[index])

        # perform N random experiments and check whether the assortment of this experiment corresponds to the expected assortment
    successes = 0
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls_drawn = new_hat.draw(num_balls_drawn)
        attempt = []
        for color in expected_balls:
            attempt.append(balls_drawn.count(color))
        if attempt >= expected:
            successes += 1

    return successes / num_experiments