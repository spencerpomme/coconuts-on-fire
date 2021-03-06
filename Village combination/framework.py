#! needed libraries
import matplotlib.pyplot as plt
import time
import csv


# define two main classes this petit program will use later.
class Center_Village:
    '''
    This class defines center village which creates center village instance.
    '''
    def __init__(self, name, long, lat, area, EPC, std_EPC, TYPE, population, admin):
        '''
        Meaning of arguments:
        name -- the name of village
        long & lat -- geographical coordinates represented as a tuple type.
        area -- area of the village, measured in square meter.
        EPC -- electric power consumption, measured in KWh.
        std_EPC -- standart deviation of EPC.
        population -- the population of the village.
        adm -- the administrative village where this very instance village belongs to.
        '''
        self.name = name
        self.cord = (float(long), float(lat))
        self.area = float(area)
        self.EPC = float(EPC)
        self.std_EPC = float(std_EPC)
        self.TYPE = TYPE
        self.population = float(population)
        self.admin = admin

    def mass_calculate(self):
        '''
        This method calculates the the mass factor of the center village.
        k, p, q are weights. 
        '''
        k = 0.004
        p = 0.5
        q = 0.5
        # need more work here
        self.mass = 1
        return self.mass

    def __str__(self):
        res = "中心村:%s|坐标:%s|面积:%.2f|用电量:%.2f|标准差:%.2f|类型:%s|人口:%d|行政村属:%s|" %\
               (self.name, str(self.cord), self.area, self.EPC, self.std_EPC,
                self.TYPE,self.population, self.admin)
        return res
    
                

    
class Hollow_Village(Center_Village):
    '''
    This class defines hollow village which creates hollow village instance.
    '''
    def mass_calculate(self):
        '''
        This method calculates the the mass factor of the hollow village.
        k, p, q are weights. 
        '''
        k = 1
        p = 1
        q = 1
        self.mass = 1
        return self.mass
    
    def __str__(self):
        res = "空心村:%s|坐标:%s|面积:%.2f|用电量:%.2f|标准差:%.2f|类型:%s|人口:%d|行政村属:%s|" %\
               (self.name, str(self.cord), self.area, self.EPC, self.std_EPC,
                self.TYPE,self.population, self.admin)
        return res
    
        

# module level functions
def opener():
    '''
    Control the outer file IO when the draw method starts: open file.
    '''
    global data, cent
    data = open(r'D:\GITHUB\coconuts-on-fire\Village combination\village_H.csv')
    cent = open(r'D:\GITHUB\coconuts-on-fire\Village combination\village_C.csv')

    

def closer():
    '''
    Control the outer file IO when the draw method starts: close file.
    '''
    global data, cent
    data.close()
    cent.close()

    

def data_reader(data, choice: 'H or C'):
    '''
    This function read hollow and center village data out of certain file.
    The choice filter can decide whether collect hollow or centers.
    '''
    hollows = []
    centers = []
    flag = choice
    res = 'fuck'
    collector = csv.reader(data, delimiter=',', skipinitialspace=True)
    for row in collector:
        if row[0] != '' and row[6] == '村庄':
            if float(row[5]) < -0.46:
                hollows.append(row)
            elif float(row[5]) > 0.13:# 0.13 is the value that control center village number at 430
                centers.append(row)
    if flag == 'H':
        res = hollows
    elif flag == 'C':
        res = centers
    return res



def hollow_reader(data):
    '''
    This function read hollow and center village data out of certain file.
    The choice filter can decide whether collect hollow or centers.
    '''
    hollows = []
    collector = csv.reader(data, delimiter=',', skipinitialspace=True)
    for row in collector:
        if row[0] != '' and row[6] == '村庄':
            if float(row[5]) < 1.56:# 1.56 is the value that control hollow village number at 1605
                hollows.append(row)
    return hollows



def distance(insH, insC):
    '''
    This function calculates phisical distance between two village points.
    insH - class Hollow_Village object
    insC - class Center_Village object
    '''
    cordH = insH.cord
    cordC = insC.cord
    # This method might have some proble, check later before May 14th.
    H = complex(cordH[0], cordH[1])
    C = complex(cordC[0], cordC[1])
    return abs(H - C)



def gravity(insH, insC):
    '''
    This function calculates 
    insH - class Hollow_Village object
    insC - class Center_Village object
    '''
    mH = insH.mass_calculate()
    mC = insC.mass_calculate()
    gravity = mH * mC / (distance(insH, insC) ** 2)
    return gravity    


def drag_long(cord):
    return cord[0]

def drag_lat(cord):
    return cord[1]


def draw_background():
    '''
    This function plots all those center villages and hollow villages as a background map.
    Then the lines could be drawn between them.
    '''
    opener()
    hollows = hollow_reader(data)
    hollow_list = []
    for vilas in hollows:        
        args = tuple(vilas)
        h = Hollow_Village(*args)
        h.mass_calculate()
        hollow_list.append(h.cord)
        

    centers = data_reader(cent, 'C')
    center_list = []
    for vilas in centers:        
        args = tuple(vilas)
        c = Center_Village(*args)
        c.mass_calculate()
        center_list.append(c.cord)
    
    plt.plot(list(map(drag_long, center_list)), list(map(drag_lat, center_list)), 'ro')    
    plt.plot(list(map(drag_long, hollow_list)), list(map(drag_lat, hollow_list)), 'k.')     
    
    plt.axis('scaled');plt.axis('off')
    closer()



def pick_lines(keyword: 'H, C or L' = "L"):
    '''
    This function picks the connective lines that show how hollow villages shoulb be merged into
    center villages.
    '''
    flag = keyword
    opener()
    hollow_ins = hollow_reader(data)
    hollow_assembly = []
    for obj in hollow_ins:        
        args = tuple(obj)
        hi = Hollow_Village(*args)
        hi.mass_calculate()
        hollow_assembly.append(hi)

    center_ins = data_reader(cent, 'C')
    center_assembly = []
    for obj in center_ins:        
        args = tuple(obj)
        ci = Center_Village(*args)
        ci.mass_calculate()
        center_assembly.append(ci)
    
    # In the nested loop below, i for hollow villages and j for center villages.
    # Now compair in permutations: first decide if two(hollow and center) are in same administrative
    # village, if so, the calculate their general distance and save into a dictionary for further op-
    # -eration.
    
    linelist = []
    for i in hollow_assembly:
        record = {}
        for j in center_assembly:            
            if i.admin == j.admin:
                record[i.name + str(i.area) + '->' + j.name + str(j.area)] = distance(i, j)                
        if record != {}:
            if record[max(record)] != 0:
                temp = min(record)
                linelist.append(temp)               
    closer()
    print(len(linelist))
    if flag == 'L':
        out = linelist
    elif flag == 'H':
        out = hollow_assembly
    elif flag == 'C':
        out = center_assembly
    return out
    


def draw_line(H, C, L):
    '''
    This function draw lines that indicates which village should be merged to which.
    '''
    hollows = H
    centers = C
    goods = L
    for item in goods:
        # v0 represent hollow village point and v1 represent center village point
        v0_name = item.split('->')[0]
        v1_name = item.split('->')[1]
        for h in hollows:
            if h.name+str(h.area) == v0_name:
                v0 = h.cord
        for c in centers:
            if c.name+str(c.area) == v1_name:
                v1 = c.cord
        plt.plot([v0[0], v1[0]], [v0[1], v1[1]], 'k-')          
            
            
# self test
if __name__ == '__main__':
    t1 = time.time()
    H = pick_lines(keyword='H')
    C = pick_lines(keyword='C')
    L = pick_lines(keyword='L')
    
    print('H', len(H))
    print('C', len(C))
    print('L', len(L))

    draw_line(H, C, L)
    draw_background()
    t2 = time.time()
    plt.show()
    
    t = t2-t1
    print(t)