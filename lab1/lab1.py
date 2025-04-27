import nbformat as nbf
from datetime import date
import base64

nb = nbf.v4.new_notebook()

cells = [nbf.v4.new_markdown_cell(
    f"# Лабораторна робота\n### «Інтелектуальні системи на основі знань»\nВаріант 2 — Буркіна‑Фасо\n")]

country_info = """
## Загальні відомості <span style="color:darkred">про Буркіна‑Фасо</span>

<div style="border:2px solid #993300; padding:10px; background:#fffaf0;">
<strong>Буркіна‑Фасо</strong> (до 4 серпня 1984 р. — Верхня Вольта) — держава у Західній Африці без виходу до моря.  
Столиця — <em>Уагадугу</em>. Населення ≈ 22 млн (2023). Державний устрій — <mark>унітарна напівпрезидентська республіка</mark>.
</div>

### Цікаві факти
| Показник | Значення |
|----------|----------|
| Площа | 274200км² |
| Офіційна мова | Французька |
| Найвища точка | Гора Тенакуро(749м) |
| Валюта | Західноафриканський франк(CFAXOF) |

1. **Видатні особистості**
   1. Томас Санкара — «африканський Че Гевара»  
   2. Салліф Кейта — видатний музикант мандінка
2. **Свята**
   * День незалежності — 5 серпня
   * Фестиваль масок у Дедугу

### Природні та культурні пам’ятки
- **Національний парк «W»** — частина транскордонного біосферного заповідника.
- **Скелі Сінду** — мальовничі пісковикові формації.
- **Місто Бобо-Діуласо** — старий район Діуласоба та глиняна велика мечеть.

> Докладніше див. на [офіційному туристичному порталі](https://burkinafaso-tourisme.gov.bf)
"""

cells.append(nbf.v4.new_markdown_cell(country_info))

svg_flag = """
### Прапор Буркіна‑Фасо (SVG)

<svg width="300" height="200">
  <rect width="300" height="100" y="0"  style="fill:#EF2B2D" />
  <rect width="300" height="100" y="100" style="fill:#009E49" />
  <polygon points="150,70 165,125 115,95 185,95 135,125" style="fill:#FCD116"/>
</svg>
"""
cells.append(nbf.v4.new_markdown_cell(svg_flag))

code_func = """
def task_2(a: int | None = None, b: int | None = None):
    \"\"\"Алгоритм Евкліда (ділення + віднімання) для НСД.

    Якщо a та b не передані — запитуються з клавіатури.

    Повертає НСД та друкує інформаційний рядок.
    \"\"\"
    if a is None or b is None:
        try:
            a, b = map(int, input("Введіть два натуральних числа через пробіл: ").split())
        except ValueError:
            print("Помилка: введіть саме два цілих числа.")
            return None
    if a <= 0 or b <= 0:
        print("Числа мають бути додатними цілими.")
        return None

    swaps = 0
    while b:
        a, b = b, a % b
        swaps += 1
    print(f"Найбільший спільний дільник — {a}")
    return a
"""
cells.append(nbf.v4.new_code_cell(code_func))

tests = """task_2(16, 36) # 4
task_2(12, 54) # 6
task_2() # інтерактивний ввід користувача
"""
cells.append(nbf.v4.new_code_cell(tests))

cells.append(nbf.v4.new_markdown_cell("#### Висновок\n> У цьому ноутбуці продемонстровано можливості Markdown/HTML у Jupyter, створено SVG‑прапор, а також реалізовано та протестовано алгоритм Евкліда для знаходження НСД (варіант 2)."))

nb['cells'] = cells

path = "lab1_v2.ipynb"
with open(path, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(path)
