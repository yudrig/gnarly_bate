#!/usr/bin/python2
import searchUsers
import searchTemplates
import imageCreation
#searchUsers()
#searchTemplates()
imageCreation.imageCreation(searchTemplates.searchTemplates(1,101),searchUsers.searchUsers(1,1,3))

