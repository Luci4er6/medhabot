class parent():
    def first(self):
        print("This is first class")

class child(parent):
    def second(self):
        print("This is second class")

obj=child()
obj.first()
obj.second()
