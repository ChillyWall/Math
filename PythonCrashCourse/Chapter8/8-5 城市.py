def describe_city(city_name, included_country='china'):
    print(city_name.title() + " is in " + included_country.title())


describe_city('beijing')
describe_city('zhengzhou')
describe_city('london', 'england')
