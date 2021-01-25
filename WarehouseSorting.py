import csv
#>>>PRINT THE WAREHOUSE PRICE VALUES
#WAREHOUSE A
def selection_a():
        f = open('WarehouseA.csv')
csv_f = csv.reader(f)
WarehouseA =[]

for row in csv_f:
        WarehouseA.append(row[0])
        WarehouseA.append(row[1])
        WarehouseA.append(row[2])
print ("Warehouse A")
print (WarehouseA)

f.close()

#WAREHOUSE B
def selection_b():
    f = open('WarehouseB.csv')
csv_f = csv.reader(f)
WarehouseB =[]

for row in csv_f:
        WarehouseB.append(row[0])
        WarehouseB.append(row[1])
        WarehouseB.append(row[2])
print ("Warehouse B")
print (WarehouseB)

f.close()

#WAREHOUSE C
def selection_c():
        f = open('WarehouseC.csv')
csv_f = csv.reader(f)
WarehouseC =[]

for row in csv_f:
        WarehouseC.append(row[0])
        WarehouseC.append(row[1])
        WarehouseC.append(row[2])
print ("Warehouse C")
print (WarehouseC)

f.close()

#WAREHOUSE D
def selection_d():
        f = open('WarehouseD.csv')
csv_f = csv.reader(f)
WarehouseD =[]

for row in csv_f:
        WarehouseD.append(row[0])
        WarehouseD.append(row[1])
        WarehouseD.append(row[2])
print ("Warehouse D")
print (WarehouseD)

f.close()


#WAREHOUSE SELECTION
def letter_selection():
        letter = ''
        while not  (letter == 'A' or letter == 'B' or letter == 'C' or letter == 'D'):
                print("Please choose what warehouse to view: A,B,C,D")
        letter = input().upper()

        if letter == "A":
                return SelectionA
        if letter == "B":
                return SelectionB
        if letter == "C":
                return SelectionC
        if letter == "D":
                return SelectionD

#Loop that goes through each row in a CSV file to the selected column and adds them up,
#If it exceeds 6 billion it rejects
        #WAREHOUSE A
        with open("WarehouseA.csv") as fin:
            headerline = fin.next()
            total = 0
            for row in csv.reader(fin):
                total += int(row[1])
                if total > 6000000000:
                        print ("The value of this warehouse has exceeded the maximum value")

        #WAREHOUSE B
        with open("WarehouseB.csv") as fin:
            headerline = fin.next()
            total = 0
            for row in csv.reader(fin):
                total += int(row[1])
                if total > 6000000000:
                        print ("The value of this warehouse has exceeded the maximum value")

        #WAREHOUSE C
        with open("WarehouseC.csv") as fin:
            headerline = fin.next()
            total = 0
            for row in csv.reader(fin):
                total += int(row[1])
                if total > 6000000000:
                        print ("The value of this warehouse has exceeded the maximum value")

        #WAREHOUSE D
        with open("WarehouseD.csv") as fin:
            headerline = fin.next()
            total = 0
            for row in csv.reader(fin):
                total += int(row[1])
                if total > 6000000000:
                        print ("The value of this warehouse has exceeded the maximum value")
       


       
