# Example for Python

# apartment which prediction we explain
apartment = pd.DataFrame({'construction_year'   : [1995],
                          'surface'             : [93],
                          'floor'               : [7],
                          'no_rooms'            : [3],
                          'district_Bemowo'     : [0],
                          'district_Bielany'    : [0],
                          'district_Mokotow'    : [0],
                          'district_Ochota'     : [1],
                          'district_Praga'      : [0],
                          'district_Srodmiescie': [0],
                          'district_Ursus'      : [0],
                          'district_Ursynow'    : [0],
                          'district_Wola'       : [0],
                          'district_Zoliborz'   : [0]},
                          index = ['Apartment'])

# Shapley values for apartment observation
rf_pparts = exp.predict_parts(new_observation = apartment, type = "shap")

# plot Shapley values
rf_pparts.plot()
