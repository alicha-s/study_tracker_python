import customtkinter as ctk
from ui.buttons import HomeButtons
from ui.headers import TableHeader
from ui.rows import NewRow

class Main_ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self,master):
        super().__init__(master)
        self.configure(fg_color="transparent")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        window_height = self.winfo_screenheight()
        window_width = self.winfo_screenwidth()
        self.geometry(f"{window_width}x{window_height}")
        self.configure(fg_color="#BED3AE")

        self.grid_rowconfigure(1, weight=1)

        self.scrollframe = Main_ScrollableFrame(self)
        self.scrollframe.grid(row=1,column=0,columnspan=7,sticky="nsew")

        #settings: buttons config
        self.clicked = False
        self.rownum = 2
        self.add_btn_row = 2
        self.del_btn_row = 3

        #settings: frame padx/pady
        self.header_pady = 10

        self.checkbox_header = TableHeader(master=self,
                                          header_name="",
                                          label_width=50)
        self.checkbox_header.grid(row=0,column=0, padx=(20,0), pady=self.header_pady)


        headers = ["Subject","Topic","Session","Complete"]

        #settings: label width
        label_widths =  [500,375,90,90]

        for col,header in enumerate(headers):
            self.subject_header = TableHeader(master=self,
                                            header_name=header,
                                            label_width=label_widths[col])
            self.subject_header.grid(row=0,column=col+1, pady=self.header_pady)

        self.progress_header = TableHeader(master=self,
                                           header_name="Progress",
                                           label_width=90)
        self.progress_header.grid(row=0,column=5, padx=(0,10),pady=self.header_pady)

        """buttons process"""
        self.add_button = HomeButtons(master=self.scrollframe,
                                           button_name="add subject",
                                           button_func=self.add_row)
        self.add_button.grid(row=self.add_btn_row,column=0,padx=(20, 0),pady=self.header_pady,columnspan=6,sticky="ew")

        self.del_button = HomeButtons(master=self.scrollframe,
                                         button_name="delete subject",
                                         button_func=self.delete_row)
        self.del_button.grid(row=self.del_btn_row,column=0,padx=(20, 0), pady=self.header_pady,columnspan=6,sticky="ew")    


    def add_row(self):
        self.newrow = NewRow(self.scrollframe)
        self.newrow.grid(row=self.rownum,
                         column=0,
                         columnspan=6,
                         padx=(20, 0),
                         pady=self.header_pady,
                         sticky="ew"
                         )
        
        self.clicked = True
        if self.clicked:
            self.rownum += 1
            add_btn_info = self.add_button.grid_info()
            self.add_btn_row = int(add_btn_info["row"])
            self.add_button.grid(row=self.add_btn_row+1,
                                 column=0,padx=(20, 0),
                                 pady=self.header_pady,
                                 columnspan=6,
                                 sticky="ew")

            del_btn_info = self.del_button.grid_info()
            self.del_btn_row = int(del_btn_info["row"])
            self.del_button.grid(row=self.del_btn_row+1,
                                 column=0,padx=(20, 0),
                                 pady=self.header_pady,
                                 columnspan=6,
                                 sticky="ew")

    def delete_row(self):
            add_btn_info = self.add_button.grid_info()
            self.add_btn_row = int(add_btn_info["row"])
            self.add_button.grid(row=self.add_btn_row-1,
                                 column=0,padx=(20, 0),
                                 pady=self.header_pady,
                                 columnspan=6,
                                 sticky="ew")

            del_btn_info = self.del_button.grid_info()
            self.del_btn_row = int(del_btn_info["row"])
            self.del_button.grid(row=self.del_btn_row-1,
                                 column=0,padx=(20, 0),
                                 pady=self.header_pady,
                                 columnspan=6,
                                 sticky="ew")


if __name__ == "__main__":
    app = App()
    app.mainloop()


