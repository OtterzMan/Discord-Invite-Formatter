import sys

def duperemove():
    lines = open('invites.txt', 'r').readlines()

    lines_set = set(lines)

    out  = open('invites.txt', 'w')

    for line in lines_set:
        out.write(line)

def nameremove():
    with open("invites.txt") as file:
        for line in file:
         print(line.split(" -")[0], file=open('newinvites.txt','a'))

duperemove()
nameremove()

print("All Invites Formatted [Click enter to exit]")
input(" ")