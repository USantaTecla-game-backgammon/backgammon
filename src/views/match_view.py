class MatchView:

    @classmethod
    def show(cls) -> None:
        print('TODO: Configure')

    @classmethod
    def read(cls) -> int:
        goal = 0
        while goal not in range(1, 64):
            try:
                goal = int(input('Insert goal (1-64):'))
            except ValueError:
                pass
        return goal
