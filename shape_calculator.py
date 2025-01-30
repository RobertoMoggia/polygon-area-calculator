class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width,self.height)

    def set_width(self,width):
        if type(width)==int:
            self.width=width
        else:
            raise(TypeError('Width has to be an int!'))
        
    def set_height(self,height):
        if type(height)==int:
            self.height=height
        else:
            raise(TypeError('Height has to be an int!'))
    
    def get_area(self):
        return self.height*self.width
    
    def get_perimeter(self):
        return (self.height+self.width)*2

    def get_diagonal(self):
        return (self.height**2+self.width**2)**0.5
    
    def get_picture(self):
        height=self.height
        width=self.width
        if width>50 or height>50:
            return 'Too big for picture.'

        picture=['*'*width]
        for i in range(height-2):
            picture.append('*'*width)
        picture.append('*'*width+'\n')
        return '\n'.join(picture)
    
    def get_amount_inside(self,other):
        if not isinstance(other,(Rectangle,Square)):
            raise(TypeError('This method only accepts an istance of class Rectangle or Square.'))

        if self.width<other.width or self.height<other.height:
            return 0
        else:
            return (self.width//other.width)*(self.height//other.height)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def __str__(self):
        return 'Square(side={})'.format(self.width)
    
    def set_side(self,side):
        self.height=side
        self.width=side
    
    def set_height(self, height):
        self.set_side(height)
    
    def set_width(self, width):
        self.set_side(width)