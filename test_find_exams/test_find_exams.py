#!/usr/bin/env python3

import unittest
import find_exams

class TestExclude(unittest.TestCase):
	'''Returns course'''
	def test_getCourse(self):
	   f = "ELEN4010"
	   ans = find_exams.find_exams.getCourse(f)
	   self.assertEqual("ELEN4010")
	   f.close()
	'''Returns the courses for lecturer'''
	def test_getCoursesForLects(self):
	   f = ("find_exams/lectlist.csv")
	   ans = find_exams.find_exams.getCoursesForLects(f)
	   self.assertEqual(ans, "Courses")
	   f.close()
	'''Returns the exams'''
	def test_getExams(self):
	   f = ("find_exams/examlist.csv")
	   ans = find_exams.find_exams.getExams(f)
	   self.assertEqual(ans, "Exams")
	   f.close()
	'''returns tiemtable'''
	def test_getTimeTable(self):
	   lf = ("find_exams/lectlist.csv")
	   ef = ("find_exams/examlist.csv")
	   courses = find_exams.find_exams.getCoursesFromLects(lf)
	   exams = find_exams.find_exams.getExams(ef)
	   ans = find_exams.find_exams.getTimetable(courses,exams)
	   self.assertEqual(ans, "Timetable")
	   f.close()
	'''Prints timetable'''
	def test_showTimeTable(self):
	   lf = ("find_exams/lectlist.csv")
	   ef = ("find_exams/examlist.csv")
	   courses = find_exams.find_exams.getCoursesFromLects(lf)
	   exams = find_exams.find_exams.getExams(ef)
	   ttable = find_exams.find_exams.getTimetable(courses,exams)
	   ans = showTimetable(ttable)
	   self.assertEquals(ans,"Show Timetable")
	   f.close()

	if __name__ == '__main__':
	   unittest.main()
