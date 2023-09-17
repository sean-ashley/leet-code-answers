Consider a special family of Engineers and Doctors. This family has the following rules:

    Everybody has two children.
    The first child of an Engineer is an Engineer and the second child is a Doctor.
    The first child of a Doctor is a Doctor and the second child is an Engineer.
    All generations of Doctors and Engineers start with an Engineer.
Given the level and position of a person in the ancestor tree above, find the profession of the person.

def solution(level, pos):
    #base case
    if level == 1:
        return "Engineer"
    #recurrent case
    else:
        parent = solution(level-1, pos - (pos//2))
    
    if (parent == "Engineer" and pos % 2 == 0) or (parent=="Doctor" and pos % 2 == 1):
        return "Doctor"
    
    else:
        return 'Engineer'
    
        
    

