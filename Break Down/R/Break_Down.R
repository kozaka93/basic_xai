# Example for R

# apartment which prediction we explain
apartment = data.frame(construction.year = 1995,
                       surface = 93,
                       floor = 7,
                       no.rooms = 3,
                       district_Bemowo = 0,
                       district_Bielany = 0,
                       district_Mokotow = 0,
                       district_Ochota = 1,
                       district_Praga = 0,
                       district_Srodmiescie = 0,
                       district_Ursus = 0,
                       district_Ursynow = 0,
                       district_Wola = 0,
                       district_Zoliborz = 0)

# Break Down for apartment observation
rf_pparts = predict_parts(explainer = explainer, new_observation = apartment, type = "break_down")

# plot Break Down
plot(rf_pparts)