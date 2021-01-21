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

# Ceteris Paribus profile for apartment observation
rf_profile = exp.predict_profile(new_observation = apartment)

# plot Ceteris Paribus profile
rf_profile.plot(variables = ['construction_year', 'surface', 'floor', 'no_rooms'])


