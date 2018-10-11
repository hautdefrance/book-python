class Prostokat:

    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return (self.a + self.b) * 2

    def __str__(self):
        return 'Prostokat(a=%s, b=%s)' % (self.a, self.b)