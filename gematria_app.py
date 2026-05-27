from tkinter import *

# ---------- Gematria values ----------
gematria_base = {
    'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80,
    'צ': 90, 'ק': 100, 'ר': 200, 'שׂ': 300, 'ת': 400,
    'ך': 500, 'ם': 600, 'ן': 700, 'ף': 800, 'ץ': 900
}

# ---------- Atbash mapping ----------
atbash_map = {
    'א': 'ת', 'ת': 'א',
    'ב': 'ש', 'ש': 'ב',
    'ג': 'ר', 'ר': 'ג',
    'ד': 'ק', 'ק': 'ד',
    'ה': 'צ', 'צ': 'ה',
    'ו': 'פ', 'פ': 'ו',
    'ז': 'ע', 'ע': 'ז',
    'ח': 'ס', 'ס': 'ח',
    'ט': 'נ', 'נ': 'ט',
    'י': 'מ', 'מ': 'י',
    'כ': 'ל', 'ל': 'כ',
    'ך': 'ל', 'ם': 'י', 'ן': 'ט', 'ף': 'ו', 'ץ': 'ה'
}
for k, v in list(atbash_map.items()):
    if v not in atbash_map:
        atbash_map[v] = k

def atbash_transform(text):
    return ''.join(atbash_map.get(ch, ch) for ch in text)

def gematria_of_text(text, aleph_is_1000):
    total = 0
    for ch in text:
        if ch == 'א':
            total += 1000 if aleph_is_1000 else 1
        else:
            total += gematria_base.get(ch, 0)
    return total

# ---------- GUI ----------
root = Tk()
root.title("Gematria + Atbash Calculator")
root.geometry("500x680")
root.configure(bg='#0a3b5a')

# Aleph mode
aleph_1000 = BooleanVar()
aleph_1000.set(False)

# Input field
Label(root, text="Hebrew word / sentence:", font=('Arial', 14, 'bold'),
      bg='#0a3b5a', fg='white').pack(pady=(15, 0))
entry = Entry(root, font=('Arial', 16), width=30, justify='center',
              relief='solid', bd=2, bg='white', fg='black')
entry.pack(pady=8)

# Result labels
original_total_label = Label(root, text="Gematria of input: 0", font=('Arial', 13, 'bold'),
                             bg='#0a3b5a', fg='#ffd966')
original_total_label.pack(pady=5)

atbash_result_label = Label(root, text="Atbash: ", font=('Arial', 12),
                            bg='#0a3b5a', fg='#f39c12', wraplength=460)
atbash_result_label.pack(pady=5)

atbash_gematria_label = Label(root, text="Atbash gematria: 0", font=('Arial', 13, 'bold'),
                              bg='#0a3b5a', fg='#ffd966')
atbash_gematria_label.pack(pady=5)

# ---------- Hebrew keyboard frame ----------
key_frame = Frame(root, bg='#0a3b5a')
key_frame.pack(pady=10)

# All buttons now have fg='black'
btn_style = {
    'font': ('Arial', 26, 'bold'),
    'width': 3,
    'height': 1,
    'relief': RAISED,
    'bd': 2,
    'bg': '#f0f0f0',
    'fg': 'black',               # black text on light background
    'activebackground': '#d0d0d0',
    'activeforeground': 'black'
}

# Rows 1-6 (letters and final forms)
row1 = ['א', 'ב', 'ג', 'ד', 'ה']
for i, ch in enumerate(row1):
    btn = Button(key_frame, text=ch, command=lambda l=ch: entry.insert(END, l), **btn_style)
    btn.grid(row=0, column=i, padx=4, pady=4)

row2 = ['ו', 'ז', 'ח', 'ט', 'י']
for i, ch in enumerate(row2):
    btn = Button(key_frame, text=ch, command=lambda l=ch: entry.insert(END, l), **btn_style)
    btn.grid(row=1, column=i, padx=4, pady=4)

row3 = ['כ', 'ל', 'מ', 'נ', 'ס']
for i, ch in enumerate(row3):
    btn = Button(key_frame, text=ch, command=lambda l=ch: entry.insert(END, l), **btn_style)
    btn.grid(row=2, column=i, padx=4, pady=4)

row4 = ['ע', 'פ', 'צ', 'ק', 'ר']
for i, ch in enumerate(row4):
    btn = Button(key_frame, text=ch, command=lambda l=ch: entry.insert(END, l), **btn_style)
    btn.grid(row=3, column=i, padx=4, pady=4)

row5 = ['שׂ', 'ת']
for i, ch in enumerate(row5):
    btn = Button(key_frame, text=ch, command=lambda l=ch: entry.insert(END, l), **btn_style)
    btn.grid(row=4, column=i, padx=4, pady=4)

final_row = ['ך', 'ם', 'ן', 'ף', 'ץ']
for i, ch in enumerate(final_row):
    btn = Button(key_frame, text=ch, command=lambda l=ch: entry.insert(END, l), **btn_style)
    btn.grid(row=5, column=i, padx=4, pady=4)

# Delete button (red background, black text)
del_btn = Button(key_frame, text="⌫", font=('Arial', 20, 'bold'), width=3,
                 relief=RAISED, bd=2, bg='#e63946', fg='black',
                 activebackground='#b71c2c', activeforeground='black',
                 command=lambda: entry.delete(len(entry.get())-1, END))
del_btn.grid(row=6, column=0, padx=4, pady=6)

# Space button (blue background, black text)
space_btn = Button(key_frame, text="Space", font=('Arial', 16, 'bold'), width=16,
                   relief=RAISED, bd=2, bg='#3498db', fg='black',
                   activebackground='#1f618d', activeforeground='black',
                   command=lambda: entry.insert(END, ' '))
space_btn.grid(row=6, column=1, columnspan=4, sticky='ew', padx=4, pady=6)

# ---------- Action buttons with black text ----------
action_frame = Frame(root, bg='#0a3b5a')
action_frame.pack(pady=15)

def calculate_original():
    total = gematria_of_text(entry.get(), aleph_1000.get())
    original_total_label.config(text=f"Gematria of input: {total}")

def show_atbash():
    text = entry.get()
    atbash = atbash_transform(text)
    atbash_total = gematria_of_text(atbash, aleph_1000.get())
    atbash_result_label.config(text=f"Atbash: {atbash}")
    atbash_gematria_label.config(text=f"Atbash gematria: {atbash_total}")

def clear_all():
    entry.delete(0, END)
    original_total_label.config(text="Gematria of input: 0")
    atbash_result_label.config(text="Atbash: ")
    atbash_gematria_label.config(text="Atbash gematria: 0")

# Action buttons now use fg='black'
action_btn_style = {
    'font': ('Arial', 12, 'bold'),
    'relief': RAISED,
    'bd': 2,
    'padx': 12,
    'pady': 6,
    'fg': 'black'          # black text for all action buttons
}

btn_calc = Button(action_frame, text="Calculate Gematria", command=calculate_original,
                  bg='#2ecc71', activebackground='#27ae60', **action_btn_style)
btn_calc.grid(row=0, column=0, padx=5)

btn_atbash = Button(action_frame, text="Atbash", command=show_atbash,
                    bg='#9b59b6', activebackground='#8e44ad', **action_btn_style)
btn_atbash.grid(row=0, column=1, padx=5)

btn_clear = Button(action_frame, text="Clear", command=clear_all,
                   bg='#e67e22', activebackground='#d35400', **action_btn_style)
btn_clear.grid(row=0, column=2, padx=5)

# Checkbox text remains white (you can change to black if preferred)
chk = Checkbutton(action_frame, text="Aleph = 1000", variable=aleph_1000,
                  bg='#0a3b5a', fg='white', selectcolor='#0a3b5a',
                  activebackground='#0a3b5a', activeforeground='white',
                  font=('Arial', 11, 'bold'))
chk.grid(row=0, column=3, padx=(20, 0))

root.mainloop()
