"""
Given a skill tree described as an array and a set of required skills, return the total number of skills needed to learn all of the required skills.
Intuition: In the example's tree, if I want to learn skill 6, I first need to learn skills 0 and 2 - a total of 3 skills learned.
"""


def count_skills(tree, required):
    bag, skills = required.copy(), set()
    while bag:
        skill = bag.pop()
        if skill in skills: continue
        skills.add(skill)
        bag.add(tree[skill])
    return len(skills)