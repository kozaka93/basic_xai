#library
library(DALEX)

#apartments dataset from DALEX
#data have 5 numerical variables and 1 factor
head(apartments)

#we use one-hot encoding for district variable - one_hot() function from mltools
data <- mltools::one_hot(data.table::data.table(apartments))

#we created a random forest model using ranger library
library(ranger)
model <- ranger(m2.price~., data = data)

#we created an explainer with DALEX package
explainer <- explain(model, data = data, y = data$m2.price)

