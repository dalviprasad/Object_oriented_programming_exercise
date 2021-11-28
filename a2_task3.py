# Visualisation code template for FIT9136 Assignment 2.
# Instructions to students:
# 1. Implement task 3 within this file as a working program. You may define
#   as many functions or classes as you require to complete this task, if needed.
#   You may also import any libraries allowed by the assignment specification.
# 2. Modify the filename (and import statement(s) where required) to replace
#   the xxxxxxxx with your student ID number.
# 3. Complete tasks 1 and 2 within the other template files. The finished
#   program is split into three files, linked together by import statements.
#   In your IDE, ensure all files are part of the same project so the Python
#   interpreter can locate them.
# 4. Before submission, you should remove these instructions from this
#   template file and add your own program comments instead. This template file
#   has omitted program comments, which are your responsibility to add. Any
#   other 'placeholder' comments should be removed from your final submission.


from a2_task2 import *
import  matplotlib.pyplot as plt
# import statement to make use of functions/classes from earlier task(s).
# (change the xxxxxxxx to match the actual filename.)


def visual_curve(days, meeting_probability, patient_zero_health):
    affected_list = run_simulation(days, meeting_probability, patient_zero_health) # To run the simulations and get a list of the number of infected on a daily basis
    print(affected_list) # To print the list of infected people
    affected_by_day = plt.plot(range(days),affected_list) # To plot days on the x-axis and number of people affected on the y-axis
    plt.xlabel("Days") # Label the x-axis
    plt.ylabel("Count") # Label the y-axis
    return affected_by_day # Return a plot of the number of infected people by days


if __name__ == '__main__':
    days = int(input()) # To input the days from the user
    meeting_probability = float(input()) # To input the meeting_probability from the user
    patient_zero_health = int(input()) # To input the patient_zero_health from the user
    #scenario_A = visual_curve(days,meeting_probability,patient_zero_health)
    #scenario_B = visual_curve(days,meeting_probability,patient_zero_health)
    visual_curve(days,meeting_probability,patient_zero_health) # To get a list and a plot of the number of people affected each day


# do not add code here (outside the main block).