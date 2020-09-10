# Space Instagram

The project allows you to automaticly publish instagram images about space.

There are 2 kinds of images you can publish: SpaceX and Hubble.

SpaceX API provides images about SpaceX launches

Hubble API provides images about space in common, but you can also choose Hubble collections of images: news and spacecraft. Spacecraft mostly provides you with images about spaceships, but if you want to see something more fascinating, I highly recommend you to choose news collection.

Below you can find information about how to work with this script and choose options you want.

### How to install

First of all, you will need an [instagram](https://www.instagram.com/) account.

Now create .env file among all the files you've downloaded and write there the following information (put your instagram login and password instead of gaps):
```
INSTAGRAM_LOGIN = <YOUR_LOGIN>
INSTAGRAM_PASSWORD = <YOUR_PASSWORD>
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
Now you are ready to work with the script

### Usage

Now let's look at what arguments you will need to launch the script ```fetch_spacex.py```

```
python fetch_spacex.py -h
```

```
usage: fetch_spacex.py [-h] [--count COUNT]

optional arguments:
  -h, --help     show this help message and exit
  --count COUNT  count of spacex images to download
```

This command will create ```images/spacex``` folders among other files in the directory and download 10 spacex images into spacex directory

```
python fetch_spacex.py --count 10
```

Let's look at what arguments you will need to launch the script ```fetch_hubble.py```

```
python fetch_hubble.py -h
```

```
usage: fetch_hubble.py [-h] [--id ID] [--collection COLLECTION] [--page PAGE]

optional arguments:
  -h, --help            show this help message and exit
  --id ID               download all hubble images by id
  --collection COLLECTION
                        collection of hubble images to download
  --page PAGE           page of collection of hubble images to download
```

The command below will create ```images/hubble/{collection}``` folders and download hubble images from ```news collection on page 10``` into ```{collection}``` directory and then download all images with ```id 1``` in ```images/hubble``` folder. All arguments are optional, if you choose no arguments you get no result. You can't use ```--page``` without ```--collection```. If ```--page``` argument in not mentioned the script will download images from collection from all pages. You can use only ```--id``` if you just want to get images by certain id.

```
python fetch_hubble --id 1 --collection news --page 10
```

When you're done with choosing options and running these two scripts, run ```resize_images.py``` to scale your images so they will fit into instagram rules. The script will create ```resized_images``` folder where all the successfuly resized images will be stored. No arguments needed.

```
python resize_images.py
```

Run the script below

```
python instagram_bot.py
```

The script is working, space images will be posted one by one into your instagram account around every 60 seconds each. All logs are saved into ```config``` directory.

***WARNING! Changing time between publications ```(time.sleep(<time>))``` to low values or turning it off at all is not recommended as instagram security script may react to this activity and won't allow you to do any publications from 24 hours to 4 days. Also uploading same images or images with same caption is not recommended***

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).