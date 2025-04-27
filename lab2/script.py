import nbformat as nbf
from nbformat.v4 import new_notebook,new_markdown_cell,new_code_cell

nb = new_notebook()

title = new_markdown_cell("# Лабораторна робота (NumPy) – варіант 2")

intro = new_markdown_cell("Кожне завдання виконано двома способами: векторизованим (NumPy) та ітеративним (loops), з вимірюванням часу виконання.\n")

nb.cells.extend([title, intro])

exercises = [
    ("Вправа 2. \"Шахівниця\" n×n (1 – чорне, 0 – біле)", """
import numpy as np, time, math
n=8
%timeit np.indices((n,n)).sum(axis=0)%2
def loop(n):
    a=np.zeros((n,n),int)
    for i in range(n):
        for j in range(n):
            if (i+j)%2: a[i,j]=1
    return a
%timeit loop(n)
"""),
    ("Вправа 3. Матриця n×m з нулем у рядку r та стовпці c", """
n,m,r,c=6,7,2,3
%timeit (lambda n,m,r,c:(np.ones((n,m),int).astype(int).__setitem__(slice(None),np.ones((n,m),int)) or None))(n,m,r,c)
a=np.ones((n,m),int);a[r]=0;a[:,c]=0;a
def loop(n,m,r,c):
    b=np.ones((n,m),int)
    for i in range(n):
        for j in range(m):
            if i==r or j==c:b[i,j]=0
    return b
%timeit loop(n,m,r,c)
"""),
    ("Вправа 5. Рядки з парним індексом – 1, інші – 0", """
n=6
%timeit (lambda n: (np.arange(n)[:,None]%2==0).astype(int))(n)
def loop(n):
    a=np.zeros((n,n),int)
    for i in range(0,n,2):a[i]=1
    return a
%timeit loop(n)
"""),
    ("Вправа 9. Вектор від n до 0", """
n=10
%timeit np.arange(n,-1,-1)
def loop(n):
    return np.array([n-i for i in range(n+1)])
%timeit loop(n)
"""),
    ("Вправа 13. Шахівниця 8×8 через repeat", """
board=np.tile(np.array([0,1]*4),(8,1))
board[1::2]=board[0][::-1]
board
"""),
    ("Вправа 14. Шахівниця 8×8 через tile", """
np.tile([[0,1],[1,0]],(4,4))
"""),
    ("Вправа 16. Нулі в інтервалі (n/4,3n/4)", """
n=20
v=np.arange(n+1)
v[(v>n/4)&(v<3*n/4)]=0
v
def loop(n):
    v=[]
    for i in range(n+1):
        v.append(0 if n/4<i<3*n/4 else i)
    return np.array(v)
loop(n)
"""),
    ("Вправа 17. Зміна знаку x<n/2 або x>3n/4", """
n=10
v=np.arange(n+1)
mask=(v<n/2)|(v>3*n/4)
v[mask]*=-1
v
def loop(n):
    v=[]
    for i in range(n+1):
        v.append(-i if i<n/2 or i>3*n/4 else i)
    return np.array(v)
loop(n)
"""),
    ("Вправа 20. Випадковий вектор; замінити max на 0", """
n=10
v=np.random.rand(n)
v[v.argmax()]=0
v
def loop(n):
    v=list(np.random.rand(n))
    v[v.index(max(v))]=0
    return np.array(v)
loop(n)
""")
]

for hdr, code in exercises:
    nb.cells.append(new_markdown_cell(hdr))
    nb.cells.append(new_code_cell(code.strip()))

nb.cells.append(new_markdown_cell("## Система лінійних рівнянь (формули Крамера)"))
sys_code="""
import numpy as np, time
A=np.array([[1,2,3,-2],
            [1,-1,-2,-3],
            [3,2,-1,2],
            [2,-3,2,1]],float)
b=np.array([6,8,4,-8],float)

detA=np.linalg.det(A)
x=[]
for i in range(4):
    Ai=A.copy();Ai[:,i]=b
    x.append(np.linalg.det(Ai)/detA)
x=np.array(x)

x_dot=A.T @ (np.linalg.inv(A.T)@b) 
x_inv=np.linalg.inv(A)@b
x_solve=np.linalg.solve(A,b)

print(x)
print(np.allclose(x,x_inv,x_solve))
"""
nb.cells.append(new_code_cell(sys_code.strip()))

nb.cells.append(new_markdown_cell("## 3) Матричний вираз $3A - (A - 2B)B$"))
expr_code="""
import numpy as np,time
A=np.array([[4,5,-2],
            [3,-1,0],
            [4,2,7]],float)
B=np.array([[2,1,-1],
            [0,1,3],
            [5,7,3]],float)

%timeit 3*A - (A-2*B)@B

def loop(A,B):
    C=np.zeros_like(A,dtype=float)
    for i in range(3):
        for j in range(3):
            s=0
            for k in range(3):
                s+=(A[i][k]-2*B[i][k])*B[k][j]
            C[i][j]=3*A[i][j]-s
    return C

%timeit loop(A,B)
print(np.allclose(3*A-(A-2*B)@B, loop(A,B)))
"""
nb.cells.append(new_code_cell(expr_code.strip()))

path="lab2_v2.ipynb"
with open(path,"w",encoding="utf-8") as f: nbf.write(nb,f)
