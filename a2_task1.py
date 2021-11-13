#!/usr/bin/env python
# coding: utf-8

# In[44]:


# Task 1 code template for FIT9136 Assignment 2.
# Instructions to students:
# 1. Where required, replace the *pass* statements with your own method and
#   function definitions. Your submission must comply with the specification:
#   do not rename specified functions or change the number or type of arguments
#   or return values; otherwise you will be deemed not to have demonstrated
#   clear comprehension of the specified instructions. (You may define
#   your own additional functions and instance variables if you wish, as long
#   as these don't contradict the specified requirements. You may also
#   import any libraries allowed by the assignment specification.)
# 2. Complete task 1 within the framework of this template file.
# 3. Modify the filename (AND import statement(s), where required) to replace
#   the xxxxxxxx with your student ID number.
# 4. Complete tasks 2 and 3 within the other template files. The finished
#   program is split into three files, linked together by import statements.
# 5. In this file, you may define your own testing code within the 'main'
#   block to check if your simulation is working when running this script file
#   directly. Code in the main block will not be run by the automarker algorithm,
#   which will instead test the specified functions/methods by attempting to
#   call them directly according to how they are defined in the assignment 
#   requirments specification.
# 6. Before submission, you should remove these instructions from this
#   template file and add your own program comments instead. This template file
#   has omitted program comments, which are your responsibility to add. Any
#   other 'placeholder' comments should be removed from your final submission.

class Person: # Creating a class name Person and making functions for different inputs as mentioned in the pdf

    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name

    def add_friend(self, friend_person):
        self.friend_person = friend_person

    def get_name(self):
        complete_name = self.first_name +" "+ self.last_name
        return complete_name

    def get_friends(self):
        return self.friend_person


def load_people(): # Loading the data by making a function as mentioned in the pdf
    dataset = open("a2_sample_set.txt", "r") # This function inputs the data line by line
    person_name = dict()
    all_persons = []
    for i in dataset:
        x = i # This step converts it into string
        name, social_contact = x.split(":")
        person_name[name] = social_contact

    for key, values in person_name.items():
        first_name, last_name = key.split(" ")
        friend_person = values.strip().split(",")
        p = Person(first_name, last_name)
        p.add_friend(friend_person)
        all_persons.append(p)
    
    dataset.close()
    return all_persons


if __name__ == '__main__':
    pass



# do not add code here (outside the main block).

