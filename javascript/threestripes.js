// write your code here
// blue to yellow
var image = new SimpleImage("hilton.jpg");
var width = image.getWidth();

for (var p of image.values()) {
        var x = p.getX();
        //debug("x=",x);
        if ( p.getX() <= width/3 ) {
            p.setRed(255);    
        }
        else if ( p.getX() > 2*(width/3)) {
            p.setBlue(255);    
        }
        else {
            p.setGreen(255);    
        }
}
print(image);

