from EventSequence import Off, ColorSelect, Fade, Circle, Bounce, Weather
import color_constants
import pprint
from flask import Flask, redirect, url_for


app = Flask(__name__)
event = Off()
event.start()

@app.route('/ledmode/<mode>')
def hello_guest(mode):

    choice = int(mode)
    event = Off()
    event.start()

    if choice == -1:
        event.stop()
        event.join()

    elif choice == 0:
        event.stop()
        event.join()
        event = Off()
        event.start()
    elif choice == 1:

        while True:
            print("Enter Color Name or")
            print("list (find valid color names) or")
            print("-1 return to main menu")
            color = input()

            if color == 'list':
                list = []
                for key in color_constants.colors:
                    list.append(key)

                pp = pprint.PrettyPrinter(width=70, compact=True)
                pp.pprint(list)
                print()
                continue
            elif color == '-1':
                break

            #check if color in list
            found = False
            for key in color_constants.colors:
                if key == color:
                    found = True
                    break

            if found == False:
                print("Invalid color\n")
                continue


            event.stop()
            event = ColorSelect(color_constants.colors[color])
            event.start()
            print()
    elif choice == 2:
        event.stop()
        event.join()
        event = Fade()
        event.start()
    elif choice == 3:
        event.stop()
        event.join()
        event = Circle()
        event.start()
    elif choice == 4:
        event.stop()
        event.join()
        event = Bounce()
        event.start()
    elif choice == 5:
        event.stop()
        event.join()
        event = Weather()
        event.start()

    return 'Success'


if __name__ == '__main__':
   app.run(debug = True)
    
    


