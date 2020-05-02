def make_car(company, name, **car_information):
    information = {}
    information['company'] = company.title()
    information['name'] = name.title()
    for key, value in car_information.items():
        information[key] = value
    return information


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
