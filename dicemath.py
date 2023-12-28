import random

# Basic Dice class
class Dice:
    def __init__(self, num_dice, sides):
        self._num_dice = num_dice
        self._sides = sides
        self.results = []

    # Rolls the dice
    def roll_dice(self):
        for i in range(self._num_dice):
            self.results.append(random.randrange(1, self._sides + 1))
        return self.results
    

# Shadowrun behavior and rolls
class Shadowrun(Dice):
    def __init__(self, num_dice, sides):
        super().__init__(num_dice, sides)
        self._hits = 0
        self._exploded_hits = 0
        self._ones = 0
        self._exploding_dice = 0
        self._glitch = False
        self._critical_glitch = False
        self._exploded_dice = []

    def roll_dice(self):
        rolls = super().roll_dice()

        for die in self.results:
            if die == 6:
                self._exploding_dice += 1
            if die >= 5:
                self._hits += 1
            if die == 1:
                self._ones += 1

        while self._exploding_dice != 0:
            self.explode_dice()

        for die in self._exploded_dice:
            if die >= 5:
                self._exploded_hits += 1

        glitch_report = self.glitch_city()
        exploded_report = self.explosion()


        if glitch_report is None:
            glitch_report = "Good news!  You didn't glitch!"
        
        if exploded_report is None:
            exploded_report = "I hope you didn't spend Edge on this because you got no sixes..."

        return rolls, glitch_report, exploded_report

    def glitch_city(self):
        if self._ones >= len(self.results) // 2:
            self._glitch = True
        if self._glitch and self._hits == 0:
            self._critical_glitch = True
        if self._critical_glitch:
            return "Oh that's a Critical Glitch... I hope your GM is merciful!"
        if self._glitch and not self._critical_glitch:
            return "Someone just Glitched!  This could be embarrassing..."
        else :
            pass

    def explode_dice(self):
        explode = random.randrange(1, self._sides + 1)
        self._exploded_dice.append(explode)
        self._exploding_dice -= 1
        if explode == 6:
            self._exploding_dice += 1

    def explosion(self):
        if len(self._exploded_dice) == 0:
            pass
        else :
            return f"If you had Edged this roll you would have rolled an extra {len(self._exploded_dice)} dice for {self._exploded_dice}.  That would have netted you an additional {self._exploded_hits} hits."



def test_case():
    d1 = Shadowrun(10, 6)
    rolled_dice = d1.roll_dice()
    print(rolled_dice)
