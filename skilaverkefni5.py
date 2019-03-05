# Matthías Ólafur

class Node:
    def __init__(self, d):
        self.data = d
        self.prv = None
        self.nxt = None

    # Endurkvæmt fall sem bætir aftast á listann.
    def append(self, d):
        if self.nxt:
            return self.nxt.append(d)
        else:
            curr = Node(d)
            self.nxt = curr
            curr.prv = self
            return True

    # Endurkvæmt fall sem og prentar listann.
    def printList(self):
        print(self.data, end = " ")
        if (self.nxt):
            self.nxt.printList()
        else:
            print()

    # Endurkvæmt fall sem og prentar listann frá Head til enda
    def find(self, d):
        if (self.data == d):
            return True
        elif (self.nxt):
            return self.nxt.find(d)
        else:
            return False

    # Endurkvæmt fall sem eyðir ákveðnum hnút úr lista
    def delete(self, d):
        if (self.data == d):
            if (self.nxt):
                self.prv.nxt = self.nxt
                self.nxt.prv = self.prv
            else:
                self.prv.nxt = None
            return True
        if (self.nxt):
            return self.nxt.delete(d)
        else:
            return False

# þinn kóði hér

class DLL:  # DLL = Dobule Linked List
    def __init__(self):
        self.head = None

    # Bætir við fremst á listann, hnúturinn verður Head -> förum ekki í Node klasann.  Þú úrfærir fallið í þessum klasa
    def push(self, d):
        if (self.head):
            tmp = self.head
            self.head = Node(d)
            self.head.nxt = tmp
            tmp.prv = self.head
        else:
            self.head = Node(d)
        return True

    # Bætir við aftast á listann -> kallar á endurkvæmnt fall í Node.  Fallið er þegar útfært í Node klasa
    def append(self, d):
        if self.head:
            return self.head.append(d)
        else:
            self.head = Node(d)
            return True

    # Prentar listann allan á skjá -> kallar á endurkvæmt fall í Node, þú útfærir printList í Node.  Notaðu endurkvæmni.
    def printList(self):
        if self.head:
            self.head.printList()
        else:
            print("Empty list!")

    # Kallar á endurkvæmt fall í Node klasanum, finnur ákveðinn hnút.  Þú útfærir fallið find í Node klasanum.  Notaðu endurkvæmni.
    def find(self, d):
        if self.head:
            return self.head.find(d)
        else:
            return False

    # Kallar á endurkvæmt fall í Node klasanum, finnur ákveðinn hnút og eyðir.  Þú útfærir fallið delete í Node klasanum.  Notaðu endurkvæmni.
    def delete(self, d):
        if self.head is None:
            return -1
        elif self.head.data == d:
            self.head = self.head.nxt
            self.head.prv.nxt = None
            self.head.prv = None
            return True
        else:
            return self.head.delete(d)


dbl = DLL()
dbl.append(5)  # 5
dbl.append(7)  # 5 7
dbl.push(1)  # 1 5 7
dbl.push(0)  # 0 1 5 7
dbl.append(10)  # 0 1 5 7 10
dbl.printList()
print()
print(dbl.delete(10))  # 0 1 5 7
dbl.printList()
print(dbl.find(5))  # True
print(dbl.find(10))  # False


print()
dbl.printList()
print(dbl.delete(0))
print(dbl.delete(5))
dbl.printList()