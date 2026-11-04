import customtkinter as ctk

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