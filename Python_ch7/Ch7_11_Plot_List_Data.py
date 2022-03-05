# Plotting List Data with the matplotlib
# Package

# Reading

import matplotlib.pyplot

# matplotlib.pyplot.plot(arguments...)

# Alternate Method
import matplotlib.pyplot as plt
# plt.plot(arguments...)
x_coords = [0,1,2,3,4]
y_coords = [0,3,1,5,2]

plt.plot(x_coords,y_coords)
plt.show()

# line graph1
import matplotlib.pyplot as plt
def main():
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    plt.plot(x_coords,y_coords)
    plt.show()

if __name__ == '__main__':
    main()

# line graph2
import matplotlib.pyplot as plt
def main():
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    plt.plot(x_coords,y_coords)
    plt.title('Sample Data')
    plt.xlabel('This is the X axis')
    plt.ylabel('This is the Y axis')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()

# line graph3
import matplotlib.pyplot as plt
def main():
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    plt.plot(x_coords,y_coords)
    plt.title('Sample Data')
    plt.xlabel('This is the X axis')
    plt.ylabel('This is the Y axis')
    plt.xlim(xmin=-1, xmax=10)
    plt.ylim(ymin=-1, ymax=6)
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()

# line graph4
import matplotlib.pyplot as plt
def main():
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    plt.plot(x_coords,y_coords)
    plt.title('Sales by Year')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.xticks([0,1,2,3,4],['2016','2017','2018',
    '2019','2020'])
    plt.yticks([0,1,2,3,4,5],['$0m','$1m','$2m',
    '$3m','$4m','$5m'])
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()

# line graph5
import matplotlib.pyplot as plt
def main():
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    plt.plot(x_coords,y_coords,marker = 'o')
    plt.title('Sales by Year')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.xticks([0,1,2,3,4],['2016','2017','2018',
    '2019','2020'])
    plt.yticks([0,1,2,3,4,5],['$0m','$1m','$2m',
    '$3m','$4m','$5m'])
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()

# bar chart1
import matplotlib.pyplot as plt
def main():
    left_edges = [0,10,20,30,40]
    heights = [100,200,300,400,500]
    plt.bar(left_edges,heights)
    plt.show()

if __name__ == '__main__':
    main()

# bar chart2
import matplotlib.pyplot as plt
def main():
    left_edges = [0,10,20,30,40]
    heights = [100,200,300,400,500]
    bar_width = 5
    plt.bar(left_edges,heights,bar_width)
    plt.show()

if __name__ == '__main__':
    main()

# with color
import matplotlib.pyplot as plt
def main():
    left_edges = [0,10,20,30,40]
    heights = [100,200,300,400,500]
    bar_width = 5
    plt.bar(left_edges,heights,bar_width,
    color=('r','g','b','y','k'))
    plt.show()

if __name__ == '__main__':
    main()

# bar chart3
import matplotlib.pyplot as plt
def main():
    left_edges = [0,10,20,30,40]
    heights = [100,200,300,400,500]
    bar_width = 10
    plt.bar(left_edges,heights,bar_width,
    color=('r','g','b','y','k'))
    plt.title('Sales by Year')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.xticks([5,15,25,35,45],['2016','2017','2018',
    '2019','2020'])
    plt.yticks([0,100,200,300,400,500],['$0m','$1m','$2m',
    '$3m','$4m','$5m'])
    plt.show()

if __name__ == '__main__':
    main()

# pie chart1
import matplotlib.pyplot as plt
def main():
    values = [20,60,80,40]
    plt.pie(values)
    plt.show()

if __name__ == '__main__':
    main()

# pie chart2
import matplotlib.pyplot as plt
def main():
    sales = [100,400,300,600]
    slice_labels = ['1st Qtr','2nd Qtr',
    '3rd Qtr','4th Qtr']
    plt.pie(sales,labels= slice_labels)
    plt.title('Sales by Quarter')
    plt.show()

if __name__ == '__main__':
    main()

# with color
import matplotlib.pyplot as plt
def main():
    sales = [100,400,300,600]
    slice_labels = ['1st Qtr','2nd Qtr',
    '3rd Qtr','4th Qtr']
    plt.pie(sales,labels= slice_labels,
    colors=('r','g','b','y','k'))
    plt.title('Sales by Quarter')
    plt.show()

if __name__ == '__main__':
    main()

# End

# Checkpoint

# 7.29 To create a graph with the 'plot' function, what 2 arguments
# you must pass?
# A: 2 lists. One holding the X coordinates of the data points, 
# and the other holding the Y coordinates.

# 7.30 What sort of graph does the 'plot' function produce?
# A: A line graph.

# 7.31 What functions do you use to add labels to the X and Y axes
# in a graph?
# A. Use the xlabel and ylabel functions.

# 7.32 How do you change the lower and upper limits of the X and 
# Y axes in a graph?
# A. Call the xlim and ylim functions, passing values for the xmin,
# xmax,ymin,and ymax keyword arguments.

# 7.33 How do you customize the tick marks along the X and Y axes
# in a graph?
# A. Call the xticks and yticks functions. You pass 2 arguments 
# to these functions. The first argument is a list of tick-mark
# locations, and the second argument is a list of labels 
# to display at the specified locations.

# 7.34 To create a bar chart with the 'bar' function, what 2 
# arguments you must pass?
# A. 2 lists: 1 containing the X coordinates of each bar's
# left edge, and another containing the heights of each bar,
# along the Y axis.

# 7.35 Assume the following statements calls the 'bar' function to
# construct a bar chart with 4 bars. What color will the bars be?
# plt.bar(left_edges,heights,color=('r','b','r','b')) 
# A. The bars will be red,blue,red,and blue.

# 7.36 To create a pie chart with the 'pie' function, what argument
# you must pass?
# A. You pass a list of values as an argument. The 'pie' function
# will calculate the sum of the values in the list, then use that
# sum as the value of the whole. Then, each element in the list
# will become a slice in the pie chart. The size of a slice
# represents that element's value as a percentage of the whole.

# End   