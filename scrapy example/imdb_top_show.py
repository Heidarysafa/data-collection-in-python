# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 20:34:39 2020

@author: Moji HSsafa
"""

import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt 
shows = pd.read_csv('C:\\Users\\Moji\\Documents\\spiders\\imdb_spider\\top_shows.csv')

shows['Genre_list'] = shows['genre'].str.split(',')
all_genre_tags = shows['Genre_list'].sum()

popular_genre = Counter(all_genre_tags)
popular_genre.most_common()
plt.bar(popular_genre.keys(), popular_genre.values())
 