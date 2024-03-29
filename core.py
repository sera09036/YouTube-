import webbrowser
from yt_dlp import YoutubeDL 
import tkinter as tki
from tkinter import filedialog, messagebox, ttk
import os
import threading
import sys

data = '''R0lGODlhIAAgAMZvADY2Nv8AAP8BATQ8PP8CAv8DAzo8PC9AQDNAQP8GBjhBQUBA
        QP8KCj1CQkFBQf8LCz1DQ0JCQv8MDENDQz1FRT1HR0RFRT5HR0NGRj5ISEZGRkdG
        RkdHR0dISEJKSkpISElJSUpKSkNNTUtLS0xMTEZOTk1MTE1NTU5OTk9PT1BQUFFR
        UVJSUkVWVlRUVEhYWFVVVV9hYf80NF1jY2VmZlBtbVpvb190dF92dmd0dF16emd9
        fWF/f2l9ff9VVWuAgHV+fmyCgv9bW/9fX/9gYHuLi/9oaP9paf9qav9sbP9tbf9u
        bvxvb5WPj/9xcXqYmPZ3d5qTk/Z5efl6enigoPh9fft9ffx+fpafn7Kbm6+dnbWe
        nrqdnbWfn7afn7agoL2enregoLyfn7Ojo9ycnLunp8Olpf+dne2kpPygoNWursG0
        tNOwsMK4uOOzs///////////////////////////////////////////////////
        /////////////////yH5BAEKAH8ALAAAAAAgACAAAAf+gH+Cg4SFhoeIiYqLjI2O
        j5CRhyOUISGUmJmalBsiLRaVlpQoKCksKyqkqqusIDNqZFEYKCorK6QjJCOCISmb
        vxE/SgRmFSkhgpgnILwrv5sTPUYEYhcrg7kjy4Igzs+Z0UcF1dfJurq8KpokKiQk
        Gg0UFAM6SQVhBx4I5pS62Zn+KNEYs6VLljVDBLjR0uWLlyYdLvULiAkFsj8GsPhg
        8EBCggAgH4iUgOYFiH4qVJzQZJFQGitToFSREYCJFChTrrApcZLExRG+Kl4khMMG
        FScF2tS4wUPQB13b/oTwNmooIQA7kBTgooAENqjMpFId0fLQkyXjrH3VdjGEOqGB
        hyIEIRIATAYVPylKzFR20IllOc4IKQOh0iZ3m/r+OcHCpwkgRWJwmKjpb+KwKG5h
        CuFggYZzJyiOuLS3H8pvz060fYuJRArRm9TxizoV9bdyf7LRHms7E+5sPpOh6P3L
        VzKgKVS4gLEihfPn0KNLZwHDhXPi2DVJ2s69u/fvhQIBADs=
        '''

class Application(tki.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        if not os.path.exists('media'):
            os.mkdir('media')
        self.master = master
        self.pack()
        self.pack_propagate(0)
        self.create_menu()
        self.create_widgets()
        self.create_downWidgets()

    def create_menu(self):
        menuber = tki.Menu(self.master)
        root.config(menu=menuber)
        menu_file = tki.Menu(menuber, tearoff=False)
        menu_file.add_command(label='終了', command=self.master.destroy)
        menuber.add_cascade(label='File', menu=menu_file)

    def create_widgets(self):
        frame1 = tki.LabelFrame(self.master,text='設定', foreground='LightGreen', bg='grey25')
        f0 = tki.Frame(frame1)
        f0.configure(bg='grey25')
        
        #ラベル
        path_label = tki.Label(f0)
        path_label['text'] = "Folder"
        path_label['bg'] = 'grey25'
        path_label['foreground'] = 'White'
        path_label.pack(fill = 'x', padx=10, pady= 5,  side = 'left')

        #パス指定
        self.get_path = tki.Entry(f0)
        self.get_path['width'] = 40
        self.get_path['bg'] = 'grey40'
        self.get_path['foreground'] = 'White'
        self.get_path.insert(tki.END,f'{os.path.dirname(os.path.abspath(sys.argv[0]))}\media')
        self.get_path.pack(fill = 'x', padx=10, pady= 5, side = 'left')

        #パス選択ボタン
        button_reference = tki.Button(f0)
        button_reference['text'] = '参照'
        button_reference['bg'] = 'grey25'
        button_reference['foreground'] = 'Red'
        button_reference['command'] = self.reference
        button_reference.pack(fill = 'x', padx=10, side = 'left')

        f1 = tki.Frame(frame1)
        f1.configure(bg='grey25')

        #ラベル
        link_label = tki.Label(f1,text='フォーマット指定', bg='grey25', foreground='White')
        link_label.pack(fill = 'x', padx=10, pady= 5, side = 'left')

        self.combo = ttk.Combobox(f1, width=40, state='readonly')
        self.combo['values'] = ('M4A (音声のみ)','MP4 (動画)')
        self.combo.current(0)
        self.combo.pack(fill = 'x', padx=10, pady= 5, side = 'left')

        f0.pack()
        f1.pack()
        frame1.pack(pady=15)

    def create_downWidgets(self):
        frame = tki.Frame(self.master)
        f0 = tki.Frame(frame)
        f1 = tki.Frame(frame)
        frame.configure(bg='grey25')
        f0.configure(bg='grey25')
        f1.configure(bg='grey25')

        #ラベル
        label = tki.Label(f0,text='URL：', bg='grey25', foreground='White')
        label.pack(fill = 'x', padx=5, pady= 10, side = 'left')

        #URLエントリー
        self.get_url = tki.Entry(f0)
        self.get_url['width'] = 50
        self.get_url['bg'] = 'grey40'
        self.get_url['foreground'] = 'White'
        self.get_url.pack(fill = 'x', pady=10, padx= 0, side = 'left')

        #クリアボタン
        clear_btn = tki.Button(f0)
        clear_btn['text'] = 'Clear'
        clear_btn['bg'] = 'grey25'
        clear_btn['foreground'] = 'Red'
        clear_btn['command'] = self.crearurl
        clear_btn.pack(fill = 'x', padx=5, pady= 10, side = 'left')

        #ダウンロードボタン
        self.get_button = tki.Button(f1)
        self.get_button['text'] = 'ダウンロード'
        self.get_button['width'] = 30
        self.get_button['height'] = 2
        self.get_button['bg'] = 'SeaGreen3'
        self.get_button['command'] = self.input_handler
        self.get_button.pack(fill = 'x', pady=10, padx=5, side='left')

        #ブラウザで開くボタン
        brows_btn = tki.Button(f1)
        brows_btn['text'] = 'ブラウザで開く'
        brows_btn['bg'] = 'SeaGreen3'
        brows_btn['width'] = 10
        brows_btn['height'] = 2
        brows_btn['command'] = self.open_brow
        brows_btn.pack(fill='x', pady=10, padx=5, side='left')

        f0.pack()
        f1.pack()
        frame.pack()


    def input_handler(self):
        try:
            os.chdir(self.get_path.get())
        except OSError as ose:
            messagebox.showerror('OSError', ose)
        else:
            if self.combo.get() == 'MP4 (動画)':
                self.callbackm4(self.get_url.get())

            elif self.combo.get() == 'M4A (音声のみ)':
                self.callbackm3(self.get_url.get())

    def youtubem4(self,url):
        self.get_button['text'] = 'ダウンロード中...'
        self.get_button['state'] = tki.DISABLED
        try:
            with YoutubeDL() as ydl:
                ydl.download([str(url)])
        except:
            messagebox.showerror('Error',f'無効なURLです()')
            self.get_button['state'] = tki.NORMAL
            self.get_button['text'] = 'ダウンロード'
        else:
            self.get_button['state'] = tki.NORMAL
            self.get_button['text'] = 'ダウンロード'
            messagebox.showinfo('YouTube+', 'ダウンロードが完了しました！')

    def callbackm4(self,url):
        thread = threading.Thread(target=self.youtubem4, args=(url,))
        thread.start()

        
    def youtubem3(self,url):
        self.get_button['text'] = 'ダウンロード中...'
        self.get_button['state'] = tki.DISABLED
        try:
            ydl_ops = ({'outtmpl': '%(id)s'+'_.mp3', 'format': 'bestaudio'})
            with YoutubeDL(ydl_ops) as ydl:
                ydl.download([str(url)])
        except:
            messagebox.showerror('Error', f'無効なURLです()')
            self.get_button['state'] = tki.NORMAL
            self.get_button['text'] = 'ダウンロード'

        else:
            self.get_button['state'] = tki.NORMAL
            self.get_button['text'] = 'ダウンロード'
            messagebox.showinfo('YouTube+', 'ダウンロードが完了しました！')

    def callbackm3(self,url):
        thread = threading.Thread(target=self.youtubem3, args=(url,))
        thread.start()

    def reference(self):
        self.get_path.delete(0, tki.END)
        self.get_path.insert(tki.END, filedialog.askdirectory())
    
    def crearurl(self):
        self.get_url.delete(0, tki.END)

    def open_brow(self):
        if self.get_url.get() != '':
            webbrowser.open(self.get_url.get())
        else:
            webbrowser.open('https://www.youtube.com/')




root = tki.Tk()
root.title('YYouTube+')
root.geometry('580x330')
root.configure(bg='grey25')
root.resizable(False, False)
root.tk.call('wm', 'iconphoto', root._w, tki.PhotoImage(data=data))
app = Application(master=root)
app.mainloop()
