import pandas as pd
def create_bins(lower_bound,width, quantity):
    bins=[]
    for low in range(lower_bound,
                     lower_bound+(quantity-1)*width+1,
                     width):
        bins.append((low,low+width))
    return bins

weigths = [ 73.4, 69.3, 64.9, 75.6, 74.9, 80.3,
            78.6, 84.1, 88.9, 90.3, 83.4, 69.3,
            52.4, 58.3, 67.4, 74.0, 89.3, 63.4 ]
categorical_object = pd.cut(weigths,18)
print(categorical_object)

bins = create_bins(lower_bound=50,
                   width=4,
                   quantity=10)
print(bins)
sequence_of_scalars =[x[0] for x in bins]
print(sequence_of_scalars)