def build_profile(name, surname, **info):
    profile = {'name': name, 'surname': surname}
    for key, value in info.items():
        profile[key] = value
    print(profile)


build_profile('viktor', 'bezai', age='31',
              language='russian', programming='python')
