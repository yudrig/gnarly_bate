#!/usr/bin/python2
import searchUsers
import searchTemplates
import imageCreation
#searchUsers()
#searchTemplates()
x=1
while x <= 12:
        imageCreation.imageCreation(searchTemplates.searchTemplates(1,101),searchUsers.searchUsers(1,x,3))
        x += 1

