def city_country(city, country):
    return city.title() + ', ' + country.title()


kiev = city_country('kyiv', 'ukraine')
moscow = city_country('moscow', 'russia')
minsk = city_country('minsk', 'belarus')


print(kiev)
print(moscow)
print(minsk)
