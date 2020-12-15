from data_service import get_indicators, get_shops

temp_analysis_goods_handiling_assets = {
    'nameshop'                  : '', # назва магазину
    'quarter'                   : '', # Квартал
    'planed_goods_turnover'     : 0, # Товарообіг плановий
    'planed_factual'            : 0, # товарообіг фактичний
    'percentage_of_perfomance'  : 0, # відсотки виконання
    'productivity_planed'       : 0, # Продуктивність планова
    'productivity_is_actual'    : 0, # продуктивність фатична
}

def get_analytycs():

    def get_name_shop(code):

        for key in directorys:
            if int(key[0]) == int(code):
                return key[1]

        return "Название магазина не найдено!"


    analitycs_list = []

    indexes = get_indicators()
    directorys = get_shops()

    for indexe in indexes:
        temp = temp_analysis_goods_handiling_assets.copy()

        temp["nameshop"]                    = get_name_shop(indexe[1])
        temp["quarter"]                     = indexe[0]
        temp["planed_goods_turnover"]       = indexe[2]
        temp["planed_factual"]              = indexe[3]
        temp["percentage_of_perfomance"]    = round( (100 * float(indexe[3]) ) / float(indexe[2]), 2)
        temp["productivity_planed"]         = round(float(indexe[2]) / float(indexe[4]), 2)
        temp["productivity_is_actual"]      = round(float(indexe[3]) / float(indexe[5]), 2)

        analitycs_list.append(temp)

    return analitycs_list





analytyc = get_analytycs()

print(analytyc)
