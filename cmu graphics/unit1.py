from cmu_graphics import *

# Fill me in!

#background
Rect(0, 0, 400, 400, fill=rgb(50, 50, 50))

#stalactites in the background
Polygon(100, 0, 125, 125, 175, 0, fill='darkGrey', opacity=25)
Polygon(250, 0, 305, 150, 325, 0, fill='darkGrey', opacity=25)

#stalagmites in the background
Polygon(100, 400, 155, 275, 175, 400, fill='darkGrey', opacity=25)
Polygon(250, 400, 375, 250, 325, 400, fill='darkGrey', opacity=25)


#lantern post
Rect(190, 250, 20, 150, fill='saddleBrown')

#cave floor and ceiling
Rect(0, 350, 400, 50, fill='darkGrey')
Polygon(0, 0, 0, 65, 75, 55, 175, 75, 250, 70, 400, 65, 400, 0, fill='darkGrey')

#lantern flame
Polygon(200, 210, 220, 235, 200, 250, 180, 235, fill='orange')

#lantern
Oval(200, 225, 70, 60, fill='gold', opacity=75)
Rect(160, 195, 80, 10, fill='saddleBrown')
Rect(160, 250, 80, 10, fill='saddleBrown')

#Light emitted by lantern
Circle(200, 225, 250, fill=gradient('white', 'yellow', 'yellow'), opacity=5)
Circle(200, 225, 200, fill=gradient('white', 'yellow', 'yellow'), opacity=10)
Circle(200, 225, 150, fill=gradient('white', 'yellow', 'yellow'), opacity=15)
Circle(200, 225, 100, fill=gradient('white', 'yellow', 'yellow'), opacity=25)
Circle(200, 225, 50, fill=gradient('white', 'yellow', 'yellow'), opacity=40)

cmu_graphics.run()