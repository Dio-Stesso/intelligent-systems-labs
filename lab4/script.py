import nbformat as nbf
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

nb = new_notebook()

nb.cells.append(new_markdown_cell("# Matplotlib Lab – Variant 2\nСистема:\n"
                                  "$$\\begin{cases}6.2x_1+6.6x_2=83\\\\-9.6x_1+13.8x_2=72\\\\-13.2x_1+5.7x_2=305\\end{cases}$$"))

setup_code = """
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')
%matplotlib inline

# coeffs a*x + b*y = c
eqs = [(6.2,  6.6,  83),
       (-9.6, 13.8, 72),
       (-13.2, 5.7, 305)]

def line_xy(a,b,c,x):
    return (c - a*x)/b
"""
nb.cells.append(new_code_cell(setup_code.strip()))

subplot_code = """
fig, axes = plt.subplots(1,3, figsize=(12,4), sharey=True, dpi=100)
colors = ['crimson','darkgreen','navy']
styles = ['--','-.',':']
x = np.linspace(-20,30,400)

for idx,(ax,(a,b,c)) in enumerate(zip(axes,eqs)):
    y=line_xy(a,b,c,x)
    ax.plot(x,y, color=colors[idx], linestyle=styles[idx], linewidth=2)
    ax.set_title(f'$%.1f x_1 %+ .1f x_2 = %.0f$'%(a,b,c))
    ax.set_xlabel('$x_1$')
    if idx==0: ax.set_ylabel('$x_2$')
fig.suptitle('Окремі прямі')
plt.tight_layout()
"""
nb.cells.append(new_code_cell(subplot_code.strip()))

combined_code = """
pts=[]
from itertools import combinations
for (i,(a1,b1,c1)), (j,(a2,b2,c2)) in combinations(enumerate(eqs),2):
    A=np.array([[a1,b1],[a2,b2]])
    B=np.array([c1,c2])
    x1,x2=np.linalg.solve(A,B)
    pts.append((x1,x2))
pts=np.array(pts)
xmin,xmax=pts[:,0].min()-5, pts[:,0].max()+5
ymin,ymax=pts[:,1].min()-5, pts[:,1].max()+5

fig,ax=plt.subplots(figsize=(8,16/2), dpi=100)
x=np.linspace(xmin,xmax,400)
for (a,b,c),col,st in zip(eqs,['crimson','darkgreen','navy'],['--','-.',':']):
    y=line_xy(a,b,c,x)
    ax.plot(x,y, color=col, linestyle=st, linewidth=2,
            label=r'$%.1f x_1 %+ .1f x_2 = %.0f$'%(a,b,c))
    xm=(xmin+xmax)/2
    ym=line_xy(a,b,c,xm)
    ax.text(xm, ym, r'$%.1f x_1 %+ .1f x_2 = %.0f$'%(a,b,c),
            rotation=np.degrees(np.arctan2(-a,b)), color=col,
            fontsize=9)

ax.fill(pts[:,0], pts[:,1], color='gold', alpha=0.3, label='Область перетину')

ax.scatter(pts[:,0], pts[:,1], s=60, color='black')
for k,(xp,yp) in enumerate(pts):
    ax.annotate(f'$P_{k+1}$',(xp,yp), textcoords='offset points', xytext=(5,5))

ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_title('Три прямі та їх область перетину')
ax.grid(color='gray', linestyle=':', linewidth=0.7)
ax.legend()
plt.tight_layout()

fig.savefig('combined_plot.jpg')
fig.savefig('combined_plot.png')
fig.savefig('combined_plot.svg')
"""
nb.cells.append(new_code_cell(combined_code.strip()))

nb.cells.append(new_markdown_cell("### Файли збережено\n"
                                  "- `combined_plot.jpg`\n- `combined_plot.png`\n- `combined_plot.svg`"))

path='matplotlib_v2.ipynb'
with open(path,'w',encoding='utf-8') as f:
    nbf.write(nb,f)
