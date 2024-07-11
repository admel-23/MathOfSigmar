import random
from pydantic import BaseModel
from enum import Enum

class DiceRollResult(Enum):
    SUCCESS = 1,
    CRITICAL_SUCCESS = 2,
    FAILURE = 3,
    CRITICAL_FAILURE = 4

    def is_failed(self):
        if self == DiceRollResult.FAILURE:
            return True
        if self == DiceRollResult.CRITICAL_FAILURE:
            return True

    def is_succeeded(self):
        return not self.is_failed()

    def is_critical_success(self):
        return self == DiceRollResult.CRITICAL_SUCCESS

class Dice(BaseModel):
    size: int
    fixed: int = 0

    def roll(self):
        return random.randint(1, self.size) + self.fixed

    def roll_check(self,
                   passing_threshold: int,
                   roll_modifier: int = 0,
                   critical_success_allowed: bool = True) -> DiceRollResult:
        natural_roll_result = self.roll()
        if natural_roll_result == self.size and critical_success_allowed:
            return DiceRollResult.CRITICAL_SUCCESS
        if natural_roll_result == 1:
            return DiceRollResult.CRITICAL_FAILURE
        modified_roll_result = natural_roll_result + roll_modifier
        if modified_roll_result >= passing_threshold:
            return DiceRollResult.SUCCESS
        else:
            return DiceRollResult.FAILURE

class MultiDice(Dice):
    count: int
    fixed: int = 0

D3 = Dice(size=3)
D6 = Dice(size=6)
D3_p3 = Dice(size=3, fixed=3)