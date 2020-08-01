#working on resizing and repositioning stuff

import numpy
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        self.resize()#determine whether or not we need to resize the table
        hashvalue = self.hashfunction(key, len(self.slots))#get hash val with given key and length of slots

        if self.slots[hashvalue] == None:#if the slot is empty, add the thing
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:#if the slot already has the same key, replace the data
                self.data[hashvalue] = data  #replace
            else:# else, rehash for a new slot
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data #replace

    #Function to check if the table needs resizing, and if so, resizes the table
    def resize(self):
        if self.getLoadFactor() > 0.7:# We resize if its over 70% full
            oldData = self.data #Take a copy of the pre-resize slots and data.
            oldSlots = self.slots
            self.data = [None] * (len(oldData) * 2)# Make new lists, twice as long as the old ones
            self.slots = [None] * (len(oldSlots) * 2)
            self.fix(oldSlots, oldData)# Take the old slots and data, and put them in the correct spots in the new table
            self.size = self.size * 2# Make sure we remember our resize
            

    #Function to fix up the table after a resize, by calculating the new position of all the stuff
    def fix(self, oldSlots, oldData):
        for i in range(0, len(oldSlots)):# Start going through all of our old stuff
            if oldSlots[i] != None:# We don't care if the slot is empty
                key = oldSlots[i] # Take the old key-val pair...
                val = oldData[i]
                self.put(key, val) # ...and put it in it's proper home in the bigger table

    #Function to get the current load factor. This value is how we decide when to resize
    def getLoadFactor(self):
        # Load factor = # of filled slots / # of slots total
        d = len(self.slots) # get the total number of slots
        n = 0 # create a counter var
        for slot in self.slots:# Go through each slot, and find out if it's filled. Add one if it is.
            if slot != None:
                n += 1
        #At this point, n is the number of slots that are filled.
        #print("There are " + str(d) + " slots, " + str(n) + " are full (" + str(n/d * 1.0) + ")")
        return n/d * 1.0# Calculate the load factor, as a float

    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


