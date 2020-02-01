def make_car(brand, model, **equipment):
    car = {'brand': brand, 'model': model}
    for k, v in equipment.items():
        car[k] = v
    print(car)
    return car['brand'], car['model']


chevrolet = make_car('chevrolet', 'lacetti', body_type='sedan', power='1.6')
print(chevrolet)