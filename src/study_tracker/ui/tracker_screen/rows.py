import customtkinter as ctk

class NewRow(ctk.CTkFrame):
    def __init__(self,master,check_var):
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
                                        width=50,
                                        variable=check_var)
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