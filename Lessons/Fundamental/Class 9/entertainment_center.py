import fresh_tomatoes
import media

# Movies
the_goonies = media.Movie("The Goonies",
                    "In order to save their home from foreclosure, a group of misfits set out to find a pirate's ancient valuable treasure.",
                    "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Goonies.jpg",
                    "https://www.youtube.com/watch?v=hJ2j4oWdQtU")

ff7_advent_children = media.Movie("FF VII: Advent Children",
                                "An ex-mercenary is forced out of isolation when three mysterious men kidnap and brainwash the city's children afflicted with the Geostigma disease.",
                                "https://upload.wikimedia.org/wikipedia/en/1/18/Final_Fantasy_VII_Advent_Children_poster.jpg",
                                "https://www.youtube.com/watch?v=QuX104MeuwE")

deja_vu = media.Movie("Deja Vu",
                    "After a ferry is bombed in New Orleans, an A.T.F. agent joins a unique investigation using experimental surveillance technology to find the bomber, but soon finds himself becoming obsessed with one of the victims.",
                    "https://upload.wikimedia.org/wikipedia/en/c/cf/DejaVuBigPoster.jpg",
                    "https://www.youtube.com/watch?v=fCbEqNRIRwc")

the_butterfly_effect = media.Movie("The Butterfly Effect",
                    "Evan Treborn suffers blackouts during significant events of his life. As he grows up, he finds a way to remember these lost memories and a supernatural way to alter his life by reading his journal.",
                    "https://upload.wikimedia.org/wikipedia/en/4/43/Butterflyeffect_poster.jpg",
                    "https://www.youtube.com/watch?v=B8_dgqfPXFg")

robocop = media.Movie("Robocop",
                    "In a dystopic and crime-ridden Detroit, a terminally wounded cop returns to the force as a powerful cyborg haunted by submerged memories.",
                    "https://upload.wikimedia.org/wikipedia/en/1/16/RoboCop_%281987%29_theatrical_poster.jpg",
                    "https://www.youtube.com/watch?v=zbCbwP6ibR4")

the_neverending_story = media.Movie("The NeverEnding Story",
                    "A troubled boy dives into a wondrous fantasy world through the pages of a mysterious book.",
                    "https://upload.wikimedia.org/wikipedia/en/9/9b/Neverendingstoryposter.jpg",
                    "https://www.youtube.com/watch?v=UeFni9dOv7c")

movies = [the_goonies, ff7_advent_children, deja_vu, the_butterfly_effect, robocop, the_neverending_story]
fresh_tomatoes.open_movies_page(movies)