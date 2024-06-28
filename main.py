from tkinter import *
from tkinter import ttk

primaryColor = "#3e4f82"

class BookstoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sebo Manager")
        self.root.geometry("800x500")
        self.root.configure(background=primaryColor)
        self.root.resizable(False, False)
        
        self.create_widgets()
        
    def create_widgets(self):   
        # Frame for book list
        self.frame_list = Frame(self.root)
        self.frame_list.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.4)
        
        #Stylizing
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
            rowheight=25               
        )

        # Treeview para listar os livros
        self.book_tree = ttk.Treeview(self.frame_list, columns=("Title", "Price", "Quantity"), show="headings")
        
        # Configurando as colunas
        self.book_tree.heading("Title", text="Título")
        self.book_tree.heading("Price", text="Preço")
        self.book_tree.heading("Quantity", text="Quantidade")
        
        # Adicionando alguns dados de exemplo
        self.book_tree.insert("", "end", values=("Almas ao vento", "R$ 25", "1"))
        self.book_tree.insert("", "end", values=("O Alquimista", "R$ 20", "2"))
        self.book_tree.insert("", "end", values=("O Ceifador", "R$ 15", "1"))
        self.book_tree.insert("", "end", values=("Sherlock Holmes", "R$ 15", "1"))
        
        # Ajustando largura das colunas
        self.book_tree.column("Title", width=360)
        self.book_tree.column("Price", width=20, anchor="center")
        self.book_tree.column("Quantity", width=20, anchor="center")
        
        # Empacotando o Treeview
        self.book_tree.place(relx=0.025, rely=0.1, relwidth=0.95, relheight=0.80)
        
        # Frame para detalhes do livro
        self.frame_details = Frame(self.root)
        self.frame_details.place(relx=0.02, rely=0.44, relwidth=0.96, relheight=0.54)
        
        # Search bar
        self.search_var = StringVar()
        self.search_entry = Entry(self.frame_details, textvariable=self.search_var, width=60)
        self.search_entry.pack(pady=25)

        self.search_button = Button(self.frame_details, text="Buscar", bg=primaryColor, fg="white", width=10)
        self.search_button.pack()
        
        # Detalhes Livro
        details_frame = Frame(self.frame_details)
        details_frame.pack(pady=20)
        
        Label(details_frame, text="Titulo:").grid(row=0, column=0, sticky=W, pady=2)
        self.title_entry = Entry(details_frame, width=50)
        self.title_entry.grid(row=0, column=1, sticky=W, pady=2)
        
        Label(details_frame, text="Preço:").grid(row=1, column=0, sticky=W, pady=2)
        self.price_entry = Entry(details_frame, width=7)
        self.price_entry.grid(row=1, column=1, sticky=W, pady=2)
        
        Label(details_frame, text="Quantidade:").grid(row=2, column=0, sticky=W, pady=2)
        self.quantity_entry = Entry(details_frame, width=7)
        self.quantity_entry.grid(row=2, column=1, sticky=W, pady=2)
        
        # Buttons for actions
        self.add_button = Button(details_frame, text="Salvar", width=10, bg=primaryColor, fg="white")
        self.add_button.grid(row=3, column=0, pady=10, padx=5)
        
        self.sell_button = Button(details_frame, text="Vender", width=10, bg=primaryColor, fg="white")
        self.sell_button.grid(row=3, column=1, pady=10, padx=5)
        
        self.exchange_button = Button(details_frame, text="Trocar", width=10, bg=primaryColor, fg="white", command=self.show_exchange_form)
        self.exchange_button.grid(row=3, column=2, pady=20, padx=5)
        
    def show_exchange_form(self):
        self.exchange_window = Toplevel(self.root)
        self.exchange_window.title("Trocar Livro")
        self.exchange_window.geometry("400x300")
        
        Label(self.exchange_window, text="Livro Recebido", font=("Arial", 14)).pack(pady=10)
        
        Label(self.exchange_window, text="Titulo:").pack(pady=5)
        self.new_title_entry = Entry(self.exchange_window, width=50)
        self.new_title_entry.pack(pady=5)
        
        Label(self.exchange_window, text="Preço:").pack(pady=5)
        self.new_price_entry = Entry(self.exchange_window, width=20)
        self.new_price_entry.pack(pady=5)
        
        Label(self.exchange_window, text="Quantidade:").pack(pady=5)
        self.new_quantity_entry = Entry(self.exchange_window, width=20)
        self.new_quantity_entry.pack(pady=5)
        
        Button(self.exchange_window, text="Adicionar Livro", width=15, bg=primaryColor, fg="white", command=self.add_new_book).pack(pady=20)

    def add_new_book(self):
        new_title = self.new_title_entry.get()
        new_price = self.new_price_entry.get()
        new_quantity = self.new_quantity_entry.get()
        
        if new_title and new_price and new_quantity:
            self.book_tree.insert("", "end", values=(new_title, new_price, new_quantity))
            self.exchange_window.destroy()

if __name__ == "__main__":
    root = Tk()
    app = BookstoreApp(root)
    root.mainloop()
