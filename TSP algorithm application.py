#! needed libraries 
from __future__ import division
import matplotlib.pyplot as plt
import random
import time
import itertools
import urllib
import csv

<<<<<<< HEAD
# file_xy是景点经纬度的csv文件，file_value是景点热度的csv文件
file_xy = open(r'J:\四会多规合一\四会景点坐标.csv')
file_value = open(r'J:\四会多规合一\四会景点热度.csv')
file_back = open(r'J:\四会多规合一\四会景点坐标back.csv')
=======
file = open(r'E:\SkyDrive\近期\relics.csv')
>>>>>>> ff4c1fe4d21994e0803cc53087a4ea15874fb379

def alltours(cities):
    '''Return a list of tours, each a permutation of cities, but each one starting
    with the same city.'''
    start = first(cities)
    return [[start] + Tour(rest) for rest in itertools.permutations(cities - {start})]

def first(collection):
    '''Start iterating over collection, and return the first element.'''
    return next(iter(collection))

Tour = list # Tours are implemented as lists of cities


# This Cities function need to be improved in data reading adaptablity.
def Cities(csv):
    '''
    A function to drag out x and y coordinates from a csv file(n roww 2 col) and
    convert them into complex numbers and store into a frozen set.
    '''
    assembly = []
    # The supposed scale in certain lat and long.
    long_scale = 1.0
    lat_scale = 1.0
    for item in csv:
        a = item.rstrip()        
        pair = list(map(lambda x: float(x), a.split(',')))
        pair[0] = pair[0] * long_scale
        pair[1] = pair[1] * lat_scale
        coor = complex(*pair)
        assembly.append(coor)    
    return frozenset(assembly)

<<<<<<< HEAD
def nodes_reader(file):
    '''
    A function to drag out x and y coordinates from a csv file
    (n row 2 col) and convert them into complex numbers and store
    into a frozen set. It's extended to work with more than 2 colums
    and can omit empty rows.
    '''
    assembly = []
    readerxy = csv.reader(file, delimiter=',', skipinitialspace=True)
    filter_num = first_n(file_value)#Attention value below this will be omited.
    print('firstn:', filter_num)
    for row in readerxy:
        if row[0] != '':
            latitude = float(row[1])# latitude as Y coordinate
            longitude = float(row[2])# longitude as X coordinate
            coor = complex(longitude, latitude)
            if float(row[3]) >= filter_num:
                assembly.append(coor)
    print('length:', len(assembly))
    return frozenset(assembly)


def all_points_plot(file):
    reader_all = csv.reader(file, delimiter=',', skipinitialspace=True)
    x_all = []
    y_all = []
    for row in reader_all:
        if row[0] != '':
            y_all.append(float(row[1]))# latitude as Y coordinate
            x_all.append(float(row[2]))# longitude as X coordinate
    return (x_all, y_all)
    
    

def first_n(file):
    value_list = []
    readerv = csv.reader(file, delimiter=',', skipinitialspace=True)
    for row in readerv:
        if row[1] != 0:
            value_list.append(float(row[1]))
    value_list.sort()
    n = 20
    #The n here represents how many points you want to include in the tour.
    return value_list[(len(value_list)-1)-n]
=======


def Cities_selected(csv):
    '''
    A selected set of points according to selector's rule.
    '''
    pass



def selector(assembly):
    '''
    A function to select points from the massive points generated by the function
    above(Cities)
    '''
    pass
>>>>>>> ff4c1fe4d21994e0803cc53087a4ea15874fb379



def shortest_tour(tours):
    '''Choose the tour with the minimum tour length.'''
    return min(tours, key = tour_length)


def repeated_nn_tsp(cities, repetitions=30):
    '''
    Repeat the nn_tsp algorithm starting from specified number of cities;
    return the shortest tour.
    '''
    return shortest_tour(nn_tsp(cities, start) for start in sample(cities, repetitions))


def sample(population, k, seed=42):
    '''
    Return a list of k elements sampled from population. Set random.seed with seed.
    '''
    if k is None or k > len(population):
        return population
    random.seed(len(population) * k * seed)
    return random.sample(population, k)


 
def nn_tsp(cities, start=None):
    """Start the tour at the first city; at each step extend the tour by moving
    from the previous city to its nearest neighbor that has not yet been visited.
    """
    if start is None: start = first(cities)
    tour = [start]
    unvisited = set(cities - {start})
    while unvisited:
        C = nearest_neighbor(tour[-1], unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour



def nearest_neighbor(A, cities):
    """
    Find nearest city in cities that is nearest to city A and remain unvisited
    """
    return min(cities, key = lambda c: distance(c,A))



def reverse_segment_if_better(tour, i, j):
    '''
    If reversing tour[i:j] would make the tour shorter, then do it.
    '''
    # Given tour [...A-B...C-D...], consider reversing B...C to get [...A-C...B-D...]
    A, B, C, D = tour[i-1], tour[i], tour[j-1], tour[j % len(tour)]
    # Are old edges(AB+CD) longer than new ones(AC+BD)? If so, reverse segment.
    if distance(A, B) + distance(C, D) > distance(A, C) + distance(B, D):
        tour[i:j] = reversed(tour[i:j])



def alter_tour(tour):
    "Try to alter tour for the better by reversing segments."
    original_length = tour_length(tour)
    for (start, end) in all_segments(len(tour)):
        reverse_segment_if_better(tour, start, end)
    # If we made an improvement, then try again; else stop and return tour.
    if tour_length(tour) < original_length:
        return alter_tour(tour)
    return tour



def all_segments(N):
    "Return (start, end) pairs of indexes that form segments of tour of length N."
    return [(start, start + length)
        for length in range(N, 2-1, -1)
        for start in range(N - length + 1)]



# The algorithm below is the best so far(2015-4-5)
def altered_nn_tsp(cities):
    "Run nearest neighbor TSP algorithm, and alter the results by reversing segments."
    return alter_tour(nn_tsp(cities))    




def repeated_altered_nn_tsp(cities, repetitions=20):
    "Use alteration to improve each repetition of nearest neighbors."
    return shortest_tour(alter_tour(nn_tsp(cities, start))
        for start in sample(cities, repetitions))




def tour_length(tour):
    '''
    The total of distance between each pair of consecutive cities in the tour
    '''
    return sum(distance(tour[i], tour[i-1]) for i in range(len(tour)))


def X(point):
    '''
    The x coordinate of a point.'''
    return point.real

def Y(point):
    '''
    The y coordinate of a point.'''
    return point.imag

def distance(A, B):
    '''
    The distance between two points.'''
    return abs(A-B)


<<<<<<< HEAD

def plot_all_points(allpoints, style='go'):
    '''
    To plot all points which are potentially visitable.
    Also as an object of reference to make the route meaningful and easy to see.
    '''
    plt.plot(list(map(X, points)), list(map(Y, points)), style)
    plt.show()



=======
>>>>>>> ff4c1fe4d21994e0803cc53087a4ea15874fb379
def plot_tour(tour):
    '''
    Plot the cities as circles and the tour as lines between them.'''
    start = tour[0]
    plot_lines(list(tour) + [tour[0]])
    plot_lines([start], 'rs') # mark the start city with a red square
<<<<<<< HEAD
    
=======
>>>>>>> ff4c1fe4d21994e0803cc53087a4ea15874fb379


def plot_lines(points, style='bo-'):
    '''
    Plot lines to connect a series of points.
    '''    
<<<<<<< HEAD
    
    # The line below presents the Background points, which is to say, some of them is
    # not included in a tour.
    back = all_points_plot(file_back)
    plt.plot(back[0], back[1], 'go')
=======
>>>>>>> ff4c1fe4d21994e0803cc53087a4ea15874fb379
    plt.plot(list(map(X, points)), list(map(Y, points)), style)
    plt.axis('scaled');plt.axis('off')
    


def plot_tsp(algorithm, cities):
    '''Apply a TSP algorithm to cities, plot the resulting tour, and print
    information.'''
    # Find the solution and time how long it takes
    t0 = time.clock()
    tour = algorithm(cities)
    t1 = time.clock()
    assert valid_tour(tour, cities)
    plot_tour(tour)
<<<<<<< HEAD
    
=======
>>>>>>> ff4c1fe4d21994e0803cc53087a4ea15874fb379
    plt.show()
    print('{} city tour with length {:.1f} in {:.3f} secs for {}'.format(\
        len(tour), tour_length(tour), t1-t0, algorithm.__name__))


def valid_tour(tour, cities):
    '''Is tour a valid tour for this cities?'''
    return set(tour) == set(cities) and len(tour) == len(cities)



def length_ratio(cities):
    '''The ratio of the tour lengths ofr nn_tsp and alltour_tsp algorithms.'''
    return tour_length(nn_tsp(cities)) / tour_length(repeated_nn_tsp(cities))



<<<<<<< HEAD
res = nodes_reader(file_xy)
rep = repeated_nn_tsp(res)
alt = altered_nn_tsp(res)
rpalt = repeated_altered_nn_tsp(res, repetitions = 300)
=======
res = Cities(file)
rep = repeated_nn_tsp(res)
alt = altered_nn_tsp(res)
rpalt = repeated_altered_nn_tsp(res, repetitions = 100)
>>>>>>> ff4c1fe4d21994e0803cc53087a4ea15874fb379

# print(rpalt)
print(len(rpalt))
plot_tsp(repeated_altered_nn_tsp, res)
<<<<<<< HEAD


plt.show()
a = all_points_plot(file_xy)
print(a)
=======
>>>>>>> ff4c1fe4d21994e0803cc53087a4ea15874fb379
