from tkinter import *
 
class UITest:
        
    # удаление выделенного элемента
    def delete(language_entry,languages_listbox):
        selection = languages_listbox.curselection()
        # мы можем получить удаляемый элемент по индексу
        # selected_language = languages_listbox.get(selection[0])
        if selection:
            languages_listbox.delete(selection[0])
        else:
            print("Элемент не выбран")
 
    # добавление нового элемента
    def add(language_entry,languages_listbox):
        new_language = language_entry.get()

        if new_language:
            languages_listbox.insert(0, new_language)
            language_entry.delete(0,'end')
        else:
            print("Введите имя")
 
    def startFunc():
        
        root = Tk()
        root.title("GUI на Python")
 
        # текстовое поле и кнопка для добавления в список
        language_entry = Entry(width=40)
        language_entry.grid(column=0, row=0, padx=6, pady=6)
        
        add_button = Button(text="Добавить", command = lambda:UITest.add(language_entry,languages_listbox)).grid(column=1, row=0, padx=6, pady=6)
 
        # создаем список
        languages_listbox = Listbox()
        languages_listbox.grid(row=1, column=0, columnspan=2, sticky=W+E, padx=5, pady=5)
 
        # добавляем в список начальные элементы
        languages_listbox.insert(END, "Python")
        languages_listbox.insert(END, "C#")
 
        delete_button = Button(text="Удалить", command = lambda:UITest.delete(language_entry,languages_listbox)).grid(row=2, column=1, padx=5, pady=5)
 
        root.mainloop()