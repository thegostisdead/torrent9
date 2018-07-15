# torrent9 explorer ![Python](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

This python script makes it possible to make researches on the website of torrents, "torrent9" and then the downloaded ones. 
You can search everything, series, movies, musics, ebooks, pc-games, etc... 


## Setup && Requierments
* Python 3.3 and up needed  
install the requirements   
```$ pip install cmd2```
And now start the bootstrap.py into shell 
```$ python bootstrap.py ```
### Basic commands
``` help``` to list all the commands  
``` search ``` to make a search on website  
```downloadlist ``` to download the id who want be downloaded  
# Command exemple :
to search somthing : ```search "one piece" -limit 20 -stack 100```
to download : ```downloadlist 99,100,98,72-75``` 
###### Searching:  
```python  
t9explore $> search "the flash"  
t9explore $> search "arrow" -limit 28 -stack 100  
t9explore $> search "blindspot" -cut 150 -limit 30  
```  
| Arguments |                                         Description                                         | Default values | Minimum Values | required |
|:---------:|:-------------------------------------------------------------------------------------------:|:--------------:|:--------------:|:--------:|
|   -limit  | Define a search "page" limit, the program will stop analysing next page if limit is reached |        1       |        1       |    no    |
|    -cut   |                         Stop printing items after this limit reached                        |       10       |        1       |    no    |
|   -stack  |   Kind of useless, but it allow you to define the "max item in a page" when printing items  |       100      |        1       |    no    |
###### Downloading:  
```python 
t9explore $> downloadlist 12  
t9explore $> downloadlist 48-52  
t9explore $> downloadlist 99,100,98,72-75
```   
|            command prefix           |                     id                    |            Description            |
|:-----------------------------------:|:-----------------------------------------:|:---------------------------------:|
|             downloadlist            |                84,65,33-64                | SingleItem,SingleItem,Range-Items |
| command to download .torrent files  | ids printed in the cell after the search  | For the range : StartItem-endItem |
  
![ezgif com-optimize](https://user-images.githubusercontent.com/25646890/42424341-1390d752-830b-11e8-9f81-e4e129fddbc0.gif)
#### Authors

* **Caceres Enzo** - [Caceresenzo](https://github.com/Caceresenzo/)
* **Dorian Hardy** - [thegostisdead](https://github.com/thegostisdead/)

