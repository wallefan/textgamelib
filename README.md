# jason-0.0.1
A library for text-based games, currently not complete

Jason is a library for creating text-based games using Python and a custom file format loosely based on JSON (hence the name).

I chose the name Jason because many applications have names that have nothing to do with their function, or anything related to programming (example: BeautifulSoup), and I couldn't think of any other name less than 20 characters long.  I also used a file format based on JSON.

I didn't make it a library (so your programs would be written in standard .py) because text-based games output a LOT of (guess what?) text.  A lot of strings in the same .py file make a program really, really confusing.  I considered using gettext but you would still have to pass all your gettext strings to a constructor, which would mean a whole lot of boilerplate code.  I really don't like programs with a lot of boilerplate (which is part of the reason I hate Java) so I didn't want to make that.  I settled on making a file format.  jason as a format is fairly flexible (you can arrange your file more or less however you want, so your strings can be all in one place), you can add arbitrary Python code (I'm currently trying to work out some sort of sandbox) so you can add commands to the interpreter, custom behavior to each object (which I'm guessing will be used fairly often), etc.  

TODO finish the readme
