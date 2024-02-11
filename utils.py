def movie_stars(movie_dict):
  for movie in movie_dict:
    movie['stars'] = add_stars(movie['rating'])
  return movie_dict

def add_stars(rating):
  my_return = ""
  for x in range(5):
    full_star = "fa-star" if rating >= x + 1 else "fa-star"
    half_star = "fa-star-half-full" if 0 < rating - x < 1 else ""
    checked_star = "checked" if rating >= x + 0.5 else ""
    my_return += f"<span class=\"fa {full_star} {half_star} {checked_star}\"></span>"
  return my_return

