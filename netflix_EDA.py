import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

#reading the csv file
df = pd.read_csv("netflix_titles.csv", index_col="show_id")

#parsing date in "date_added" column and not while reading the file because of missing/messy values.
df["date_added"] = df.apply(lambda x: x["release_year"] if pd.isna(x["date_added"]) else datetime.strptime(x["date_added"].strip(),"%B %d, %Y"), axis=1)

#creating 2 datasets based on the type of content.
movies = df.loc[df["type"] == "Movie"]
shows = df.loc[df["type"] == "TV Show"]

#plotting a histigrams of different types of content

#first creating a filter function that returns subset of dataframe based on the type of content it is listed under.
def filter(df, filter_col, type):
    filter = lambda x: any(y.lower() in str.lower(x) for y in type)
    return df.loc[df[filter_col].apply(filter)]

#creating a subplot used for plotting
fig, axes = plt.subplots(3,2, figsize=(10,10))

##### MOVIE PLOTS
comedies = filter(movies, "listed_in", ["Comedies", "Comedy"])
documentaries = filter(movies, "listed_in",["Documentaries", "Documentary"])
dramas = filter(movies, "listed_in", ["Dramas", "Drama"])
action = filter(movies, "listed_in", ["Action & Adventure", "Action", "Adventure"])
anime = filter(movies, "listed_in", ["Anime", "Animation", "Animated"])
horror = filter(movies, "listed_in", ["Horror", "Thriller"])

#uncomment the following to see the movies plots:

#comedyplot = comedies["release_year"].plot(kind="hist", bins=73, title="Comedies by Date added", density=True, alpha=0.5, color="green", ax=axes[0,0])
#comedies["release_year"].plot(kind="kde", color="red", ax=comedyplot)
#documentplot = documentaries["release_year"].plot(kind="hist", bins=73, title="Documents by Date added", density=True, alpha=0.5, color="green", ax=axes[0,1])
#documentaries["release_year"].plot(kind="kde", color="red", ax=documentplot)
#dramaplot = dramas["release_year"].plot(kind="hist", bins=73, title="Dramas by Date added", density=True, alpha=0.5, color="green", ax=axes[1,0])
#dramas["release_year"].plot(kind="kde", color="red", ax=dramaplot)
#actionplot = action["release_year"].plot(kind="hist", bins=73, title="Action by Date added", density=True, alpha=0.5, color="green", ax=axes[1,1])
#action["release_year"].plot(kind="kde", color="red", ax=actionplot)
#animeplot = anime["release_year"].plot(kind="hist", bins=73, title="Anime by Date added", density=True, alpha=0.5, color="green", ax=axes[2,0])
#anime["release_year"].plot(kind="kde", color="red", ax=animeplot)
#horrorphot = horror["release_year"].plot(kind="hist", bins=73, title="Horror by Date added", density=True, alpha=0.5, color="green", ax=axes[2,1])
#horror["release_year"].plot(kind="kde", color="red", ax=horrorphot)
#plt.tight_layout()
#plt.show()


#---------------------------------------------------------------------------------------------------------------------------------------
##Our dataset ends in the year 2020, so please take this analysis with a grain of salt. This EDA is created simply for fun and
##practice.
##it is possible that almost every movie dropped in release frequency because of the covid-19 pandemic. we see a significant drop
##in the number of movies released around the year 2019-2020. what is interesting is the sudden rise in the number of documentaries
##released after the pandemic. this may be due to the fact that people were looking for more information, or that documentaries
##might have been filmed more easily in the time of the pandemic. Possible reasons might include:
##lower budget (lower need for investment), Significantly smaller casting number, easier filming conditions (no need for stabilization
##techniques and equipment for cameras, lesser need for special effects and CGI, etc. 
#--------------------------------------------------------------------------------------------------------------------------------




##### SHOW PLOTS
comedy_series = filter(shows, "listed_in", ["Comedies", "Comedy"])
documentary_series = filter(shows, "listed_in", ["Documentaries", "Documentary", "Docuseries", "Docu"])
drama_series = filter(shows, "listed_in", ["Dramas", "Drama"])
action_series = filter(shows, "listed_in", ["Action & Adventure", "Action", "Adventure"])
anime_series = filter(shows, "listed_in", ["Anime", "Animation", "Animated"])
horror_series = filter(shows, "listed_in", ["Horror", "Thriller"])

#uncomment the following to see the series plots:

#comedy_series_plot = comedy_series["release_year"].plot(kind="hist", bins=73, title="Comedies by Date added", density=True, alpha=0.5, color="green", ax=axes[0,0])
#comedy_series["release_year"].plot(kind="kde", color="red", ax=comedy_series_plot)
#documentary_series_plot = documentary_series["release_year"].plot(kind="hist", bins=73, title="Documents by Date added", density=True, alpha=0.5, color="green", ax=axes[0,1])
#documentary_series["release_year"].plot(kind="kde", color="red", ax=documentary_series_plot)
#drama_series_plot = dramas["release_year"].plot(kind="hist", bins=73, title="Dramas by Date added", density=True, alpha=0.5, color="green", ax=axes[1,0])
#drama_series["release_year"].plot(kind="kde", color="red", ax=drama_series_plot)
#action_series_plot = action["release_year"].plot(kind="hist", bins=73, title="Action by Date added", density=True, alpha=0.5, color="green", ax=axes[1,1])
#action["release_year"].plot(kind="kde", color="red", ax=action_series_plot)
#anime_series_plot = anime["release_year"].plot(kind="hist", bins=73, title="Anime by Date added", density=True, alpha=0.5, color="green", ax=axes[2,0])
#anime["release_year"].plot(kind="kde", color="red", ax=anime_series_plot)
#horror_series_plot = horror["release_year"].plot(kind="hist", bins=73, title="Horror by Date added", density=True, alpha=0.5, color="green", ax=axes[2,1])
#horror["release_year"].plot(kind="kde", color="red", ax=horror_series_plot)
#plt.tight_layout()
#plt.show()


#--------------------------------------------------------------------------------------------------------------------------
##Again, our dataset ends in the year 2020, so please take this analysis with a grain of salt. This EDA is created simply for
##fun and practice.
##the plots show similar pattern in the number of series released over time. the numbers drop significantly around the year 2019-2020.
##the number of series released during the pandemic is higher than the number of movies released before the pandemic mainly in 
##the comedy, documentary, and anime. These types being strongly rooted in the entertainment industry. (documentaries maybe further
##strenghtened with the sudden and strong demand for true-crime series these past years).
##the number of movies released in the horror genre is lower than the number of movies released before the pandemic. Which is an
##interesting topic for further observation.
#--------------------------------------------------------------------------------------------------------------------------
