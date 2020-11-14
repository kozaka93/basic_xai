
# PDP profile for surface and construction.year variable
rf_mprofile = exp.model_profile(variables = ["surface", "construction_year"] , type = "partial")

# plot PDP
rf_mprofile.plot()

# PDP profile for surface and construction.year variable grouped by no.rooms
rf_mprofile_group = exp.model_profile(variables = ["surface", "construction_year"], groups = "no_rooms", type = "partial")

# plot PDP
rf_mprofaile_group.plot()

# create a linear regresion model
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X,y)

# create an explainer for linear regresion model
exp_lm = dx.Explainer(lm, X, y)

# PDP profile for surface and construction.year variable
lm_mprofile = exp_lm.model_profile(variables = ["surface", "construction_year"] , type = "partial")

# comparison for random forest and linear regression model
rf_mprofile.plot(lm_mprofile)