# Task 1 code template for FIT9136 Assignment 2.

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

