class PartyAnimal:
    x = 0
    # -----[ constructor ]------
    def __init__(self):
        print("I am constructed")

    def party(self):
        self.x = self.x + 1
        print("So far " , self.x)
    # -----[ destructor ]---------
    def __del__(self):
        print("I am destructed" , self.x)


an = PartyAnimal() # calling constructor
an.party()
an.party()

an = 42             # calling destructor
print("an contains : " , an )
