// border frame refactored
var image = new SimpleImage(200,200);
w = image.getWidth();
h = image.getHeight();

for (var pixel of image.values()) {
    pixel.setRed(0);
    pixel.setGreen(255);
    pixel.setBlue(0);
    
    var x = pixel.getX();
    var y = pixel.getY();
    if ( y < h/3 || x < w/3) {
        pixel.setRed(255);
        pixel.setGreen(0);
        pixel.setBlue(0);
    }
    if ( y > 2*h/3) {
        pixel.setBlue(255);
        pixel.setGreen(0);
        pixel.setRed(0)
    }
    
     
}


print(image);

