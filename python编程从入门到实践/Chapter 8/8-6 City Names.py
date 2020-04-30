def get_city_country(city_name, country_name):
    """Return the full name of the city"""
    full_name = '"' + city_name + ', ' + country_name + '"'
    return full_name.title()


print(get_city_country('beijing', 'china'))
print(get_city_country('new york', 'america'))
print(get_city_country('london', 'england'))
