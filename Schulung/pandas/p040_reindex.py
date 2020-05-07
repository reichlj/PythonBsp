import pandas as pd

growth = {
   'Switzerland': {'2010': 3.0,'2011': 3.6,'2012': 1.1,'2013': 1.9},
   'Germany':     {'2010': 4.1,'2011': 3.6,'2012': 0.4,'2013': 0.1},
   'France':      {'2010': 2.0,'2011': 2.1,'2012': 0.3,'2013': 0.3},
   'Greece':      {'2010': -5.4,'2011': -8.9,'2012': -6.6,'2013': -3.3},
   'Italy':       {'2010': 1.7,'2011': 0.6,'2012': -2.3,'2013': -1.9}
   }
growth_frame = pd.DataFrame(growth)
growth_frame   = growth_frame.T
growth_frame= growth_frame.reindex(
        ['Switzerland','Italy','Germany','Greece'])
print(growth_frame)

   
