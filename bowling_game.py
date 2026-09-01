# Source - https://stackoverflow.com/a/39567637
# Posted by Maarten Bosmans
# Retrieved 2026-08-27, License - CC BY-SA 3.0

class Game(object):
    def __init__(self):
        self._score = [[]]

    def roll(self, pins):
        # start new frame if needed
        if len(self._score[-1]) > 1 or 10 in self._score[-1]:
            self._score.append([])

        # add bonus points to the previous frames
        for frame in self._score[-3:-1]:
            if sum(frame[:2]) >= 10 and len(frame) < 3:
                frame.append(pins)

        # add normal points to current frame
        for frame in self._score[-1:10]:
            frame.append(pins)

    def score(self):
        return sum(sum(x) for x in self._score)
