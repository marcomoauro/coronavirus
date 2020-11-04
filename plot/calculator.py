def calculate_data(csv_dict, field):
    if field == 'deceduti':
        return calculate_deceduti(csv_dict)
    if field == 'terapia_intensiva':
        return calculate_terapia_intensiva(csv_dict)

    d = []
    for row in csv_dict:
        d.append(int(row[field]))
    return d


def calculate_deceduti(csv_dict):
    temp = []
    for row in csv_dict:
        temp.append(int(row['deceduti']))
    pred = temp[0]
    d = [pred]
    for dec in temp[1:]:
        d.append(dec - pred)
        pred = dec
    return d


def calculate_terapia_intensiva(csv_dict):
    total_seats = 6628
    d = []
    for row in csv_dict:
        d.append(int(row['terapia_intensiva']) / total_seats)
    return d
