# quick-image-fix
quick and dirty browser-based fix for image rotation web bugs

This is a fix for the really stupid issue where sometimes iOS photos end up rotated with exif metadata, which would be great, except that when you try to upload them to the web, Chrome doesn't honor exif rotation, so it goes badly wrong.  Most of the work is actually done [this nice library by Sebastian Tschan](https://github.com/blueimp/JavaScript-Load-Image), which I've checked into here out of sheer laziness.  

It's all pretty self-explanatory.  Upload a badly rotated image, and download an image with the exif rotation replaced by real rotation that Chrome will respect.  

It's really trivial stuff.  

Only meant to be used in recent chrome.  Other browsers might not have exif broken, or might not support the various canvas/blob fuckery in use here.  

If you're annoyed that this is necessary, harass the Chrome people and/or web standards people to fix [this issue that has been open for over seven years](https://bugs.chromium.org/p/chromium/issues/detail?id=56845).

Demo: [http://paul-gowder.com/fix-images/](http://paul-gowder.com/fix-images/)

the cmdlinefix folder also has a python script that wraps some commandline utilities to fix a whole folder of images.  


