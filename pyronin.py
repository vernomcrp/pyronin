#!/usr/bin/env python

import datetime

class Siraset(object):
    NAME = 'siraset'
    FAMILY_NAME = 'jirapatchandej'
    HEIGHT = 167.0
    WEIGHT = 56.4
    BIRTHDATE = datetime.datetime(year=1981, month=4, day=1) 
    def __init__(self):
        self.today = datetime.datetime.now()
    def his_name(self):
        return "Mr. {name} {family_name}".format(
                name = self.NAME,
                family_name = self.FAMILY_NAME
            )
    def approx_day_on_earth(self):
        return self.today - self.BIRTHDATE

if __name__ == "__main__":
    me = Siraset()
    print "Hello my name is ", me.his_name()
    print "I'm valid on earth for %d days (that's mean since %s)." %  (
            me.approx_day_on_earth().days, 
            me.BIRTHDATE.strftime('%d %B %Y')
        )

        
        
