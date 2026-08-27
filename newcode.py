class family_member:

    def __init__(self,eye_color,height):
        self.eye_color = eye_color
        self.height = height

    def show_traits(self):
      print(self.name)
      print(self.age)

class kid(family_member):

    def __init__(self,name,age,eye_color,height):
        self.name = name
        self.age = age
        family_member.__init__(self,eye_color,height)

    def show_traits(self):
        print(self.name)


    def age_printer(self, age):
        print(self.name,"age is",self.age)

obj = kid("ahmed",8,"Blue","5-1")

obj.show_traits()
obj.age_printer(8)

print("IS KID A SUBCLASS OF FAMILY?",issubclass(kid,family_member))