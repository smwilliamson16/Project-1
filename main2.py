from gui2 import *


def main():
    """
    - Change the window title to 'Lab 10'.
    - Set its length to 250 and height to 200.
    - Make the window non-resizable.
    """
    window = Tk()
    window.title('Lab 10')
    window.geometry('400x300')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()