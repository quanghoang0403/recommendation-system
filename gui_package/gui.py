import tkinter
from tkinter import *
from tkinter import ttk


def main(cf_rs, cb_rs, list_name_movie, list_year_movie):
    def get_id_user():
        """
        Lấy id người dùng và trả về danh sách phim
        """
        tv.delete(*tv.get_children())
        x1 = entry1.get()
        list_movies = cf_rs.recommend_top(int(x1),200)
        for i in range(200):
            tv.insert(parent='', index=i, iid=i, text='',
                      values=('{0:.{1}f}'.format(list_movies[i]['similar'], 2),
                              list_name_movie[list_movies[i]['id']],
                              list_year_movie[list_movies[i]['id']]))

    root = Tk()
    root.title('Recommendation System')
    root.iconbitmap('assets/logo.ico')
    root.resizable(False, False)

    window_height = 450
    window_width = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
    root.deiconify()

    canvas1 = tkinter.Canvas(root, width=window_width, height=window_height)
    canvas1.pack()

    label1 = tkinter.Label(root, text='Welcome to Recommendation System')
    label1.config(font=('Segoe UI Semibold', 14))
    canvas1.create_window(250, 40, window=label1)

    label2 = tkinter.Label(root, text='Type your id here')
    label2.config(font=('Segoe UI Symbol', 10))
    canvas1.create_window(175, 95, window=label2)

    entry1 = tkinter.Entry(root)
    canvas1.create_window(300, 95, window=entry1)

    button1 = tkinter.Button(text='Suggest me', command=get_id_user, bg='brown', fg='white',
                             font=('helvetica', 9, 'bold'))
    canvas1.create_window(250, 135, window=button1)

    tv = ttk.Treeview(root)
    tv['columns'] = ("SIMILAR RATE", "MOVIE NAME", "RELEASE DATE")
    tv.column('#0', width=0, stretch=NO)
    tv.column('SIMILAR RATE', anchor=CENTER, width=90)
    tv.column('MOVIE NAME', anchor=W, width=230)
    tv.column('RELEASE DATE', anchor=CENTER, width=90)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('SIMILAR RATE', text='SIMILAR RATE', anchor=CENTER)
    tv.heading('MOVIE NAME', text='MOVIE NAME', anchor=CENTER)
    tv.heading('RELEASE DATE', text='RELEASE DATE', anchor=CENTER)

    def on_double_click(e):
        """
        Trả về danh sách phim phù hợp với phim vừa chọn
        :param e:
        :return:
        """
        item = tv.selection()[0]
        new_window = Toplevel(root)
        new_window.title("Content-based RS")
        new_window.geometry("440x350")
        cb_canvas = tkinter.Canvas(new_window)
        cb_canvas.pack()

        cb_label = tkinter.Label(new_window, text="This is list movies similarity with \n" + tv.item(item)['values'][1])
        cb_label.config(font=('Segoe UI Semibold', 10))
        cb_canvas.create_window(200, 40, window=cb_label)

        cb_tv = ttk.Treeview(new_window)
        cb_tv['columns'] = ("SIMILAR RATE", "MOVIE NAME", "ID MOVIE")
        cb_tv.column('#0', width=0, stretch=NO)
        cb_tv.column('SIMILAR RATE', anchor=CENTER, width=80)
        cb_tv.column('MOVIE NAME', anchor=W, width=200)
        cb_tv.column('ID MOVIE', anchor=CENTER, width=70)

        cb_tv.heading('#0', text='', anchor=CENTER)
        cb_tv.heading('SIMILAR RATE', text='SIMILAR RATE', anchor=CENTER)
        cb_tv.heading('MOVIE NAME', text='MOVIE NAME', anchor=CENTER)
        cb_tv.heading('ID MOVIE', text='ID MOVIE', anchor=CENTER)

        list_similarity, list_movies_cb = cb_rs.genre_recommendations(tv.item(item)['values'][1], 200)
        for i in range(200):
            cb_tv.insert(parent='', index=i, iid=i, text='',
                         values=('{0:.{1}f}'.format(list_similarity[i][1], 2),
                                 list_movies_cb[i],
                                 list_similarity[i][0]))
        cb_canvas.create_window(190, 200, window=cb_tv)

    tv.bind("<Double-1>", on_double_click)

    canvas1.create_window(250, 290, window=tv)

    root.mainloop()
