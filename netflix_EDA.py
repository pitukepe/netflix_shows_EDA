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

comedies = filter(movies, "listed_in", ["Comedies", "Comedy"])
documentaries = filter(movies, "listed_in",["Documentaries", "Documentary"])
dramas = filter(movies, "listed_in", ["Dramas", "Drama"])
action = filter(movies, "listed_in", ["Action & Adventure", "Action", "Adventure"])
anime = filter(movies, "listed_in", ["Anime", "Animation", "Animated"])
horror = filter(movies, "listed_in", ["Horror", "Thriller"])

fig, axes = plt.subplots(3,2, figsize=(10,10))

comedyplot = comedies["release_year"].plot(kind="hist", bins=73, title="Comedies by Date added", density=True, alpha=0.5, color="green", ax=axes[0,0])
comedies["release_year"].plot(kind="kde", color="red", ax=comedyplot)

documentplot = documentaries["release_year"].plot(kind="hist", bins=73, title="Documents by Date added", density=True, alpha=0.5, color="green", ax=axes[0,1])
documentaries["release_year"].plot(kind="kde", color="red", ax=documentplot)

dramaplot = dramas["release_year"].plot(kind="hist", bins=73, title="Dramas by Date added", density=True, alpha=0.5, color="green", ax=axes[1,0])
dramas["release_year"].plot(kind="kde", color="red", ax=dramaplot)

actionplot = action["release_year"].plot(kind="hist", bins=73, title="Action by Date added", density=True, alpha=0.5, color="green", ax=axes[1,1])
action["release_year"].plot(kind="kde", color="red", ax=actionplot)

animeplot = anime["release_year"].plot(kind="hist", bins=73, title="Anime by Date added", density=True, alpha=0.5, color="green", ax=axes[2,0])
anime["release_year"].plot(kind="kde", color="red", ax=animeplot)

horrorphot = horror["release_year"].plot(kind="hist", bins=73, title="Horror by Date added", density=True, alpha=0.5, color="green", ax=axes[2,1])
horror["release_year"].plot(kind="kde", color="red", ax=horrorphot)

#showing the plots
plt.tight_layout()
plt.show()

##it is possible that almost every movie dropped in release frequency because of the covid-19 pandemic. we see a significant drop
##in the number of movies released around the year 2019-2020. what is interesting is the sudden rise in the number of documentaries
##released after the pandemic. this may be due to the fact that people were looking for more information, or that documentaries
##might have been filmed more easily in the time of the pandemic. Possible reasons might include:
##lower budget (lower need for investment), Significantly smaller casting number, easier filming conditions (no need for stabilization
##techniques and equipment for cameras, lesser need for special effects and CGI, etc. 


