class spam():
    """ Spam Class """
    def __init__(self):
        super().__init__()          # If inheriting
        self.ham    = 'ham'
        self.eggs   = 100

    def Get_Spam(self):
        rdStr = 'Get Spam'
        return rdStr

    def Init_Spam(self):
        print('Spam Init')

    def Set_Spam(self):
        print('Set Spam')

if __name__ == "__main__":                  # won't be run when imported
    foo = spam()
    foo.foo = 'Hello'
