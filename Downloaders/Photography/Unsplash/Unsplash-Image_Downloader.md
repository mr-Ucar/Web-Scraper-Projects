# Unsplash-Image_Downloader

### Download images from the photography website called _"Unsplashed"_ and save/store the images based on the topic. </br> 
I modified this script which works well:  </br> https://github.com/ibuetler/unsplash-image-downloader-python
### *Some modifications:*  
- save the images in subfolders named after the topic
- input validation, logging, sleep module, etc.
### - _You can use the script with command-line arguments or let the user enter the necessary values._

## Usage Method 1:
```
python3 Unsplash-Image_Downloader.py --topic Linux --resolution 1280x1280 --amount 2
python3 Unsplash-Image_Downloader.py --topic hacking --resolution 800x600 --amount 50
python3 Unsplash-Image_Downloader.py --topic Paris --resolution 640x451 --amount 50
python Unsplash-Image_Downloader.py --topic dogs --resolution 1280x1280 --amount 2
```

## Usage Method 2:

You can also let the user provide the necessary values. The screenshot can give an idea:

<img width="892" alt="image" src="https://github.com/emreYbs/unsplash-image-downloader-python/assets/59505246/e4461b36-19f0-4ed4-83b2-b13a3761e881">
