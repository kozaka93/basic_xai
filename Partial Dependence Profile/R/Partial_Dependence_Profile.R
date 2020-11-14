# PDP profile for surface and construction.year variable
rf_mprofile <- model_profile(explainer = explainer, variables = c("surface", "construction.year"), type = "partial")

# plot PDP
plot(rf_mprofile)

# PDP profile for surface and construction.year variable grouped by no.rooms
rf_mprofile_group <- model_profile(explainer = explainer, variables = c("surface", "construction.year"), groups = "no.rooms", type = "partial")

# plot PDP
plot(rf_mprofile_group)

# create a linear regresion model
model_lm <- lm(m2.price~., data = data)

# create an explainer for linear regresion model
explainer_lm <- explain(model_lm, data = data, y = data$m2.price)

# PDP profile for surface and construction.year variable
lm_mp <- model_profile(explainer = explainer_lm, variables = c("surface", "construction.year"))

# comparison for random forest and linear regression model
plot(rf_mprofile, lm_mprofile)