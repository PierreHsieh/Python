# coding:utf-8
from random import randint


class Team(object):

    tName = ''

    def __init__(self, tname):
        self.tName = tname
        self.students = []
        self.tearchers = []

    @property
    def Tname(self):
        return self.tName

    def addStudent(self, sobj):
        self.students.append(sobj)
        sobj.Steam = self

    def getAllstudent(self):
        return self.students

    def getStudent_byid(self, id):
        for s in self.students:
            if s.Id == id:
                return s

    def addTearcher(self, tobj):
        self.tearchers.append(tobj)
        tobj.setTeam(self)

    def getTearch_byobj(self, obj):
        for t in self.tearchers:
            if t.Object == obj:
                return t

    def getSnum(self):
        return len(self.students)

    def getTnum(self):
        return len(self.tearchers)


class Student(object):
    id = 0
    age = 0
    name = ''

    teamid = None

    def __init__(self, num, age, name):
        self.id = num
        self.name = name
        self.age = age
        self.scores = {}

    @property
    def Age(self):
        return self.age

    @Age.setter
    def Age(self, age):
        self.age = age

    @property
    def Id(self):
        return self.id

    @property
    def Name(self):
        return self.name

    @property
    def STeam(self):
        return self.teamid

    def Steam(self, team):
        self.teamid = team

    def setScoreByObj(self, obj, score):
        print(self.Name, score, id(self.scores))
        self.scores[obj] = score

    def getScoreByObj(self, obj):
        return self.scores.get(obj, 0)


class Tearcher(object):
    age = 0
    name = ''
    salary = 0

    object = ''

    def __init__(self, name, age, salary, obj):
        self.name = name
        self.age = age
        self.salary = salary
        self.object = obj
        self.teams = []

    @property
    def Salary(self):
        return self.salary

    @Salary.setter
    def Salary(self, salary):
        self.salary = salary

    @property
    def Object(self):
        return self.object

    def setTeam(self, team):
        self.teams.append(team)

    def getTeam_byname(self, tname):
        for team in self.teams:
            if team.Tname == tname:
                return team

    def genScores(self, classname):
        for t in self.teams:
            if t.Tname == classname:
                for s in t.getAllstudent():
                    s.setScoreByObj(self.object, randint(30, 100))


team = Team('001')
for Id in range(1, 41):
    s = Student(Id, randint(10, 11), 'name_'+str(Id))
    team.addStudent(s)
print(team.getSnum())
# 40
print('======')

objs = ['math', 'biology']
for obj in objs:
    t = Tearcher('Alvis', randint(25, 35), 5000, obj)
    team.addTearcher(t)
print(team.getTnum())
# 2
print('======')

t.genScores('001')
for s in team.getAllstudent():
    print(s.Name, s.getScoreByObj(t.Object))
'''
name_1 97 6887968
name_2 49 6888064
name_3 88 6888160
name_4 60 6888256
name_5 58 6888352
name_6 39 6888448
name_7 65 6888544
name_8 84 6888640
name_9 61 6888736
name_10 100 6888832
name_11 53 6888928
name_12 36 6889024
name_13 37 6889120
name_14 69 6889216
name_15 81 6889312
name_16 56 6889408
name_17 54 6918240
name_18 32 6918336
name_19 41 6918432
name_20 76 6918528
name_21 62 6918624
name_22 38 6918720
name_23 87 6918816
name_24 65 6918912
name_25 43 6919008
name_26 99 6919104
name_27 54 6919200
name_28 55 6919296
name_29 43 6919392
name_30 81 6919488
name_31 89 6919584
name_32 30 6919680
name_33 40 6919776
name_34 30 6919872
name_35 48 6919968
name_36 77 6920064
name_37 99 6920160
name_38 48 6920256
name_39 58 6920352
name_40 68 6920448
name_1 97
name_2 49
name_3 88
name_4 60
name_5 58
name_6 39
name_7 65
name_8 84
name_9 61
name_10 100
name_11 53
name_12 36
name_13 37
name_14 69
name_15 81
name_16 56
name_17 54
name_18 32
name_19 41
name_20 76
name_21 62
name_22 38
name_23 87
name_24 65
name_25 43
name_26 99
name_27 54
name_28 55
name_29 43
name_30 81
name_31 89
name_32 30
name_33 40
name_34 30
name_35 48
name_36 77
name_37 99
name_38 48
name_39 58
name_40 68
'''