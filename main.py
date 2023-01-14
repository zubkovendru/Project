def sum(*args, **kwargs):
    k = 0
    try:
        for i in args:
            k += int(i) ** 2

        for j in kwargs:
            k += int(j) ** 2
        print(k)
    except ValueError:
        print("ValueError!")
    except TypeError:
        print("TypeError!")
    except:
        print("Error!")


sum(1, "2", "two")


class Item():
    def __init__(self, painting, delo2, srok, priority):
        self.painting = painting
        self.delo2 = delo2
        self.srok = srok
        self.priority = priority

    def paint(self):
        print(f"You painted a picture in {self.srok} minutes, congratulations!")

    def delo(self):
        print(f"You did {self.priority}!")

c = Item(painting = 'рисование', delo2 = 'футболл', srok = 10, priority = 'a very high priority case')
c.paint()
c.delo()

class ItemList:
  def __init__(self, dela):
    self.dela = dela

  def get_all_cases(self):
    print(*self.dela)

v = ItemList(("zasxzas", "ddd","ghgh"))
v.get_all_cases()