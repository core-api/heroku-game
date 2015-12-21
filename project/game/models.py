from django.db import models
import random
import uuid


def get_initial_position():
    return random.choice('abc') + random.choice('123')


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    board = models.CharField(default=".........", max_length=9)
    turns = models.IntegerField(default=5)
    position = models.CharField(max_length=2, default=get_initial_position)
    state = models.CharField(max_length=1, default='p')

    class Meta:
        ordering = ('-created',)

    def get_position(self, position):
        """
        Takes a position like 'b2' and returns the board cell as a character.
        """
        index = {
            'a1': 0, 'a2': 1, 'a3': 2,
            'b1': 3, 'b2': 4, 'b3': 5,
            'c1': 6, 'c2': 7, 'c3': 8,
        }[position]
        return self.board[index]

    def set_position(self, position, state):
        """
        Takes a position like 'b2' and sets the board cell character state.
        """
        index = {
            'a1': 0, 'a2': 1, 'a3': 2,
            'b1': 3, 'b2': 4, 'b3': 5,
            'c1': 6, 'c2': 7, 'c3': 8,
        }[position]
        self.board = self.board[:index] + state + self.board[index + 1:]

    def play(self, position):
        """
        Play in the given position, saving the new state.
        """
        assert not self.is_finished(), 'This game is finished.'
        assert len(position) == 2 and position[0] in 'abc' and position[1] in '123', 'Invalid position.'
        assert self.get_position(position) == '.', 'Position occupied.'

        if position == self.position:
            # User has found the treasure.
            self.set_position(position, '*')
            self.state = 'w'
        else:
            # User has not found the treasure. One less turn remaining.
            self.set_position(position, 'x')
            self.turns -= 1
            if self.turns == 0:
                # If all turns are done then the game is over.
                self.state = 'l'
        self.save()

    def is_finished(self):
        """
        Return True if the game is no longer in progress.
        """
        return self.state in ('w', 'l')

    def get_description(self):
        """
        Return a descriptive state of the game.
        """
        if self.state == 'w':
            return "You've won!"
        elif self.state == 'l':
            return "You've lost."
        elif self.turns == 1:
            return "1 turn remaining."
        return '%d turns remaining.' % self.turns

    def get_board_string(self):
        """
        Return the board state in a string like:

        ...a
        .*.b
        xx.c
        123
        """
        return "%s%s%sa\n%s%s%sb\n%s%s%sc\n123" % (
            self.board[0], self.board[1], self.board[2],
            self.board[3], self.board[4], self.board[5],
            self.board[6], self.board[7], self.board[8]
        )
