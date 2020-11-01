# we created a model_parts object
mp <- model_parts(explainer, loss_function = loss_root_mean_square)

# we can see a data.frame with results
mp

# we can plot the results
plot(mp)

