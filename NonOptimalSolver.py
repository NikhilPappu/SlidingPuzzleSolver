# n = eval(input("Enter the size of the grid: \n"))
# print("\nEnter the initial state of the board :")
# board2 = []
# count = 0
# for i in range(n):
#     board2.append([int(temp) for temp in input().strip().split()])
def find(a,l,n):
    for i in range(n):
        for j in range(n):
            if(l[i][j]==a):
                return (i,j)
def swap(l,r1,c1,r2,c2):
    global count
    l[r1][c1],l[r2][c2] = l[r2][c2],l[r1][c1]
    for a in l:
        for b in a:
            print(b, end=" ")
        print()
    print()
    count+=1
def manhattanDist(r1,c1,r2,c2):
    return abs(r1-r2)+abs(c1-c2)
def shortestPath(r1,c1,r2,c2):
    path1 = []
    path2 = []
    R1 = r1
    C1 = c1
    if(r1>r2):
        while(r1>r2):
            path1.append((r1,c1))
            r1-=1
        if(c1>c2):
            while(c1>=c2):
                path1.append((r1,c1))
                c1-=1
        else:
            while(c2>=c1):
                path1.append((r1,c1))
                c1+=1
    else:
        while(r2>r1):
            path1.append((r1,c1))
            r1+=1
        if (c1 > c2):
            while (c1 >= c2):
                path1.append((r1, c1))
                c1 -= 1
        else:
            while (c2 >= c1):
                path1.append((r1, c1))
                c1 += 1
    r1 = R1
    c1 = C1
    if (c1 > c2):
        while (c1 > c2):
            path2.append((r1, c1))
            c1 -= 1
        if (r1 > r2):
            while (r1 >= r2):
                path2.append((r1, c1))
                r1 -= 1
        else:
            while (r2 >= r1):
                path2.append((r1, c1))
                r1 += 1
    else:
        while (c2 > c1):
            path2.append((r1, c1))
            c1 += 1
        if (r1 > r2):
            while (r1 >= r2):
                path2.append((r1, c1))
                r1 -= 1
        else:
            while (r2 >= r1):
                path2.append((r1, c1))
                r1 += 1


    return (path1,path2)
restricted = []
def moveBlank(dr,dc,val,row,board,n):
    newVal = val%n
    if(newVal==0):newVal=n
    (zi, zj) = find(0, board)
    (onei,onej) = find(val,board)
    bpath1 = shortestPath(zi, zj, dr, dc)[0]
    bpath2 = shortestPath(zi, zj, dr, dc)[1]
    if((onei,onej) not in bpath1 and (row,newVal-2) not in bpath1):
        for i in bpath1:
            swap(board,zi,zj,i[0],i[1])
            zi=i[0]
            zj=i[1]
    elif((onei,onej) not in bpath2 and (row,newVal-2) not in bpath2):
        for i in bpath2:
            swap(board,zi,zj,i[0],i[1])
            zi=i[0]
            zj=i[1]
    else:
        if(zi<n-1):
            swap(board,zi,zj,zi+1,zj)
        else:swap(board,zi,zj,zi-1,zj)
def Up(i,j,val,row,board,n):
    print("Up")
    moveBlank(i - 1, j,val,row,board,n)
    swap(board, i - 1, j, i, j)
def Left(i,j,val,row,board,n):
    print("Left")
    moveBlank(i, j - 1,val,row,board,n)
    swap(board, i, j - 1, i, j)
def Right(i,j,val,row,board,n):
    print("Right")
    moveBlank(i,j+1,val,row,board,n)
    swap(board,i,j+1,i,j)
def placeRowElement(val,row,board,n):
    newVal = val % n
    if (newVal == 0): newVal = n
    (i, j) = find(val, board,n)
    while(j<newVal and newVal!=1):
        if(newVal==n and j==(newVal-1)):
            placeN(val,row,board,n)
            return
        (zi, zj) = find(0, board)
        if(zi==i and zj<j):
            if(i<n-1):
                swap(board,zi,zj,zi+1,zj)
            else:swap(board,zi,zj,zi-1,zj)
        Right(i,j,val,row,board,n)
        j+=1
    while (i > row and j > newVal-1):
        (zi, zj) = find(0, board,n)

        if(j==zj and zi>i):
            Left(i,j,val,row,board,n)
            j-=1
        elif(i==zi and zj>j):
            Up(i,j,val,row,board,n)
            i-=1
        elif(manhattanDist(zi,zj,i-1,j)<=manhattanDist(zi,zj,i,j-1)):
            Up(i, j,val,row,board,n)
            i -= 1
        elif(manhattanDist(zi,zj,i-1,j)>manhattanDist(zi,zj,i,j-1)):
            Left(i,j,val,row,board,n)
            j-=1
    while (i > row):
        (zi, zj) = find(0, board,n)
        if(zj==newVal-1 and zi>i):
            if(zj<n-1):
                swap(board,zi,zj,zi,zj+1)
            else:swap(board,zi,zj,zi,zj-1)
            Up(i,j,val,row,board,n)
            i-=1
        else:
            if(i!=row):
                Up(i,j,val,row,board,n)
                i-=1
    while (j > newVal-1):
        (zi, zj) = find(0, board,n)

        if(zi==newVal-1 and zj>j):
            swap(board,zi,zj,zi+1,zj)
            Left(i,j,val,row,board,n)
            j-=1
        else:
            if(j!=newVal-1):
                Left(i,j,val,row,board,n)
                j-=1
def placeN(val,row,board,n):
    newVal = val % n
    if (newVal == 0): newVal = n
    (zi, zj) = find(0, board,n)
    (i, j) = find(val, board,n)
    if(zi==row and zj==n-1 and i==row+1 and j==n-1):
        swap(board,zi,zj,i,j)
        return
    (i,j) = find(val,board,n)
    while(i>row+1):
        (zi, zj) = find(0, board)
        if(zj==j and zi>i):
            swap(board,zi,zj,zi,zj-1)
        Up(i,j,val,row,board,n)
        i-=1
    moveBlank(row+1,0,val,row,board,n)
    swap(board,row,0,row+1,0)
    (zi, zj) = find(0, board,n)
    for i in range(1,n):
        swap(board,zi,zj,zi,zj+1)
        zj+=1
    swap(board,zi,zj,zi+1,zj)
    zi+=1
    swap(board,zi,zj,zi,zj-1)
    zj-=1
    swap(board,zi,zj,zi-1,zj)
    zi-=1
    for i in range(1,n-1):
        swap(board, zi, zj, zi, zj - 1)
        zj -= 1
    swap(board,zi,zj,zi+1,zj)
    zi+=1
def placeRow(row,board,n):
    for i in range(1,n+1):
        if (find(i, board,n)[0] != row or find(i, board,n)[1] != i - 1):
            placeRowElement(i+n*row,row,board,n)

def placeAllBut2Rows(board,n):
    for i in range(n-2):
        placeRow(i,board,n)
# placeAllBut2Rows(board2)
# print(count)
