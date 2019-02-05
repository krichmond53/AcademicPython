from tkinter import *  # Import tkinter
class GraphPie():

    def __init__(self, data, width, height):

        # Parse the data into readable values
        def parsedata(self, data):
            each = data.split(',')  # Split and parse for raw data
            for x in range(0, len(each)):
                if x.__mod__(3) == 0:
                    # print(x, each[x][2:])
                    each[x] = each[x][2:]
                elif x.__mod__(3) == 1:
                    # print(x, each[x][2:-1])
                    each[x] = each[x][2:-1]
                elif x == len(each) - 1:
                    # print(x, each[x][2:-3])
                    each[x] = each[x][2:-3]
                elif x.__mod__(3) == 2:
                    # print(x, each[x][2:-2])
                    each[x] = each[x][2:-2]
            return each


        window = Tk()  # Create a window
        window.title("Pie Graph")  # Set title

        # Place self.canvas in the window
        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.pack()

        # Place buttons in frame
        # frame = Frame(window)
        # frame.pack()

        data = parsedata(self, data)
        print(data)

        window.mainloop()  # Create an event loop


    # Display a rectangle
    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")

    # Display an oval
    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill="red",
                                tags="oval")

    # Display an arc
    def displayArc(self):
        self.canvas.create_arc(10, 10, 190, 90, start=0,
                               extent=90, width=8, fill="red", tags="arc")

    # Display a polygon
    def displayPolygon(self):
        self.canvas.create_polygon(10, 10, 190, 90, 30, 50,
                                   tags="polygon")

    # Display a line
    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, fill="red",
                                tags="line")
        self.canvas.create_line(10, 90, 190, 10, width=9,
                                arrow="last", activefill="blue", tags="line")

    # Display a string
    def displayString(self):
        self.canvas.create_text(60, 40, text="Hi, I am a string",
                                font="Times 10 bold underline", tags="string")

    # Clear drawings
    def clearCanvas(self):
        self.canvas.delete("rect", "oval", "arc", "polygon",
                           "line", "string")