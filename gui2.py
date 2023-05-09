from tkinter import *
import formulas

class GUI:
    def __init__(self, window):
    
        self.window = window
        #number input
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Enter numbers (ex: 10 20):')
        self.num_input = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='top')
        self.num_input.pack(padx=5, side='top')
        self.frame_name.pack(anchor='center', pady=10)
        
        #operators buttons
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Choose an operation:')
        self.label_name.pack(padx=5, side='top')
        
        self.frame_name.pack(anchor='center', pady=10)
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_add = Radiobutton(self.frame_name, text = 'ADD', variable =self.radio_1, value = 1)
        self.radio_subtract = Radiobutton(self.frame_name, text='SUBTRACT', variable=self.radio_1, value=2)
        self.radio_multiply = Radiobutton(self.frame_name, text='MULTIPLY', variable=self.radio_1, value=3)
        self.radio_divide = Radiobutton(self.frame_name, text='DIVIDE', variable=self.radio_1, value=4)
        self.radio_add.pack(side='left')
        self.radio_subtract.pack(side='left')
        self.radio_multiply.pack(side='left')
        self.radio_divide.pack(side='left')
        self.frame_name.pack(anchor='center', pady=10)
        
        #calculate button
        self.frame_bottom = Frame(self.window)
        self.calculate_button = Button(self.frame_bottom, text='CALCULATE', command=self.calculate)
        self.calculate_button.pack()
        self.frame_bottom.pack()
        
        #answer display
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Answer')
        self.label_name.pack(padx=5, side='top')
        self.frame_name.pack(anchor='center', pady=10)
        
        self.frame_answer = Frame(self.window)
        self.answer_output = Label(self.frame_answer)
        self.answer_output.pack(pady=10)
        self.frame_answer.pack()
        
        #self.frame_answer.pack()shape = self.radio_1.get()
        
    def calculate(self):
        operator = self.radio_1.get()
        user_input = self.num_input.get()
        values = user_input.split(' ')
        values = [float(i) for i in values]
        
        if operator == 1:
            self.answer_output.config(text=f'{formulas.add(values):.2f}')
        elif operator == 2:
            self.answer_output.config(text=f'{formulas.subtract(values):.2f}')
        elif operator == 3:
            self.answer_output.config(text=f'{formulas.multiply(values):.2f}')
        elif operator == 4:
            self.answer_output.config(text=f'{formulas.divide(values):.2f}')
        self.radio_1.set(0)
        self.num_input.delete(0, END)
        
        #self.answer_output.config(text=f'{total:.2}')