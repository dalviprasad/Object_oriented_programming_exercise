#!/usr/bin/env python
# coding: utf-8

# In[173]:


# Task 2 code template for FIT9136 Assignment 2.
# Instructions to students:
# 1. Where required, replace the *pass* statements with your own method and
#   function definitions. Your submission must comply with the specification:
#   do not rename specified functions or change the number or type of arguments
#   or return values; otherwise you will be deemed not to have demonstrated
#   clear comprehension of the specified instructions. (You may define
#   your own additional functions and instance variables if you wish, as long
#   as these don't contradict the specified requirements. You may also
#   import any libraries allowed by the assignment specification.)
# 2. Complete task 2 within the framework of this template file.
# 3. Modify the filename (and import statement(s) where required) to replace
#   the xxxxxxxx with your student ID number.
# 4. Complete tasks 1 and 3 within the other template files. The finished
#   program is split into three files, linked together by import statements.
# 5. In this file, you may define your own testing code within the main block
#   to check if your simulation is working when running this script file
#   directly. Code in the main block will not be run by the automarker algorithm,
#   which will instead test the specified functions/methods by attempting to
#   call them directly according to how they are defined in the assignment 
#   requirments specification.
# 6. Before submission, you should remove these instructions from this
#   template file and add your own program comments instead. This template file
#   has omitted program comments, which are your responsibility to add. Any
#   other 'placeholder' comments should be removed from your final submission.

from a2_task1 import * # Importing the module created in task 1
import numpy
class Patient(Person):
    def __init__(self, first_name, last_name, health):
        super().__init__(first_name, last_name) # Inheriting the class Person from module a2_task1
        self.health = health

    def get_health(self):
        return self.health

    def set_health(self, new_health):
        self.health = round(new_health)

    def is_contagious(self):
        if self.health > 49:
            return False
        else:
            return True

    def infect(self, viral_load): # Building the infect function based on the description in the pdf
        if self.health <= 29:
            self.health -= 0.1 * viral_load
            if self.health > 100:
                self.health = 100
            elif self.health < 0:
                self.health = 0
        elif 29 < self.health < 50:
            self.health -= 1 * viral_load
            if self.health > 100:
                self.health = 100
            elif self.health < 0:
                self.health = 0
        else:
            self.health -= 2 * viral_load
            if self.health > 100:
                self.health = 100
            elif self.health < 0:
                self.health = 0

    def viral_load_cal(self): # Function to calculate the viral load for a person
        self.viral_load_patient = round(5 + ((self.health - 25)**2)/62)
        return self.viral_load_patient
    
    def sleep(self):
        self.health += 5
        if self.health > 100:
            self.health = 100


def run_simulation(days, meeting_probability, patient_zero_health):
    patient_list = load_patients(patient_zero_health)
    patient_list[0].set_health(patient_zero_health)
    
    contagious_all_day = []
    
    for i in range(1, len(patient_list)):
        patient_list[i].set_health(75)
    
    friend_index = dict()
    for i in range(len(patient_list)):
        friend_index[patient_list[i].get_name()] = i
        
    for i in range(days):
        for j in range(len(patient_list)):
            friend_names = patient_list[j].get_friends()
            for k in friend_names:
                prob = numpy.random.choice(numpy.arange(0, 2), p=[1-meeting_probability, meeting_probability]) # Numpy.random.choice will generate 0(not meeting) or 1(meeting) with the given probability of meeting 
                if prob == 1: # Will run only if the pair of person are meeting
                    index = 0
                    for key, values in friend_index.items():
                            if key == k:
                                index = values
                    if patient_list[j].is_contagious() == True: # If the Patient is cantagious
                        load = patient_list[j].viral_load_cal()
                        patient_list[index].infect(load)
                    elif patient_list[index].is_contagious() == True: # If the friend is cantagious
                        load = patient_list[index].viral_load_cal()
                        patient_list[j].infect(load)
        count_contagious = 0
        for m in range(len(patient_list)):
            if patient_list[m].is_contagious() == True:
                count_contagious += 1   
            patient_list[m].sleep()            
        contagious_all_day.append(count_contagious)
        
    return contagious_all_day

def load_patients(initial_health):
    dataset = open("a2_sample_set.txt", "r")
    patient_name = dict()
    all_patients = []
    for i in dataset:
        x = i
        name, social_contact = x.split(":")
        patient_name[name] = social_contact
        
    for key, values in patient_name.items():
        first_name, last_name = key.split(" ")
        friend_person = values.strip().split(",")
        patient_object = Patient(first_name, last_name, initial_health)
        patient_object.add_friend(friend_person)
        all_patients.append(patient_object)
    
    dataset.close()
    return all_patients


if __name__ == '__main__':
    # You may add your own testing code within this main block
    # to check if the code is working the way you expect.

    #This is a sample test case. Write your own testing code here.
    test_result = run_simulation(15, 0.8, 49)
    print(test_result)
    # Sample output for the above test case (15 days of case numbers):
    # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]
    #
    # Note: since this simulation is based on random probability, the
    # actual numbers may be different each time you run the simulation.


    # Another sample test case (high meeting probability means this will
    # spread to everyone very quickly; 40 days means will get 40 entries.)
    test_result = run_simulation(40, 1, 1)
    #sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200, 
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

    

# do not add code here (outside the main block).

