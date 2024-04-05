#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:06:46 2024

@author: Ruiyang Shi
"""

# 1
class MyClass():
    def __init__(self):
        self.a = 10
        self.b = 20
        self.x = self.a + self.b

my_instance = MyClass()
print(my_instance.x)

# 2
class MyClass():
    def __init__(self):
        self.a = 10
        self.b = 20
        self.x = self.a + self.b

my_instance = MyClass()
print(my_instance.x)

# 3
class MyClass():
    def __init__(self, a, b):
        self.x = a + b

my_instance = MyClass(10, 20)
print(my_instance.x)

# 4
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.enrolled_courses = []

    def enroll(self, course):
        self.enrolled_courses.append(course)

    def display_enrolled_courses(self):
        print(f"{self.name}'s enrolled courses:")
        for course in self.enrolled_courses:
            print(course)

    def drop_course(self, course):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            print(f"{course} dropped successfully.")
        else:
            print(f"{course} not found in enrolled courses.")

student1 = Student("Ruiyang Shi", 2024)
student1.enroll("Econ1001")
student1.enroll("CS5000")
student1.enroll("Physics1001")
student1.display_enrolled_courses()
student1.enroll("Chemistry1001")
student1.drop_course("CS5000")
student1.display_enrolled_courses()