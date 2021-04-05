// border frame refactored
var image = new SimpleImage(200,200);
w = image.getWidth();
h = image.getHeight();

for (var pixel of image.values()) {
    pixel.setRed(0);
    pixel.setGreen(0);
    pixel.setBlue(0);
    
    var x = pixel.getX();
    var y = pixel.getY();
    if ( x < w/2 ) {
        if ( y < h/2  ) {
            pixel.setRed(255);
        }
        else {
            pixel.setRed(255);
            pixel.setBlue(255);
        }
    }
    else {
        if ( y < h/2) {
            pixel.setGreen(255);
        }
        else {
            pixel.setBlue(255);
        }
    }


    
}


print(image);

