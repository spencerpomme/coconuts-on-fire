from classtools import AttrDisplay

class Person(AttrDisplay):
    '''
    Create and process person records
    '''
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay *(1 + percent))


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
        
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent+bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)





if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', pay=50000)
    
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaise(.10)
    development.showAll()
    
    
