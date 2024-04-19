import csv
from bokeh.plotting import figure, show
import numpy as np
from bokeh.models import Range1d
from bokeh.layouts import gridplot

# Creates a dictionary with keys of country name, values of HDI ranking

f = open('hdi_rankings.csv')
hdirankings = csv.reader(f)
header = next(hdirankings)

hdirankingsDict = {}

for line in hdirankings:
    try: hdirankingsDict[line[0]] = float(line[2])
    except: continue

f.close()

# Creates three dictionaries with keys of country name, value of mortality via injury per 100,000 population
# Three different dictionaries for All, Male, Female statistics

f2 = open('mortality_stats2.csv')
mortalitystats = csv.reader(f2)
header2 = next(mortalitystats)

mortalitystatsDictMale = {}
mortalitystatsDictFemale = {}
mortalitystatsDictAll = {}

for line in mortalitystats:
    if line[6] == "Age_all":
        if line[5] == "All":
            try: mortalitystatsDictAll[line[3]] = line[11]
            except: continue
        elif line[5] == "Male":
            try: mortalitystatsDictMale[line[3]] = line[11]
            except: continue
        elif line[5] == "Female":
            try: mortalitystatsDictFemale[line[3]] = line[11]
            except: continue

f2.close()

# Organizes all of the data so that each index in both the HDI and mortality array match up
# F.e first index of either array are both for Albania

hdiOrdered = []
mortalityAllOrdered = []
tempkey = ""

translatorCSV = {"Brunei Darussalam": "Brunei", "Syrian Arab Republic": "Syria", "Cabo Verde": "NA", 
"Czechia": "Czech Republic", "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
"China, Hong Kong SAR": "China", "Republic of Moldova": "Moldova", "Russian Federation": "Russia", "T?rkiye": "Turkey",
"Venezuela (Bolivarian Republic of)": "Venezuela", "Iran (Islamic Republic of)": "Iran", "Republic of Korea": "South Korea",
"United States of America": "United States", "Guadeloupe": "NA", "French Guiana": "NA", "Martinique": "NA",
"Mayotte": "NA", "R?union": "NA", "Puerto Rico": "NA"}

for key in mortalitystatsDictAll:
    if key in translatorCSV:
        if translatorCSV[key] == "NA":
            continue
        tempkey = translatorCSV[key]
    else: tempkey = key

    try: mortalityAllOrdered.append(float(mortalitystatsDictAll[key]))
    except: continue
    hdiOrdered.append(float(hdirankingsDict[tempkey]))

# Graphs of the different metrics

fig = figure(title="Death by injury rate per 100 000 population vs HDI ranking of a country")

fig.xaxis.axis_label = "HDI"
fig.yaxis.axis_label = "Death by injury rate per 100 000 population"
fig.y_range = Range1d(0, 300)
fig.x_range = Range1d(0, 1)
fig.circle(hdiOrdered, mortalityAllOrdered, size=3, color = "red")

# A line of best fit in order to show the trendline of the data

mean_x = np.mean(hdiOrdered)
mean_y1 = np.mean(mortalityAllOrdered)
num = 0
denom = 0

for i in range(len(hdiOrdered)):
    num += (hdiOrdered[i] - mean_x) * (mortalityAllOrdered[i] - mean_y1)
    denom += (hdiOrdered[i] - mean_x) ** 2

m = num / denom
c = mean_y1 - (m * mean_x)

x = np.linspace(0, 2, 1000)

fig.line(x, c + m * x)

mortalityMaleOrdered = []
hdiOrdered = []

for key in mortalitystatsDictMale:
    if key in translatorCSV:
        if translatorCSV[key] == "NA":
            continue
        tempkey = translatorCSV[key]
    else: tempkey = key

    try: mortalityMaleOrdered.append(float(mortalitystatsDictMale[key]))
    except: continue
    hdiOrdered.append(float(hdirankingsDict[tempkey]))

fig2 = figure(title="Death by injury rate for per 100 000 male population vs HDI ranking of a country")

fig2.xaxis.axis_label = "HDI"
fig2.yaxis.axis_label = "Death by injury rate per 100 000 male population"
fig2.y_range = Range1d(0, 300)
fig2.x_range = Range1d(0, 1)
fig2.circle(hdiOrdered, mortalityMaleOrdered, size=3, color = "purple")

mean_x = np.mean(hdiOrdered)
mean_y1 = np.mean(mortalityMaleOrdered)
num = 0
denom = 0

for i in range(len(hdiOrdered)):
    num += (hdiOrdered[i] - mean_x) * (mortalityMaleOrdered[i] - mean_y1)
    denom += (hdiOrdered[i] - mean_x) ** 2

m2 = num / denom
c = mean_y1 - (m2 * mean_x)

x = np.linspace(0, 2, 1000)

fig2.line(x, c + m2 * x)

mortalityFemaleOrdered = []
hdiOrdered = []

for key in mortalitystatsDictFemale:
    if key in translatorCSV:
        if translatorCSV[key] == "NA":
            continue
        tempkey = translatorCSV[key]
    else: tempkey = key

    try: mortalityFemaleOrdered.append(float(mortalitystatsDictFemale[key]))
    except: continue
    hdiOrdered.append(float(hdirankingsDict[tempkey]))

fig3 = figure(title="Death by injury rate for per 100 000 female population vs HDI ranking of a country")

fig3.xaxis.axis_label = "HDI"
fig3.yaxis.axis_label = "Death by injury rate per 100 000 female population"
fig3.y_range = Range1d(0, 300)
fig3.x_range = Range1d(0, 1)
fig3.circle(hdiOrdered, mortalityFemaleOrdered, size=3, color = "green")

mean_x = np.mean(hdiOrdered)
mean_y1 = np.mean(mortalityFemaleOrdered)
num = 0
denom = 0

for i in range(len(hdiOrdered)):
    num += (hdiOrdered[i] - mean_x) * (mortalityFemaleOrdered[i] - mean_y1)
    denom += (hdiOrdered[i] - mean_x) ** 2

m3 = num / denom
c = mean_y1 - (m3 * mean_x)

x = np.linspace(0, 2, 1000)

fig3.line(x, c + m3 * x)

p = gridplot([[fig, fig2, fig3]])
show(p)

print(f"Whole population gradient: {str(m)}\nMale population gradient: {str(m2)}\nFemale population gradient: {str(m3)}")