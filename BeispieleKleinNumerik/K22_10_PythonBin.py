from collections import Counter
def create_bins(lower_bound,width, quantity):
    bins=[]
    for low in range(lower_bound,
                     lower_bound+(quantity-1)*width+1,
                     width):
        bins.append((low,low+width))
    return bins

def find_bin(value,bins):
    for k in range(0,len(bins)):
        if bins[k][0]<= value and value < bins[k][1]:
            return k
    return -1

bins = create_bins(lower_bound=50,
                   width=4,
                   quantity=10)
print(bins)
weigths = [73.4, 69.3, 64.9, 75.6, 74.9, 80.3,
           78.6, 84.1, 88.9, 90.3, 83.4, 69.3,
           52.4, 58.3, 67.4, 74.0, 89.3, 63.4]
binned_weights = []
for value in weigths:
    bin_index = find_bin(value,bins)
    print(value,bin_index,bins[bin_index])
    binned_weights.append(bin_index)

frequencies = Counter(binned_weights)
print(frequencies)