cats_Ponor = ["Cancan", "Pizza", "Ponos"]
good_against = ["red", "black", "all"]


# de invatat mai bine (de ce se pune def + de ce trebuie sa ii atribui cv pentru a functiona(sa nu dea eroarea aia cu multe numere si cifre(de trebuie sa ii dai call la function cu __name__ sau idk..)))

class cancan:
  def __init__(self, name, leg):
    self.name = cats_Ponor[0]
    self.leg = good_against[0]
    pass

cat1 = cancan("name", "leg")


class Pizza:
  def __init__(self, name, leg):
    self.name = cats_Ponor[1]
    self.leg = good_against[1]
    pass

cat2 = Pizza("name", "leg")

class Ponos:
  def __init__(self, name, leg):
    self.name = cats_Ponor[2]
    self.leg = good_against[2]
    pass

cat3 = Ponos("name", "leg")

cats = [cat1, cat2, cat3]

cat = (input("What cat do you choose? \n"))



# de optimizat 🔽🔽🔽🔽🔽🔽

if cat == cancan.__name__:
    print(cat1.name,"\n" ,cat1. leg),
    pass

elif cat == Pizza.__name__:
    print(cat2.name,'\n', cat2.leg),
    pass

elif cat == Ponos.__name__:
    print(cat3.name, '\n', cat3.leg)
    pass


else:
  print("Cat not recognized.")
  pass