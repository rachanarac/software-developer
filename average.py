marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
i=0
c=0
while i<len(marks):
    j=0
    s=0
    while j<len(marks[i]):    
        s=s+(marks[i][j])
        c=c+1
        average=s/c
        j=j+1
    i=i+1
    print(average)        
