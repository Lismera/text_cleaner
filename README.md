# Text data NLP cleaner 
This cleaner can be useful for the variety of NLP data cleaning problems.   
It can perform any combination of:
 - Punctuation removal
 - NLTK stopwords modification and removal
 - Conversion of files to the lower case
 - Encoding standardization
 - Non-ascii character removal  
 - Numerical data removal  

You can input either a single file(`'filename.txt'`) or an entire folder(`'full/path/to/file.txt'`)

## Installation

Firstly, ensure you have python >= 3.6 installed on your machine. Then use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install nltk
nltk.download()
```

In order to download the repository, use [git](https://git-scm.com/download/win) from your command line:

```bash
git clone 
```
cd into the cloned folder :  

```bash
cd text_cleaner-master 
```

## Usage

Once in the folder, you can specify how exactly you want your text to be processed. 

__Required parameters__:  
```
-infile 'filename.txt'
```
OR
```  
-infolder 'absolute/path/to/the/folder'
```
__Optional parameters to choose from__:  

```
-ex_stop #applies default nltk stopwords removal  
-pun #removes the punctuation  
-lowc #translates the text to lower case  
-dig #removes numerical data    
```
__Usage examples:__  

`python main.py -infile Name.txt -pun -lowc`   -> this creates a folder "output" in your directory with the file without any punctuation and in lowercase inside it.
   
`python main.py -infolder C:\Users\dell\Desktop\cleaner -dig`  -> this creates a subfolder "output" in the folder specified and outputs there all the .txt files found in that folder without any numerical data


## Modifying the code


If you want to add/change the defaults for any part of the code so it is more relevant to your project:  
1. _Stopwords_  
If you want to modify nltk stopwords list, go to `text_cleaner.py` file and have a look in `exc_stopwords()` function. Uncomment the line you need to add or remove the stopwords.
2. _Punctuation and numerical data_  
If you want to remove only certain punctuation or only certain digits, find in `text_cleaner.py` those sections and change the regex rules accordingly to your needs.  
3. _Change encoding_    
By default, the program reads in `ascii` encoding (which allows to remove all 'weird' text characters prior to further processing) and saves the data in `utf-8` encoding. If you want to save the data in a different encoding, go to the very last lines in `text_cleaner.py` and change the encoding accordingly.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
Developed by Anastasia Ugaste. Do whatever you like with it for any commercial or private projects
