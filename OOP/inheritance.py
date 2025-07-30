class Person ():
    def __init__(self, name , surname , age):
        self.name = name
        self.surname = surname
        self.age = age
        print("İnsan sınııfı oluşturuldu.\n")

    def intro(self):
        print(self.name , self.surname , self.age)


class Student(Person):
    def __init__(self, name, surname, age, number):
        super().__init__(name, surname, age)
        self.number = number
        print("Öğrenci sınııfı oluşturuldu.\n")


    def intro (self):
        print(self.name , self.surname , self.age , self.number)

    def study(self):
        print(self.name + " ders çalışıyor")

class Teacher(Person):
    def __init__(self, name, surname, age , branch):
        super().__init__(name, surname, age)
        self.branch = branch
        print("Öğretmen sınııfı oluşturuldu.\n")


    def intro(self):
        print(self.name , self.surname , self.age , self.branch)

    def teach(self):
        print(self.name + self.branch +" dersini anlatıyor")

    
st = Student("İbrahim","Babacan",25,1915)
st.intro()
st.study()

tchr = Teacher("Mehmet","Yılmaz",50,"Fizik")
tchr.intro()
tchr.teach()

person = Person("Ali","Bozkurt",45)
person.intro()