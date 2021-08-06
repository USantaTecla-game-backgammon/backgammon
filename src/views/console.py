from typing import List

class Console:
    def show(self, msg: str) -> None:
        print(msg)
            
    def read_str(self, msg: str = '') -> str:
        while True:
            user_input: str = input(msg + ': ')
            if user_input:
                break
        return user_input

    def read_int(self, msg: str = '') -> int:
        user_str: str = self.read_str(msg)
        try:
            user_int: int = int(user_str)
            return user_int
        except ValueError:
            self.show('Solo se permiten números')
            return self.read_int(msg)

    def read_int_range(self, valids: List[int], msg: str = '') -> int:
        user_int: int = self.read_int(msg)
        if(not user_int in valids):
            print('valores permitidos: ', valids)
            return self.read_int_range(valids, msg)
        return user_int