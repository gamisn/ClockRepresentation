import sys
class Digits:
    def __init__(self,d1,d2,d3,d4):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.matrix = self.create_matrix()
    def create_matrix(self):
        switcher = {
            0 : 'Zero',
            1 : 'One',
            2 : 'Two',
            3 : 'Three',
            4 : 'Four',
            5 : 'Five',
            6 : 'Six',
            7 : 'Seven',
            8 : 'Eight',
            9 : 'Nine'
            
        }
        
        d1_obj = globals()[switcher[self.d1]]()
        d2_obj = globals()[switcher[self.d2]]()
        d3_obj = globals()[switcher[self.d3]]()
        d4_obj = globals()[switcher[self.d4]]()
        
        m1 = d1_obj.get_matrix()
        m2 = d2_obj.get_matrix()
        m3 = d3_obj.get_matrix()
        m4 = d4_obj.get_matrix()
        matrix = []
        for i in range(len(m1)):
            if i == 1 or i==3:
                matrix.append(m1[i] + [0] + m2[i] + [0,0,0,1,0,0,0] + m3[i] + [0] + m4[i])
            else:    
                matrix.append(m1[i] + [0] + m2[i] + [0,0,0,0,0,0,0] + m3[i] + [0] + m4[i])
        #print(len(matrix))       
        return matrix
    def print(self):
        for line in self.matrix:
            for field in line:
                if field == 0:
                    print(" ", end = "")
                else:
                    print("#", end ="")
            print()
class Digit:
    def __init__(self):
        self.matrix = [[]]
        self.create_matrix()
    def create_matrix(self):
        self.matrix = [[0,0,0,0,0]]
    def get_matrix(self):
        return self.matrix

class Eight(Digit):
    def create_matrix(self):
        self.matrix = [[1,1,1,1,1] for i in range(5)]
        self.matrix[1] = [1,0,0,0,1]
        self.matrix[3] = [1,0,0,0,1]
        
class Nine(Digit):
    def create_matrix(self):
        self.matrix = Eight().get_matrix()
        self.matrix[3][0] = 0
        self.matrix[4] = [0,0,0,0,1]
        
class Three(Digit):
    def create_matrix(self):
        self.matrix = Eight().get_matrix()
        self.matrix[1][0] = 0
        self.matrix[3][0] = 0

class Two(Digit):
    def create_matrix(self):
        self.matrix = Eight().get_matrix()
        self.matrix[1][0] = 0
        self.matrix[3][4] = 0

class Five(Digit):
    def create_matrix(self):
        self.matrix = Eight().get_matrix()
        self.matrix[1][4] = 0
        self.matrix[3][0] = 0

class Six(Digit):
    def create_matrix(self):
        self.matrix = Eight().get_matrix()
        self.matrix[1][4] = 0
class Zero(Digit):
    def create_matrix(self):
        self.matrix = Eight().get_matrix()
        self.matrix[2] = [1,0,0,0,1]
class Seven(Digit):
    def create_matrix(self):
        self.matrix = Three().get_matrix()
        self.matrix[2] = [0,0,0,0,1]
        self.matrix[4] = [0,0,0,0,1]
class One(Digit):
    def create_matrix(self):
        self.matrix = Seven().get_matrix()
        self.matrix[0] = [0,0,0,0,1]

class Four(Digit):
    def create_matrix(self):
        self.matrix = One().get_matrix()
        self.matrix[0] = [1,0,0,0,1]
        self.matrix[1] = [1,0,0,0,1]
        self.matrix[2] = [1,1,1,1,1]
        
def generate_digital_clock(line: str):
    # Access your code here. Feel free to create other classes or methods as required
    linestr1= line.replace(" ","").replace("\n","").split(':')
    digit1 = int(linestr1[0][0])
    digit2 = int(linestr1[0][1])
    digit3 = int(linestr1[1][0])
    digit4 = int(linestr1[1][1])
    digits = Digits(digit1,digit2,digit3,digit4)
    digits.print()
    # print(digit1,digit2,digit3,digit4)
for line in sys.stdin:
    generate_digital_clock(line)
    
    

    