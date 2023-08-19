from tkinter import *  # type: ignore
from tkinter import ttk


class Enhance_Tkinter():
    
    def __init__(self) -> None:
        self._version = "Version: 1.4"
        self._Publisher = "By NooR MaseR"
    
    class Change_Titlebar():
        """removes the Titlebar and adding a new one and it's customizable!!
            >>> from TOOLS.enhance_tkinter import Enhance_Tkinter
            >>> en_widget = Enhance_Tkinter.Change_Titlebar(root)
        ----
        that's it !!!\n
        now you don't need to type tenth of codes anymore\n
        only 2 lines of code
        """
        def __init__(
            self,
            parent,
            titlebar_Title: str = "Advanced Tkinter",
            titlebar_bg: str = "systembuttonface",
            title_bg: str = "systembuttonface",
            title_fg: str = "black",
            title_font: tuple[str,int,str] = ("Arial", 10,"normal"),
            Padx: int | tuple = 5,
            Pady: int | tuple = 5,
            border: int = 0,
            color_exit_defualt_bg: str = "white",
            color_exit_defualt_fg: str = "black",
            color_exit_on_enter_bg: str = "red",
            color_exit_on_enter_fg: str = "white",
            color_exit_on_leave_bg: str = "white",
            color_exit_on_leave_fg: str = "black",
            color_exit_on_click_bg: str = "red",
            color_exit_on_click_fg: str = "white"
            ) -> None:

            self.parent = parent
            self.titlebar_Title = titlebar_Title
            self.titlebar_bg = titlebar_bg
            self.title_bg = title_bg
            self.title_fg = title_fg
            self.title_font = title_font
            self.Padx = Padx
            self.Pady = Pady
            self.border = border
            self.color_exit_defualt_bg = color_exit_defualt_bg
            self.color_exit_defualt_fg = color_exit_defualt_fg
            self.color_exit_on_enter_bg = color_exit_on_enter_bg
            self.color_exit_on_enter_fg = color_exit_on_enter_fg
            self.color_exit_on_leave_bg = color_exit_on_leave_bg
            self.color_exit_on_leave_fg = color_exit_on_leave_fg
            self.color_exit_on_click_bg = color_exit_on_click_bg
            self.color_exit_on_click_fg = color_exit_on_click_fg
        
            
            def __move_window(e) -> None:
                self.parent.geometry(f"+{e.x_root}+{e.y_root}")

            def __on_enter(e) -> None:
                self.exit_button.config(bg = self.color_exit_on_enter_bg, fg = self.color_exit_on_enter_fg)

            def __on_leave(e) -> None:
                self.exit_button.config(bg = self.color_exit_on_leave_bg, fg = self.color_exit_on_leave_fg)

            
            
            self.parent.overrideredirect(True)
            self.frame = Frame(self.parent, bg = self.titlebar_bg, relief="raised")
            self.frame.pack(fill="x")

            self.label = Label(
                self.frame,
                text = self.titlebar_Title,
                bg = self.title_bg,
                fg = self.title_fg,
                font = self.title_font,
                bd = self.border,
            )
            self.label.pack(side=LEFT, pady = self.Padx, padx = self.Pady)

            self.exit_button = Button(
                self.frame,
                text="X",
                bg = self.color_exit_defualt_bg,
                fg = self.color_exit_defualt_fg,
                font = self.title_font,
                command=quit,
                width=3,
                bd=0,
                cursor="hand2",
                activebackground = self.color_exit_on_click_bg,
                activeforeground = self.color_exit_on_click_fg,
            )
            self.exit_button.pack(side="right")
            self.exit_button.bind("<Enter>", __on_enter)
            self.exit_button.bind("<Leave>", __on_leave)

            self.frame.bind("<B1-Motion>", __move_window)
            
        def Set_title(self,title:str, fg_color:str = "black", bg_color:str = "white", Font:tuple[str,int,str] = ("Arial", 10,"normal")) -> None:
            self.label.configure(text=title, fg=fg_color, bg=bg_color, font=Font)
            
        def Set_bg(self,bg_color:str) -> None:
            self.frame.configure(bg=bg_color)
