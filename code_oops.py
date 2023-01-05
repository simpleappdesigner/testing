class A:
    def __init__(self,pos):
        self.char_at_pos=pos
class MyWord(A):
    def __init__(self,pos):
        super().__init__(pos)
        self.number_of_chars=0
    def _conv_bn_activation(self,pos):
        def wrapper(input_tensor):
            return input_tensor(self.char_at_pos)     
        return wrapper