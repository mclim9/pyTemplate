class covid():
    """ Covid Class """
    def __init__(self):
        super().__init__()          # If inheriting
        self.foo    = 'N'
        self.bar    = 100

    def Get_Covid(self):
        rdStr = 'Get Covid'
        return rdStr

    def Init_Covid(self):
        print('Covid Init')

    def Set_Covid(self):
        print('Set Covid')

if __name__ == "__main__":              # won't be run when imported
    foo = covid()
    foo.foo = 'Hello'
