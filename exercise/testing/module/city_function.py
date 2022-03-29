def loaction(city, country, population=''):
    """Will show the place and loaction of the place in which country it lies."""
    if population:
        place = f"{city}, {country} {population}"
    else:
        place = f"{city}, {country}"
    return place.title()
