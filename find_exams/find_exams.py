

import sys
import re

"""
This program is used to create an exam timetbale for lecturers.
Inputs: examlist.csv and lectlist.csv
Outputs: certains elements within the csv files
"""
'''Returns the course'''
def getCourse(line):
    l_name, c_name = line.strip().split("/")    ##EE1 fixed
    return l_name, c_name   #EE2 fixed
'''Returns the courses for lecturer'''
def getCoursesForLects(lectsfn):
    courses = {}  # dictionary: for each lect returns list of courses
    lf = open(lectsfn)
    for line in lf:
        lect, course = getCourse(line)
        if lect in courses: # is the lecturer in the dictionary
            courses[lect].append(course)  # add course to the list ##EE3 fixed
        else:
            courses[lect] = [course]  
    lf.close()
    return courses
'''Returns the exams'''
def getExams(examfname):
    exams = {}
    for line in open(examfname):
        data = line.rstrip().split(",")
        exams[data[0]]=(data[1],data[2])
    return exams
'''Returns the timetable'''
def getTimeTable(courses,exams):
    ttable = []  # nested list -- for each lect a list of exams
    for lect in sorted(courses.keys()):
        l_exams   = [] # build list of lecturer's exams
        l_courses = courses[lect] # get their courses
        for c in l_courses:
            if c not in exams:
                the_exam=("TBD","TBD")
            else:
                the_exam = exams[c]
            l_exams.append((c,the_exam))
        ttable.append((lect,l_exams)) # now we know the exams add it list
    return ttable
'''Prints the course'''
def showTimeTable(ttable):
    for (lect, l_exams) in ttable:
        print(lect)
        for c,ex in l_exams:
            print("   ",c,ex[0],ex[1])
        

if __name__ == "__main__":
    examfn    =  sys.argv[0] #"examlist.csv"
    lectsfn     = sys.argv[2] #"lectlist.csv"
    courses    = getCoursesForLects(lectsfn)
    exams     = getExams(examfn)
    tt = getTimeTable(courses,exams)
    showTimeTable(tt)
