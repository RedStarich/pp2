# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#task1
def above_fivefive(movie):
    if movie["imdb"] > 5.5:
        return True
    else:
        return False

# movie = {
# "name": "Usual Suspects", 
# "imdb": 5.0,
# "category": "Thriller"
# }
# if above_fivefive(movie):
#     print("yes")
# else:
#     print("no")
    
#task2
def good_movies_list(movies):
    good_movies = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            good_movies.append(movie["name"])
        else:
            continue
    return good_movies

# print(good_movies_list(movies))

#task3
def category_list(movies, categ):
    list_of_category = []
    for movie in movies:
        if movie["category"] == categ:
            list_of_category.append(movie)
        else:
            continue
    return list_of_category
# print(category_list(movies, "Suspense"))

#task4
def average_score(list_of_movies):
    score = 0
    movie_number = len(list_of_movies)
    for movie in list_of_movies:
        current_score = movie["imdb"]
        score += float(current_score)
    score /= movie_number
    return score

# list_of_movies = movies[0:3]
# print(average_score(list_of_movies))

#task5
def category_avg_score(movies, categ):
    score = average_score(category_list(movies, categ))
    return score
# categ = "Suspense"
# result = category_avg_score(movies, categ)
# print(result)
