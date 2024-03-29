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

As the zoe app is only availiable on mobile devices, I had 3 choices. I could either download the app on an IOS device, android device or an android emulator. I chose to use the andoid emulator called Bluestacks X as it is the least complicated option. From here I ran the zoe app on the emulator and logged in and browsed the main menu while I had a wireshark running. This allowed me to identify IP adresses of zoe servers but not much more, as all data was encrypted with TLS. therefore I needed to find a different way to view the raw http requests.

The next step was to root bluestacks, which is just a matter of editing the emulator's config file. From there, I used the ADB - android debug bridge to setup and connect to a man in the middle proxy. This would then allow me to see how the data is being sent to and from the zoe servers, allowing me to reverse engineer the exact http requests that are required in order to extract the food data. .

Now that I had figured out the exact http requests needed, all I had to do was make my own requests with python. For this, I used the aformentioned 'requests' library, which I found extremely useful for this job as as it makes using authentification tokens, csrf tokens and session id's very easy. 

After sending the http requests that I made, it is just a matter of manipulating and parsing the response into a .csv file.
  
