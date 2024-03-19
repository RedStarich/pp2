class Square():
    def __init__(self, length):
        self.length = length
    
    def generate_sq(self):
        n = int(self.length)
        g = n-2
        h = " "*g
        print("*"*n)
        for i in range(1, n-1):
            print("*", " "*g,'*', sep='')
            
        print("*"*n)
        return
    
a = Square(5).generate_sq()
