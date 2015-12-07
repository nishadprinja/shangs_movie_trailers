# Importing from externally written python files to use class Movie and the open_movies_page function
import fresh_tomatoes
import media

'''
9 movie instance variables initialized with a title, storyline, poster, and trailer using the 
Movie class in media.py
'''
the_rundown = media.Movie("The Rundown",
                          "A bounty hunter tracks down his boss's son",
                          "http://movies.geourdu.com/wp-content/uploads/2015/07/The-Rundown-2003.jpg",
                          "https://www.youtube.com/watch?v=BehhBCBSplY")

the_dark_knight = media.Movie("The Dark Knight",
                              "The Joker comes to Gotham City",
                              "http://host.trivialbeing.org/up/tdk-may17-joker-poster-large.jpg",
                              "https://www.youtube.com/watch?v=yrJL5JxEYIw")

inception = media.Movie("Inception",
                        "A heist happens through lucid dreams",
                        "http://www.filmofilia.com/wp-content/uploads/2009/12/inception_poster2.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")
                        
memento = media.Movie("Memento",
                      "A movie runs forwards and backwards",
                      "http://news.doddleme.com/wp-content/uploads/2013/02/memento-movie-poster.jpg",
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0")

waking_life = media.Movie("Waking Life",
                          "A series of dreams unraveled as a moving painting",
                          "http://ecx.images-amazon.com/images/I/51P24AAS71L.jpg",
                          "https://www.youtube.com/watch?v=xX10vQEa56E")

shawshank_redemption = media.Movie("The Shawshank Redemption",
                                   "An innocent man is put in jail",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")
                                   
rang_de_basanti = media.Movie("Rang De Basanti",
                               "Aimless college kids portray the story of India's freedom fighters",
                               "https://upload.wikimedia.org/wikipedia/en/5/5f/RDB_poster.jpg",
                               "https://www.youtube.com/watch?v=9U5gGXvJxO8")

fight_club = media.Movie("Fight Club",
                          "A man's alter-ego causes him to create an underground cult",
                          "http://i.jeded.com/i/fight-club.25541.jpg",
                          "https://www.youtube.com/watch?v=SUXWAEX2jlg")

the_waterboy = media.Movie("The Waterboy",
                           "A waterboy turns out to be a beastly football player",
                           "http://cdn.traileraddict.com/content/touchstone-pictures/thewaterboy.jpg",
                           "https://www.youtube.com/watch?v=z8yv9eq5s14")

'''
An array of the instance variables is built and passed into the open_movies_page function of fresh_tomatoes.py
to serve an HTML page built with the information from these movies
'''
movies = [the_rundown, the_dark_knight, inception, memento, waking_life, shawshank_redemption, rang_de_basanti, fight_club, the_waterboy]

fresh_tomatoes.open_movies_page(movies)

# 6 example movie instances used to test the original Fresh Tomatoes Movie Trailers site

# toy_story = media.Movie("Toy Story",
#                         "A story of a boy and his toys that come to life",
#                         "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
#                         "https://www.youtube.com/watch?v=vwyZH85NQC4")

# avatar = media.Movie("Avatar",
#                      "A marine on an alien planet",
#                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
#                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# school_of_rock = media.Movie("School of Rock",
#                              "A music teacher tries to make a band with his students",
#                              "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
#                              "https://www.youtube.com/watch?v=3PsUJFEBC74")

# ratatouille = media.Movie("Ratatouille",
#                           "A rat cooks food",
#                           "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
#                           "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# midnight_in_paris = media.Movie("Midnight in Paris",
#                                 "In Paris, it's midnight",
#                                 "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
#                                 "https://www.youtube.com/watch?v=atLg2wQQxvU")

# hunger_games = media.Movie("Hunger Games",
#                            "Everyone's hungry, but still playing games",
#                            "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
#                            "https://www.youtube.com/watch?v=PbA63a7H0bo")

#movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]