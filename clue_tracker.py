import numpy as np
<<<<<<< HEAD
distancelist = []
=======
>>>>>>> 4bab1aa94748b90e355327f9e9e7c467c6178439

class Player:
    
    def __init__(self):
        "Initialize player with card lists, question lists, and answer list"
        self.pqlist, self.wqlist, self.rqlist = np.zeros((10,6)), np.zeros((10,6)),           np.zeros((10,9))
        self.palist, self.walist, self.ralist = np.zeros((10,6)), np.zeros((10,6)),           np.zeros((10,9))
        
        self.pclist, self.wclist, self.rclist = np.ones(6), np.ones(6), np.ones(9)
        self.t = 0
    
    def ask(self, p, w, r):
        pqlist, wqlist, rqlist, t = self.pqlist, self.wqlist, self.rqlist, self.t
        
        pqlist[t][p-1] = 1
        wqlist[t][w-1] = 1
        rqlist[t][r-1] = 1
        t += 1
    
    def nocard(self, p, w, r):
        pclist, wclist, rclist = self.pclist, self.wclist, self.rclist
        pclist[p-1], wclist[w-1], rclist[r-1] = 0, 0, 0    
    
<<<<<<< HEAD
    def hascard(self, p, w, r):
        palist, walist, ralist, t = self.palist, self.walist, self.ralist, self.t
        palist[t][p-1], walist[t][w-1], ralist[t][r-1] = 1, 1, 1
    
    def turn(self, ask, nocard, hascard):
        
   
        
class Board: 
    
    def __init__(self):
        self.playerloc = np.ones(6) * 9
        
    def updateLocation(self, playerid, location):
        self.playerloc[playerid] = location
    
    def checkMoves(self, roll, playerid):
        possibilities = []
        for i in distancelist:
            if roll < i:
                possibilities.append(i)
    def turn(self, 
             
             
def Turn():
        
    userloc = input("enter the room that the first user chose")
    userpid = input("enter the pid of the first user")
    board.updateLocation(userpid, userloc)
=======
    def answer(self, p, w, r):
        palist, walist, ralist, t = self.palist, self.walist, self.ralist, self.t
        palist[t][p-1], walist[t][w-1], ralist[t][r-1] = 1, 1, 1
>>>>>>> 4bab1aa94748b90e355327f9e9e7c467c6178439
