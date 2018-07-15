# torrent9explorer
This python script makes it possible to make researches on the website of torrents,  "torrent9"  and then the downloaded ones
Python Version : python 3 

## Setup 
install the requirements 
```pip install cmd2```
And now start the bootstrap.py 
``` python bootstrap.py ```
### Basic commands
``` help``` to list all the commands  
``` search ``` to make a search on website  
```dl ``` to download the id who want be downloaded  
# Command exemple :
to search somthing : ```search "one piece" -limit 20 -stack 100```
to download : ```downloadlist 99,100,98,72-75``` 
###### Searching:
```t9explore $> search "the flash"```
```t9explore $> search "arrow" -limit 28 -stack 100```
```t9explore $> search "blindspot" -cut 150 -limit 30```
###### Downloading:
```t9explore $> downloadlist 12``` 
```t9explore $> downloadlist 48-52``` 
```t9explore $> downloadlist 99,100,98,72-75``` 

  
![ezgif com-optimize](https://user-images.githubusercontent.com/25646890/42424341-1390d752-830b-11e8-9f81-e4e129fddbc0.gif)
#### Authors

* **Caceres Enzo** - [Caceresenzo](https://github.com/Caceresenzo/)
* **Dorian Hardy** - [thegostisdead](https://github.com/thegostisdead/)
