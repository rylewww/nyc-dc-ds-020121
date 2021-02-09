def most_popular_artist(our_data):
    
    counter_dict = {}
    for artist in all_artists(our_data): #loops over list of the artists for all albums includes repeats
        if artist in counter_dict: #checking to see if artist alread in counter_dict
            counter_dict[artist] += 1 #if it is, increment by 1
        else: #if 
            counter_dict[artist] = 1 #add artist to the dictionary
    maximum_albums = max(counter_dict.values())
    artist_lists = []
    for keys, values in counter_dict.items():
        if values == maximum_albums:
            artist_lists.append(keys) 
    return artist_lists


###Import data###
import csv
from collections import OrderedDict
with open('data.csv') as f:
        
    reader = csv.DictReader(f)
    songs = [{k:v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]



## Find by name ##
def album_name(string, data):
    for album in data:
        if album['album'] == string:
            return albums
        else:
            return None 
            
##Find by year##
def album_rank(string, data):
    for albums in data:
        if albums['number'] == string:
            return albums
        else:
            None

 ##Return list by year##        
def album_year(string, data):
    song_year = []
    for albums in data:
        if albums['year'] == string:
            song_year.append(albums)
        else:
            None
    return song_year    


##Find by years#
def album_in_years(start, end, data):
    song_years = []
    for albums in data:
        if int(albums['year']) >= start and int(albums['year']) <= end:
            song_years.append(albums)
    return song_years

##Find by ranks##
def album_in_ranks(start, end, data):
    song_ranks = []
    for albums in data:
        if int(albums['number']) >= start and int(albums['number']) <= end:
            song_ranks.append(albums)
        else:
            None
    return song_ranks   

##All titles##
def all_titles(data):
    title_list=[]
    for albums in data:
        title_list.append(albums['album'])
    return title_list
            
##All artists##
def all_artists(data):
    artist_list=[]
    for albums in data:
        artist_list.append(albums['artist'])
    return artist_list

def all_artists(data):
    artist_list=[]
    for albums in data:
        artist_list.append(albums['artist'])
    return list(set(artist_list))


##Artists with the most albums##
def all_artists(data):
    artist_list=[]
    for albums in data:
        artist_list.append(albums['artist'])
    return artist_list


def top_artist(data):
    return max(all_artists(songs), key=all_artists(songs).count)

Or use example code?
        
##Most popular word##    
def top_word(songs):
    words = []
    for word in all_titles(songs):
        words.append(word.split())
    flat_list= []
    for sublist in words:
        for item in sublist:
            flat_list.append(item)
    return max(flat_list, key = flat_list.count)

##attempt 2
def most_popular_word(our_data):
    
    counter_dict = {}
    for word in all_titles(our_data): 
        if word in counter_dict: 
            counter_dict[word] += 1 
        else: #if 
            counter_dict[word] = 1
    maximum_word = max(counter_dict.values())
    word_lists = []
    for keys, values in counter_dict.items():
        if values == maximum_word:
            word_lists.append(keys) 
    return word_lists 

##Histogram of albums by decade ##

import matplotlib.pyplot as plt

def decade_list(data):
    years = [(int(album['year'])//10*10) for album in songs]
    return years

decade_list(songs)


fig, ax = plt.subplots(figsize=(12,12))
plt.hist(decade_list(songs), bins = 7)
ax.set_xlabel('Decades')
ax.set_ylabel('Album Count')
ax.set_title('Distribution Top 500 Albums by Decade')
plt.show()

###break out all genres into a single list###

def all_genres(data):
    genre_list = [genre['genre'] for genre in data]
    return genre_list

def broken_out_genre(songs):
    genres = []
    for genre in all_genres(songs):
        genres.append(genre.split(", "))
    flat_list_genre= []
    for sublist in genres:
        for item in sublist:
            flat_list_genre.append(item)
    return flat_list_genre

##Histogram by genre  ##
import matplotlib.pyplot as plt

  
fig, ax = plt.subplots(figsize=(20,12))
plt.hist(broken_out_genre(songs), bins = 10)
plt.xticks(broken_out_genre(songs), rotation = 60)
plt.show()

##turning txt file list into a dictionary##
def ranking():
    rank_items = []
    for line in list_songs:
        rank_dict = {}
        rank_dict["Rank"]=line[0]
        rank_dict["Name"]=line[1]
        rank_dict["Artist"]=line[2]
        rank_dict["Year"]=line[3][:-1]
        rank_items.append(rank_dict)
    return rank_items


##albumsWithTopSongs - returns a list with the name of only the albums that have tracks featured on the list of top 500 songs##
def albumsWithTopSongs(data):
    albums_list = [album['album'] for album in data]
    return (albums_list)

##