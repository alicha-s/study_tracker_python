import customtkinter as ctk

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