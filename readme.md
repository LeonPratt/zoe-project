## overview ##
This is a project that can be used to extract data from the 'Zoe Personalised Nutrition' app and export this data to a .csv file 
(this is not a feature currently avaliable via the app)

## Requirements ##  

required python libraries:
- [requests](https://github.com/psf/requests) - a simple but very useful HTTP library

## Usage ##

edit the following variables in zoe.py
- 'usr' --> the email or id associated with your zoe account
- 'passwd' --> the password to your zoe account
- 'outputfile_name' --> the path to the .csv file that you want to output to
- 'food_type_list' --> the list of food categories that you wish to export from the app

Run the code and, provided that all details have been entered correctly, a .csv file should be outputted containing data in the following structure:

```
food_category1,
food_1_name, food_1_score,
food_2_name, food_2_score,


food_category2,
food_1_name, food_1_score,
food_2_name, food_2_score
```

## Development ##

This project is much more indepth and complicated than one may first think. This is because of a few reasons:
- There is no public API for the zoe app, and therefore you can't just create an http get request and send it to a zoe server.
- You can't access the data via a website, only through a mobile app. This means that tools such as [Scrapy](https://github.com/scrapy/scrapy) can't be used.  
this means that a bit of reverse engineering needs to be done


  
