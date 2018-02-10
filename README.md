# quick-image-fix
quick and dirty browser-based fix for image rotation web bugs

This is a fix for the really stupid issue where sometimes iOS photos end up rotated with exif metadata, which would be great, except that when you try to upload them to the web, Chrome doesn't honor exif rotation, so it goes badly wrong.  Most of the work is actually done [this nice library by Sebastian Tschan](https://github.com/blueimp/JavaScript-Load-Image), which I've checked into here out of sheer laziness.  

It's all pretty self-explanatory.  Upload a badly rotated image, and download an image with the exif rotation replaced by real rotation that Chrome will respect.  

It's really trivial stuff.  
