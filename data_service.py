def get_indicators():
    with open("./data/letter.txt") as line:
        from_file = line.readlines()

    get_indicators = []

    for line in from_file:
        line = line[0:-1]
        line_list = line.split(";")
        get_indicators.append(line_list)

    return get_indicators


def show_indicators(indicators):

    input_code_from = input("с какого\n")
    input_code_to = input("по какой\n")

    for line in indicators:
        if input_code_from <= line[1] <= input_code_to:
            print("Квартал: {} Номер магазина: {} товарообіг плановий: {} товарообіг фактичний: {} чисельність чол плановий: {} чисельність чол фактичний: {}".format(line[0],line[1],line[2],line[3],line[4],line[5]))


def get_shops():
    with open("./data/letter2.txt") as line:
        from_file = line.readlines()

    get_shops = []

    for line in from_file:
        line = line[0:-1]
        line_list = line.split(";")
        get_shops.append(line_list)

    return get_shops


def show_shops(shops):

    input_code_from = input("с какого\n")
    input_code_to = input("по какой\n")

    for line in shops:
        if input_code_from <= line[0] <= input_code_to:
            print("Номер магазина: {}Назва: {}".format(line[0],line[1]))


# 
# indicators = get_indicators()
# show_indicators(indicators)
#
# shops = get_shops()
# show_shops(shops)
