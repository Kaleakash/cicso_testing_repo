class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Penguin(Bird):

    def fly(self):
        raise Exception("Penguins cannot fly")

# Main application

def make_bird_fly(bird):
    bird.fly()

sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)
#make_bird_fly(penguin)