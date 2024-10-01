def check_movie_realease(movie):
    if movie['year'] <2000:
        print(f"This movie was released before 2000")
    else:
        print(f"This movie was released after 2000")
        return movie['name']
    
recent_movies =[]

favorite_movies = [
    {'name': 'Frozen' , 'year': 2013 },
    {'name': 'Forrest Gump' , 'year': 1994 },
    {'name': 'Men in Black' , 'year': 1997 },
    {'name': 'Dune:Part Two' , 'year': 2024 }
]

for movie in favorite_movies:
    result = check_movie_realease(movie)
    if result is not None:
        recent_movies.append(result)

print("Recent movies:", recent_movies)