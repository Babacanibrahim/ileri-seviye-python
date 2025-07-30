class Movie():
    def __init__(self, title , director, year, duration):
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration

    def __repr__(self):
        return f"{self.title} filmi {self.director} tarafından {self.year} yılında çekilmiştir"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("film silindi")
    
movie = Movie("Başlık","Yönetmen",2015,120)
print(movie)
print(len(movie))

del movie

# import keyword

# print(keyword.kwlist)