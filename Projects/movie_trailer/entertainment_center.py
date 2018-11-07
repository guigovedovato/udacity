import fresh_tomatoes
import media


print("Starting...")
# My Favorite Movies - instance of media.Movie
the_goonies = media.Movie(
    'The Goonies',
    "https://www.youtube.com/watch?v=hJ2j4oWdQtU")

ff7_advent_children = media.Movie(
    "Final Fantasy VII: Advent Children",
    "https://www.youtube.com/watch?v=QuX104MeuwE")

deja_vu = media.Movie(
    "Deja Vu",
    "https://www.youtube.com/watch?v=fCbEqNRIRwc")

the_butterfly_effect = media.Movie(
    "The Butterfly Effect",
    "https://www.youtube.com/watch?v=B8_dgqfPXFg")

robocop = media.Movie(
    "Robocop",
    "https://www.youtube.com/watch?v=zbCbwP6ibR4")

the_neverending_story = media.Movie(
    "The NeverEnding Story",
    "https://www.youtube.com/watch?v=UeFni9dOv7c")

# List of my favorite movies to show on the website
movies = [the_goonies,
          ff7_advent_children,
          deja_vu,
          the_butterfly_effect,
          robocop,
          the_neverending_story]

print("Movies loaded successfully")
print("Generating HTML file")
# Calling fresh_tomatoes.open_movies_page to generates a HTML file
fresh_tomatoes.open_movies_page(movies)
print("Opening HTML file")
