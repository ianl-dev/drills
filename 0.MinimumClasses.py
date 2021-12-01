"""
Given a list of students, each with a number of their learning level,
find the minimum amount of grouping such that each group contains students with a learning gap at most k

for example:
[1,2,3,4,6,8,11], for k = 2

Min group # = 4
[1,2,3], [4,6], [8], [11]

Amazon question
"""
def findGroup(students, k):
    """
    My approach, record where the least (least knowledgeble) student in the group, add to group based on that student
    """
    # First sort the students by their knowledge level
    students.sort()
    least = students[0]
    classes, currentClass = [], [least]
    # Visit each student
    for i in range(1, len(students)):
        current = students[i]
        if abs(current-least) <= k:
            # Add student to class
            currentClass.append(current)
        else:
            # New class needs to form
            classes.append(currentClass)
            # Update new lowest-level student
            least = students[i]
            # Reset current class to fill in new students
            currentClass = [least]
    
    if currentClass:
        classes.append(currentClass)
    print(classes)
    return len(classes)

# Test cases
students = [1,2,3,4,6,8,11,100]
print(findGroup(students, 3))