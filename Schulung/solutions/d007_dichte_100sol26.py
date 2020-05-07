import urllib.request
url = "https://www.python-course.eu/material/texts/bundeslaender.txt"
with urllib.request.urlopen(url) as fh:
    with open("bundeslaender.txt", "w") as fhw:
        fh.readline()
        for line in fh:
            line = line.decode("iso8859-1")   #  "utf-8" 
            land, area, male, female = line.split()
            population = int(male) + int(female)
            area_sq_km = population / float(area) * 1000
            output = land + " " + str(area)
            output += " " + str(population) + " " + str(area_sq_km)
            fhw.write( output + "\n" )
