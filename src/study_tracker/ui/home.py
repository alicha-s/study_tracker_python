import customtkinter as ctk

class NewRow(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.configure(fg_color="transparent")
        self.font_color = "#1D2E0F"
        self.font_config =("Nunito", 16)

        self.checkbox = ctk.CTkCheckBox(self,
                                        corner_radius=0,
                                        border_color="#6A8257",
                                        border_width=1.5,
                                        bg_color="transparent",
                                        fg_color="#D4E4D4",
                                        hover_color="#9A9B9A",
                                        checkmark_color="#252E1E",
                                        text=None,
                                        width=50)
        self.checkbox.grid(row=0, column=0, padx=(5,0))

        column_widths = [490,375,90,90,90]

        for col,cw in enumerate(column_widths):
            self.subject_entry = ctk.CTkEntry(self,
                                            corner_radius=0,
                                            border_width=1,
                                            border_color="#A0BB8C",
                                            width=cw,
                                            fg_color="transparent")
            self.subject_entry.grid(row=0, column=col+1)


class HomeButtons(ctk.CTkFrame):
    def __init__(self,master,button_name,button_func):
        super().__init__(master)
        self.button_name = button_name
        self.button_func = button_func
        self.configure(fg_color="transparent")
        self.font_color = "#1D2E0F"
        self.font_config =("Nunito", 16)

        self.button = ctk.CTkButton(self,
                                    text=self.button_name,
                                    text_color=self.font_color,
                                    font=self.font_config,
                                    fg_color="#D7E4C6",
                                    corner_radius=3,
                                    border_color="#A0B18A",
                                    border_width=1,
                                    hover_color="#819770",
                                    command=self.button_func)
        self.button.grid(row=1,column=0,padx=0,pady=0)

        
class TableHeader(ctk.CTkFrame):
    def __init__(self,master,header_name,label_width):
        super().__init__(master)
        self.header_name = header_name
        self.label_width = label_width
        self.configure(fg_color="transparent")
        self.font_color = "#1B3D00"
        self.font_config =("Nunito", 16, "bold")

        self.label = ctk.CTkLabel(self, 
                                  text=self.header_name,
                                  font=self.font_config,
                                  text_color=self.font_color,
                                  width=label_width,
                                  corner_radius=0,
                                  fg_color="#D7E4C6",
                                  border_color="#5F7148",
                                  border_width = 1.5,
                                  height=35)
        self.label.grid(row=0, column=0,padx=0,pady=25)


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


