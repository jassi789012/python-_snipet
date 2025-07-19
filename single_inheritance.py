class animal:
    def __init__(self, name, speci):
        self.name = name
        self.speci = speci

    def __str__(self):
        return (f"Name : {self.name}\nSpeci : {self.speci}")

class cat(animal):
    def __init__(self, name, speci, voice):
        animal.__init__(self, name, speci)
        self.voice = voice

    def __str__(self):
        return (f"Name : {self.name}\nSpeci : {self.speci}\nVoice : {self.voice}")

c = cat("cat", "black", "meou")
print(c)