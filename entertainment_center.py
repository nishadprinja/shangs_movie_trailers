# Importing from external .py files
import fresh_tomatoes
import media

'''
9 movie instance variables initialized with a title, storyline, poster, and
trailer using the Movie class in media.py
'''
the_rundown = media.Movie("The Rundown",
                          "A bounty hunter tracks down his boss's son",
                          "http://movies.geourdu.com/wp-content/uploads/2015/07/The-Rundown-2003.jpg",  # noqa
                          "https://www.youtube.com/watch?v=BehhBCBSplY")

the_dark_knight = media.Movie("The Dark Knight",
                              "The Joker comes to Gotham City",
                              "http://host.trivialbeing.org/up/tdk-may17-joker-poster-large.jpg",  # noqa
                              "https://www.youtube.com/watch?v=yrJL5JxEYIw")

inception = media.Movie("Inception",
                        "A heist happens through lucid dreams",
                        "http://www.filmofilia.com/wp-content/uploads/2009/12/inception_poster2.jpg",  # noqa
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

memento = media.Movie("Memento",
                      "A movie runs forwards and backwards",
                      "http://news.doddleme.com/wp-content/uploads/2013/02/memento-movie-poster.jpg",  # noqa
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0")

waking_life = media.Movie("Waking Life",
                          "A series of dreams unraveled as a moving painting",
                          "http://ecx.images-amazon.com/images/I/51P24AAS71L.jpg",  # noqa
                          "https://www.youtube.com/watch?v=xX10vQEa56E")

shawshank_redemption = media.Movie("The Shawshank Redemption",
                                   "An innocent man is put in jail",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # noqa
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")  # noqa

rang_de_basanti = media.Movie("Rang De Basanti",
                              "Aimless college kids learn revolution",
                              "https://upload.wikimedia.org/wikipedia/en/5/5f/RDB_poster.jpg",  # noqa
                              "https://www.youtube.com/watch?v=9U5gGXvJxO8")

fight_club = media.Movie("Fight Club",
                         "A man's alter-ego creates an underground cult",
                         "http://i.jeded.com/i/fight-club.25541.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

the_waterboy = media.Movie("The Waterboy",
                           "A waterboy becomes a beastly football player",
                           "http://cdn.traileraddict.com/content/touchstone-pictures/thewaterboy.jpg",  # noqa
                           "https://www.youtube.com/watch?v=z8yv9eq5s14")

'''
An array of the instance variables is built and passed into the
open_movies_page function of fresh_tomatoes.py to serve an HTML
page built with the information from these movies
'''
movies = [the_rundown, the_dark_knight, inception, memento, waking_life,
          shawshank_redemption, rang_de_basanti, fight_club, the_waterboy]

fresh_tomatoes.open_movies_page(movies)
