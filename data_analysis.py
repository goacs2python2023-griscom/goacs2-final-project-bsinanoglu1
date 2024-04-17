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

f2 = open('mortality_stats.csv')
mortalitystats = csv.reader(f2)
header2 = next(mortalitystats)

mortalitystatsDictMale = {}
mortalitystatsDictFemale = {}
mortalitystatsDictAll = {}

for line in mortalitystats:
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

for key in mortalitystatsDictAll:
    try: mortalityAllOrdered.append(float(mortalitystatsDictAll[key]))
    except: continue
    hdiOrdered.append(float(hdirankingsDict[key]))

# Graphs of the different metrics

fig = figure(title="Death by injury rate per 100 000 population vs HDI ranking of a country")

fig.xaxis.axis_label = "HDI"
fig.yaxis.axis_label = "Death by injury rate per 100 000 population"
fig.y_range = Range1d(0, 3000)
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

show(fig)