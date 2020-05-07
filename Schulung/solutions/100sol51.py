PersAnz = np.array([[100,175,210],[90,160,150],[200,50,100],[120,0,310]])
Preis_per_100_g = np.array([2.98,3.90,1.99])
Preis_in_Cent = np.dot(PersAnz,Preis_per_100_g)
Preis_in_Euro = Preis_in_Cent / np.array([100,100,100,100])
Preis_in_Euro
