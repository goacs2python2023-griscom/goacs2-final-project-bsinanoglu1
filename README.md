This catalyst project is aimed at determining whether there is a correlation between HDI rankings of a country, and mortality rate by injury.

The references for the datasets can be found in my catalyst slideshow: https://docs.google.com/presentation/d/1uAqKx7OXdyFciFhDk8tmUrkLMWAfAkCh6aS_cqR9Jxg/edit?usp=sharing

=======================

> mortality_stats2.csv

Conveniently named, houses the statistics of the mortality statistics of countries and territories recognized by the UN. The dates used are the last year that statistics were recorded for each country, which might lead to some inaccuracies in the way the data is then analyzed. Most of the data is ignored as the only important parts for my investigation include the 'Age_all' field, as I'm not measuring the differences in ages of the casualties.



> hdi_rankings.csv

Also conveniently named, this CSV file includes all of the latest HDI rankings for nations across the world. Does not include all of the nations / territories used in the mortality statistics CSV.



> data_analysis.py

This is my work in analyzing the correlation between the two datasets. In this program, I create three graphs with trend lines in order to find the correlations, as well as preparing the datasets for these graphs.


> data_analysis.html

File created by Bokeh to visualize my graphs in HTML.
