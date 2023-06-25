import csv

def collatz(n):
    counter = 0
    while n!=1:
        if n%2==0:
            n/=2
        else:
            n=3*n+1
        counter+=1
    return counter

with open("data.csv", "w") as f:
    for i in range(1,100):
        print(i)
        csv.writer(f).writerow([i, collatz(i)])
    
with open("data.csv", "r") as f:
    for row in csv.reader(f):
        print(row)