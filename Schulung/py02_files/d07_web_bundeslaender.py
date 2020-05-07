import urllib.request

url = "https://www.python-course.eu/material/texts/bundeslaender.txt"

with urllib.request.urlopen(url) as fh:
    with open('bundeslaender_neu.txt','w') as fhw:
        fhw.write('Land Flaeche Einwohnerzahl Einwohner pro qkm\n')        
        fh.readline()
        for line in fh:
            line = line.decode('iso8859-1')
            state, area, male, female =  line.split()
            population = int(male) + int(female)
            pop_per_sq_km = population/float(area)*1000
            dichte = '{0:8.2f}'.format(pop_per_sq_km)
            output = state + ' ' + area + ' ' + str(population) + ' ' + dichte 
            #output = state + ' ' + area + ' ' + str(population) + ' ' + str(pop_per_sq_km) 
            fhw.write(output + '\n')
