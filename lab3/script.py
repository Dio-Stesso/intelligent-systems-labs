import nbformat as nbf
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

nb = new_notebook()
nb.cells.append(new_markdown_cell("# Pandas Lab — Варіант 2\nНабір даних **US Baby Names (NationalNames.csv)**"))

load_code = """
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('NationalNames.csv')
df.head()
"""
nb.cells.append(new_code_cell(load_code.strip()))

tasks = [
("### 3. Імена стовпців", "df.columns"),
("### 4. Загальна інформація", "df.info()"),
("### 5. Кількість унікальних імен", "df['Name'].nunique()"),
("### 8. Найпопулярніше ім’я (max Count у будь‑якому році)", "df.loc[df['Count'].idxmax()][['Year','Name','Gender','Count']]"),
("### 9. Кількість записів з мінімальним Count", "df['Count'].eq(df['Count'].min()).sum()"),
("### 11. Рік з найбільшою кількістю унікальних імен", "df.groupby('Year')['Name'].nunique().idxmax()"),
("### 12. Найпопулярніше ім’я у цьому році", """
yr=df.groupby('Year')['Name'].nunique().idxmax()
df_year=df[df['Year']==yr]
df_year.loc[df_year['Count'].idxmax()][['Year','Name','Gender','Count']]
"""),
("### 13. Рік, коли жіноче ім’я *Jacob* було найпопулярнішим", """
df_jac=df[(df['Name']=='Jacob')&(df['Gender']=='F')]
df_jac.loc[df_jac['Count'].idxmax()][['Year','Count']]
"""),
("### 14. Рік із найбільшою кількістю гендерно‑нейтральних імен", """
neutral_per_year=(df.groupby(['Year','Name'])['Gender']
                  .nunique()
                  .reset_index()
                  .query('Gender==2')
                  .groupby('Year')['Name']
                  .nunique())
neutral_per_year.idxmax()
"""),
("### 16. Рік з найбільшою кількістю народжень", "df.groupby('Year')['Count'].sum().idxmax()"),
("### 17. Кількість дівчаток та хлопчиків щороку", """
births_sex=df.pivot_table(index='Year',columns='Gender',values='Count',aggfunc='sum')
births_sex.head()
"""),
("### 18. Кількість років, коли дівчаток більше за хлопчиків", "(births_sex['F']>births_sex['M']).sum()"),
("### 19. Графік кількості народжень хлопчиків та дівчаток на рік", """
births_sex.plot(figsize=(10,4))
plt.ylabel('Births');plt.show()
"""),
("### 20. Кількість гендерно‑нейтральних імен у наборі", """
neutral_names=df.groupby('Name')['Gender'].nunique().eq(2).sum()
neutral_names
"""),
("### 22. Кількість років спостереження", "df['Year'].nunique()"),
("### 23. Найпопулярніші гендерно‑нейтральні імена, присутні щороку", """
years=df['Year'].unique()
neutral_all_years=(df.groupby(['Name','Year'])['Gender'].nunique()
                   .unstack(fill_value=0)
                   .eq(2).all(axis=1))
names_every_year=df[df['Name'].isin(neutral_all_years[neutral_all_years].index)]
names_every_year.groupby('Name')['Count'].sum().sort_values(ascending=False).head()
"""),
("### 24. Найпопулярніше серед непопулярних імен", """
min_count=df['Count'].min()
unpopular=df[df['Count']==min_count]
unpopular.groupby('Name')['Count'].sum().sort_values(ascending=False).head(1)
"""),
("### 27. Найпопулярніші імена в кожному році", """
top_per_year=df.loc[df.groupby('Year')['Count'].idxmax()][['Year','Name','Gender','Count']].set_index('Year')
top_per_year.head()
""")
]

for title, code in tasks:
    nb.cells.append(new_markdown_cell(title))
    nb.cells.append(new_code_cell(code.strip()))

path='lab3_v2.ipynb'
with open(path,'w',encoding='utf-8') as f:
    nbf.write(nb,f)
