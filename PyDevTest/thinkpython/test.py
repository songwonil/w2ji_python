import math as a
a1= type(42)
b1 = type('42')
print( a1,b1)
print( a1 )
print( 3**3 )
print( a.sqrt(2) )
degrees = 45
x = a.sin( degrees  / 360 * 2 *a.pi )
print(x)
x = a.exp( a.log(x+1) )
print(x)

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    
    print("I sleep all night and I work all day.")

print_lyrics()
print( print_lyrics )
a= print_lyrics
print(a)
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

def print_twice(b):
    print(b * 2)

print_twice('15151515151'*5)
print_twice(3.14)










