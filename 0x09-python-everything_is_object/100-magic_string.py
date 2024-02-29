#!/usr/bin/python3
magic_string=lambda n="BestSchool, ", c=[0]: ((n*(c[0])) + "BestSchool", c.__setitem__(0, c[0]+1))[0]
