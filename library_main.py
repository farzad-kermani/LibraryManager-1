#_________________________________Importes Mudoles___________________________________________>>>  


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import library_database


        
#_________________________________Creat Class & Functiones___________________________________________>>>  

class LibraryManagementApp:
    def __init__(self, page):
        self.page = page    
        image_path='Book.png'
        self.image = tk.PhotoImage(file = image_path)
        page_width = self.page.winfo_screenwidth()                       # 
        page_height = self.page.winfo_screenheight()                     #
        Screen_width = 550; Screen_height = 480                          # } موقعیت قرار گرفتن پنجره اول
        x = (page_width // 2) - (Screen_width // 2)                      #
        y = (page_height // 2) -(Screen_height // 2)                     #
        self.page.geometry(f'{Screen_width}x{Screen_height}+{x}+{y}')    #
        self.page.title('برنامه مدیریت کتابخانه')
        self.page.resizable(0,0)
        icon_path = 'bag.ico'
        self.page.iconbitmap(icon_path)                   
        Label_Wellcom=tk.Label(page,text='به سامانه مدیریت کتاب خوش آمدید',compound='center',bg='gold')
        Label_Wellcom.config(font = ('Arial',30,'bold'))
        Label_Wellcom.pack()
        label_IMG = tk.Label(page,text=' کتابخانه   مجازی',bd=7)
        label_IMG.config(image=self.image,compound = 'center',font = ('Arial',25,'bold'),fg = 'blue')
        label_IMG.pack()

        #____________________________Button_Stars_Button______________________________________>>>    
        Button_Stars =tk.Button(page,text ='شروع',font = ('Arial',18,'bold'),bd = 8,command = self.main)
        Button_Stars.pack(pady = 20)
        
                

        
#_________________________________Main Functiones For Main Window___________________________________________>>>  

    def main(self):
        '''This function designs the main window of the program.
تابع ای است که چنجره اصلی برنامه را باز میکند 

'''
        page.withdraw() #ّ page is hiden
        window = tk.Toplevel(self.page)
        window.title("Library Management System")
        window.title('کتابخانه')
        Top_width = window.winfo_screenwidth()                       #
        Top_height = window.winfo_screenheight()                     #
        window_width = 595; window_height = 550                      #  }  موقعیت قرار گرفتن پنجره دوم
        n = (Top_width // 2) - (window_width // 2)                   #  
        m = (Top_height // 2) -(window_height // 2)                  #
        window.geometry(f'{window_width}x{window_height}+{n}+{m}')   #
        window.resizable(0,0)
        icon_File = 'books.ico'
        window.iconbitmap(icon_File)
        self.book_id = tk.StringVar(window)
        self.book_title = tk.StringVar(window)
        self.book_author = tk.StringVar(window)
        self.book_publisher = tk.StringVar(window)
        self.book_year = tk.StringVar(window)
        search_book = tk.StringVar(window)
#______________________________Book_List_Label_Frame_____________________________________
        Book_list = tk.LabelFrame(window,text = 'لیست کتاب های موجود',bd = 8)
        Book_list.pack(fill = 'both',expand = 'yes')
        self.tree = ttk.Treeview(Book_list, columns=('id','Title', 'Author', 'Publisher', 'Year'))

        # اضافه کردن اسکرولبار عمودی
        yscroll = ttk.Scrollbar(Book_list, orient="vertical", command=self.tree.yview)
        yscroll.pack(side = 'right', fill = 'y')
        self.tree.configure(yscrollcommand = yscroll.set)

        # اضافه کردن اسکرولبار افقی
        xscroll = ttk.Scrollbar(Book_list, orient="horizontal", command=self.tree.xview)
        xscroll.pack(side="bottom", fill="x")
        self.tree.configure(xscrollcommand = xscroll.set)

        self.tree.heading('id', text='شناسه کتاب')
        self.tree.heading('Title', text='نام کتاب')
        self.tree.heading('Author', text='نویسنده')
        self.tree.heading('Publisher', text='ناشر')
        self.tree.heading('Year', text='سال نشر')
        self.tree.pack(expand=True, fill="both")
        
        
#_______________________book_Entry_LabelFrame_________________________>>>    
        book_Entry = tk.LabelFrame(window,text = 'ثبت کتاب جدید',bd = 8)
        book_Entry.pack(fill='both',expand='yes')
        
        Title_Book_Label=ttk.Label(book_Entry,text='نام کتاب')
        Title_Book_Label.grid(row=0,column=0)
        self.Title_Book_Entry=ttk.Entry(book_Entry,textvariable=self.book_title)
        self.Title_Book_Entry.grid(row=0,column=1)
        Author_Book_Label=ttk.Label(book_Entry,text='نویسنده')
        Author_Book_Label.grid(row=0,column=2)
        self.Author_Book_Entry=ttk.Entry(book_Entry,textvariable=self.book_author)
        self.Author_Book_Entry.grid(row=0,column=3)

        Line1=ttk.Label(book_Entry,text='')
        Line1.grid(row=1,column=0)

        Publisher_Book_Label=ttk.Label(book_Entry,text='ناشر')
        Publisher_Book_Label.grid(row=2,column=0)
        self.Publisher_Book_Entry=ttk.Entry(book_Entry,textvariable=self.book_publisher)
        self.Publisher_Book_Entry.grid(row=2,column=1)
        Year_Book_Label=ttk.Label(book_Entry,text='سال انتشار')
        Year_Book_Label.grid(row=2,column=2)
        self.Year_Book_Entry=ttk.Entry(book_Entry,textvariable=self.book_year,width=5)
        self.Year_Book_Entry.grid(row=2,column=3)

        id_Book_Label=ttk.Label(book_Entry,text='شناسه کتاب')
        id_Book_Label.grid(row=2,column=4)
        self.id_Book_Entry=ttk.Entry(book_Entry,textvariable=self.book_id,width=5)
        self.id_Book_Entry.grid(row=2,column=5)       

        Line2=ttk.Label(book_Entry,text='')
        Line2.grid(row=3,column=0)

        Search_Book_Label=ttk.Label(book_Entry,text='جستجو')
        Search_Book_Label.grid(row=4,column=0)

        self.Search_Book_Entry=ttk.Entry(book_Entry,textvariable=search_book)
        self.Search_Book_Entry.grid(row=4,column=1)

        ButtonSearch = ttk.Button(book_Entry,width=15,  text = 'جستوجو',command=self.search_and_display)
        ButtonSearch.grid(row=4,column=3)

        lbchoose = ttk.Label(book_Entry, text=':  بر اساس نام کتاب')
        lbchoose.grid(row=4,column=2)

        self.tree.bind('<<TreeviewSelect>>', self.on_select)
#________________________book_Button_LabelFrame_______________________>>>
        book_Button = tk.LabelFrame(window,text = 'ویرایش',bd = 8)
        book_Button.pack(fill='both',expand='yes')

        Button_show = ttk.Button(book_Button,width=15,  text = 'نمایش همه',command=self.show_all_books)
        Button_show.grid(row=0,column=0)
        Button_submit = ttk.Button(book_Button,width=15,  text = 'ثبت',command=self.submit)
        Button_submit.grid(row=0,column=1)
        Button_Delete = ttk.Button(book_Button,width=15,  text = 'حذف',command = self.delete_book_data)
        Button_Delete.grid(row=0,column=2)
        Button_cancel = ttk.Button(book_Button,width=15,  text = 'لغو', command = self.cancel)
        Button_cancel.grid(row=0,column=3)

        Button_Exit = ttk.Button(book_Button,command=quit,  text = 'خروج',width=15)
        Button_Exit.grid(row=0,column=4)

        Line3=ttk.Label(book_Button)
        Line3.grid(row=1,column=0)

        Home_Button=ttk.Button(book_Button,text='پنجره قبلی',command=page.deiconify)
        Home_Button.grid(row=2,column=2) 

#________________________MenuBar_Design_____________________________>>>
        MenuBar=tk.Menu(window)
        file = tk.Menu(MenuBar,tearoff=0,bg='gold')
        file.add_command(label='نمایش همه',command=self.show_all_books)
        file.add_command(label='ثبت',command = self.submit)
        file.add_command(label='حذف',command = self.delete_book_data)
        file.add_command(label='لغو',command = self.cancel)
        file.add_command(label='جستوجو',command=self.search_and_display)
        file.add_command(label='صفحه قبلی',command=page.deiconify)
        file.add_separator()
        file.add_command(label='خروج',command=window.quit)
        MenuBar.add_cascade(label='منوی خدمات',menu=file)
        window.config(menu=MenuBar)


    def show_all_books(self):
        books = library_database.get_all_books()
        
        for book in books:
            self.tree.insert('', 'end', text=('کتاب شماره :',book[0]), values=(book[0], book[1], book[2], book[3],book[4]))

    def submit(self):
        n_id=None
        title = self.Title_Book_Entry.get()   
        author = self.Author_Book_Entry.get()
        publisher = self.Publisher_Book_Entry.get()
        year = self.Year_Book_Entry.get()
        
        library_database.add_book(title,author,publisher,year)

        self.tree.insert('','end',values = (n_id,title,author,publisher,year))
        messagebox.showinfo('ثبت کتاب جدید', 'کتاب با موفقیت ثبت شد')
        
    def cancel(self):
        self.id_Book_Entry.delete(0,'end')
        self.Title_Book_Entry.delete(0,'end')             
        self.Author_Book_Entry.delete(0,'end')
        self.Publisher_Book_Entry.delete(0,'end')
        self.Year_Book_Entry.delete(0,'end')
        messagebox.showinfo('لغو عملیات  ', 'عملیات شما لغو گردید')
    
   
    def delete_book_data(self):
        if self.id_Book_Entry is not None:
            confirmation = messagebox.askyesno('هشدار','آیا میخواهید این کتاب حذف شود ؟؟؟')
            if confirmation:
                book_id = self.id_Book_Entry.get()
                library_database.delete_book(book_id)
                self.id_Book_Entry.delete(0, tk.END)
                self.Title_Book_Entry.delete(0, tk.END)
                self.Author_Book_Entry.delete(0, tk.END)
                self.Publisher_Book_Entry.delete(0, tk.END)
                self.Year_Book_Entry.delete(0, tk.END)
                messagebox.showinfo('حذف کتاب','حذف کتاب با موفقیت انجام شد !')
            else:
                messagebox.showinfo('لغو عملیات','عملیات حذف کتاب لغو شد')  
        else:
            messagebox.showerror('خطا','شما هیچ کتابی را انتخاب نکردید !')          
           


    def on_select(self, event):
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, 'values')

        self.id_Book_Entry.delete(0, tk.END)
        self.id_Book_Entry.insert(0, values[0])

        
        self.Title_Book_Entry.delete(0, tk.END)
        self.Title_Book_Entry.insert(0, values[1])

        self.Author_Book_Entry.delete(0, tk.END)
        self.Author_Book_Entry.insert(0, values[2])

        self.Publisher_Book_Entry.delete(0, tk.END)
        self.Publisher_Book_Entry.insert(0, values[3])

        self.Year_Book_Entry.delete(0, tk.END)
        self.Year_Book_Entry.insert(0, values[4])

    def search_and_display(self):
        title = self.Search_Book_Entry.get()
        book = library_database.search_books_by_title(title)
        # print(book)
        if book is not None:
            self.id_Book_Entry.delete(0,'end')
            self.Title_Book_Entry.delete(0,'end')             
            self.Author_Book_Entry.delete(0,'end')
            self.Publisher_Book_Entry.delete(0,'end')
            self.Year_Book_Entry.delete(0,'end')
            
            self.book_id.set(book[0][0])
            self.book_title.set(book[0][1])
            self.book_author.set(book[0][2])
            self.book_publisher.set(book[0][3])
            self.book_year.set(book[0][4])
        else:
            messagebox.showerror('خطا','کتاب مورد نظر یافت نشد !')    

                    
#_________________________________Run App___________________________________________>>>  
if __name__ == '__main__':
    library_database.create_table()

    page = tk.Tk()
    app = LibraryManagementApp(page)
    page.mainloop()