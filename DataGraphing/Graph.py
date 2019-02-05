from tkinter import *  # Import tkinter
import math

class Graph(Canvas):
  def __init__(self, parent, data, width, height):
    self.parent = parent
    self.data = data
    self.width = width
    self.height = height

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

  # Create a window
  def makeWindow(self, title):
    window = Tk()  # Create a window
    window.title(title)  # Set title
    return window

  # Place self.canvas in the window
  def makeCanvas(self, window, width, height):
    self.canvas = Canvas(window, width=width, height=height)
    self.canvas.pack()
    return self.canvas


class GraphBar(Graph):
  def __init__(self, parent, data, width, height):
    super().__init__(parent, data, width, height)

    window = Graph.makeWindow(self, "Bar Graph")
    canvas = Graph.makeCanvas(self,window,width,height)
    data = Graph.parsedata(self, data)
    # print(data)

    # Create the graph
    frame = Frame(window)
    frame.pack()
    segNum = len(data)/3          # Num of segments required in graph
    # print(width)
    trueWidth = int(width) - 20   # Leave 10 on each side to make it look pretty
    wpb = trueWidth/segNum        # Width Per Bar
    goodHeight = int(height)-25   # Total height with room on top and bottom for label
    maxHeight = data[0]           # Tallest Bar
    for x in range(0,len(data)):  # Determine bar max height
      if x.__mod__(3)==0:
        # print("Max Height is", maxHeight)
        if data[x] > maxHeight:
          maxHeight = data[x]

    i = 0
    cw = 10 + wpb   # Current Width
    nw = 0          # Next Width
    while i < len(data):
      d = float(data[i])
      m = float(maxHeight)
      g = float(goodHeight)
      h = float(height)

      if i == 0:
        newVal = h-d/m*g
        canvas.create_rectangle(10, newVal, cw, 185, fill = data[i+2])
        textPos = (10+cw)/2
        canvas.create_text(textPos, 195, text=data[i+1], font='Times 10 bold',
                           justify='center')
        nw = cw+wpb
        i += 3
      else:
        newVal = h-d/m*g
        canvas.create_rectangle(cw, newVal, nw, 185, fill=data[i + 2])
        textPos = (nw + cw) / 2
        canvas.create_text(textPos, 195, text=data[i + 1], font='Times 10 bold',
                           justify='center')
        cw = nw
        nw += wpb
        i += 3

    # window.mainloop()  # Create an event loop


class GraphPie(Graph):
  def __init__(self, parent, data, width, height):
    super().__init__(parent, data, width, height)

    window = Graph.makeWindow(self, "Pie Graph")
    canvas = Graph.makeCanvas(self,window,width,height)
    data = Graph.parsedata(self, data)
    print(data[0], data[1], data[2])
    print(data[3], data[4], data[5])

    # Create the graph
    frame = Frame(window)
    frame.pack()

    numSlice = len(data)/3
    # print('Number of slices', numSlice)

    totalSlice = 0                  # Will add all values to get slice size
    for x in range(0, len(data)):   # Determine bar max height
      if x.__mod__(3) == 0:
        totalSlice += int(data[x])

    # print("Total Slice is", totalSlice)

    i = 0
    nextStart = 0                   # Where the next arc will start
    buffer = 0                      # L/R buffer to center pie chart
    radius = 0
    h = int(height)
    w = int(width)
    if w > h:
      buffer = (w-h)/2
      radius = (h-h*.1)/2
    else:
      buffer = (h-w)/2
      radius = (w-w*.1)/2

    # print('Buffer =', buffer)
    # print('Radius =', radius)

    midX = w/2
    midY = h/2
    # print('Midpoint (x/y)',midX,midY)

    while i< len(data):
      d = float(data[i])            # Must be floats to get %
      m = float(totalSlice)         # Must be floats to get %
      size = d/m*360                # Angle for this part of the data

      # print(d,m, size)

      if i == 0:                    # First slice starts at 0
        self.canvas.create_arc(10+buffer, 10, h-10+buffer, h-10, start=0,
                               extent=size, fill=data[i+2])
        nextStart = size
        # print('First arc goes from 0 to',nextStart)
        midarc = float(size) / 2
        midRadians = midarc*math.pi/180
        # print('The middle of this arc is', midarc)
        x = midX + radius * math.cos(midRadians)
        y = midY + radius * math.sin(midRadians)
        # print (x,y)
        canvas.create_text(x, h-y, text=data[i+1], font='Times 12 bold',
                           justify='center')


        i += 3
      else:                         # Other slices start from where prev slice ended
        self.canvas.create_arc(10+buffer, 10, h-10+buffer, h-10, start=nextStart,
                               extent=size, fill=data[i + 2])
        # print('Next arc starts at',nextStart,'and goes',size,'to',nextStart+size)


        midarc = (size/2)+nextStart
        midRadians = midarc*math.pi/180
        # print('The middle of this arc is', midarc)
        x = midX + radius * math.cos(midRadians)
        y = midY + radius * math.sin(midRadians)
        # print (x,y)
        canvas.create_text(x, h-y, text=data[i+1], font='Times 12 bold',
                           justify='center')

        nextStart += size
        i += 3

    # canvas.create_text(210,100, text="0", font='Times 10 bold',
    #                    justify='center')
    # canvas.create_text(120,190, text="90", font='Times 10 bold',
    #                    justify='center')
    # canvas.create_text(30,100, text="180", font='Times 10 bold',
    #                    justify='center')
    # canvas.create_text(120,10, text="270", font='Times 10 bold',
    #                    justify='center')
    window.mainloop()  # Create an event loop

def main():

  # Open file for input
  infile = open("graphData.txt", "r")

  p = NONE
  line = infile.readline()
  while line != '':
    part = line.split('\t')  # Split data by tabs

    chartType = part[0]  # Type of chart to be used
    d = part[1]  # Data to be parsed and displayed on graph
    w = part[2]  # Width of the window
    h = part[3]  # Length of the window

    if chartType == "pie":
      print("We need a pie chart", w, "by", h)
      GraphPie(p, d, w, h)

    elif chartType == "bar":
      print("We need a bar chart", w, "by", h)
      GraphBar(p, d, w, h)

    line = infile.readline()

  infile.close()

main()