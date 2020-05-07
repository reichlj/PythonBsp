num_labels = 4
labels = np.random.randint(4, size=6)[:,None]
labels
labels_one_hot = (np.arange(num_labels) == labels).astype(np.float64)
labels_one_hot
