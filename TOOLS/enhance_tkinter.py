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
            parent: Tk,
            titlebar_Title: str = "Advanced Tkinter",
            titlebar_bg: str = "systembuttonface",
            title_bg: str = "systembuttonface",
            title_fg: str = "black",
            title_font: tuple[str,int,str] = ("Arial", 10,"normal"),
            Padx: int | tuple[int,int] | list[int] = 5,
            Pady: int | tuple[int,int] | list[int] = 5,
            border: int = 0,
            
            exit_default_text:str = "x",
            exit_default_icon: PhotoImage | None = None,
            color_exit_defualt_bg: str = "systembuttonface",
            color_exit_defualt_fg: str = "black",
            color_exit_on_enter_bg: str = "red",
            color_exit_on_enter_fg: str = "white",
            color_exit_on_leave_bg: str = "systembuttonface",
            color_exit_on_leave_fg: str = "black",
            color_exit_on_click_bg: str = "red",
            color_exit_on_click_fg: str = "white",
            
            fullScreen_default_text:str = "⬛",
            fullScreen_default_icon:PhotoImage | None = None,
            color_fullScreen_defualt_bg: str = "systembuttonface",
            color_fullScreen_defualt_fg: str = "black",
            color_fullScreen_on_enter_bg: str = "blue",
            color_fullScreen_on_enter_fg: str = "white",
            color_fullScreen_on_leave_bg: str = "systembuttonface",
            color_fullScreen_on_leave_fg: str = "black",
            color_fullScreen_on_click_bg: str = "blue",
            color_fullScreen_on_click_fg: str = "white",
            
            minimizeScreen_default_text:str = "-",
            minimizeScreen_default_icon:PhotoImage | None = None,
            color_minimizeScreen_defualt_bg: str = "systembuttonface",
            color_minimizeScreen_defualt_fg: str = "black",
            color_minimizeScreen_on_enter_bg: str = "blue",
            color_minimizeScreen_on_enter_fg: str = "white",
            color_minimizeScreen_on_leave_bg: str = "systembuttonface",
            color_minimizeScreen_on_leave_fg: str = "black",
            color_minimizeScreen_on_click_bg: str = "blue",
            color_minimizeScreen_on_click_fg: str = "white",
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
            self.exit_default_text = exit_default_text
            self.color_exit_defualt_bg = color_exit_defualt_bg
            self.color_exit_defualt_fg = color_exit_defualt_fg
            self.color_exit_on_enter_bg = color_exit_on_enter_bg
            self.color_exit_on_enter_fg = color_exit_on_enter_fg
            self.color_exit_on_leave_bg = color_exit_on_leave_bg
            self.color_exit_on_leave_fg = color_exit_on_leave_fg
            self.color_exit_on_click_bg = color_exit_on_click_bg
            self.color_exit_on_click_fg = color_exit_on_click_fg
            
            self.fullScreen_default_text = fullScreen_default_text
            self.fullScreen_default_icon = fullScreen_default_icon
            self.color_fullScreen_defualt_bg = color_fullScreen_defualt_bg
            self.color_fullScreen_defualt_fg = color_fullScreen_defualt_fg
            self.color_fullScreen_on_enter_bg = color_fullScreen_on_enter_bg
            self.color_fullScreen_on_enter_fg = color_fullScreen_on_enter_fg
            self.color_fullScreen_on_leave_bg = color_fullScreen_on_leave_bg
            self.color_fullScreen_on_leave_fg = color_fullScreen_on_leave_fg
            self.color_fullScreen_on_click_bg = color_fullScreen_on_click_bg
            self.color_fullScreen_on_click_fg = color_fullScreen_on_click_fg
            
            self.minimizeScreen_default_text = minimizeScreen_default_text
            self.minimizeScreen_default_icon = minimizeScreen_default_icon
            self.color_minimizeScreen_defualt_bg = color_minimizeScreen_defualt_bg
            self.color_minimizeScreen_defualt_fg = color_minimizeScreen_defualt_fg
            self.color_minimizeScreen_on_enter_bg = color_minimizeScreen_on_enter_bg
            self.color_minimizeScreen_on_enter_fg = color_minimizeScreen_on_enter_fg
            self.color_minimizeScreen_on_leave_bg = color_minimizeScreen_on_leave_bg
            self.color_minimizeScreen_on_leave_fg = color_minimizeScreen_on_leave_fg
            self.color_minimizeScreen_on_click_bg = color_minimizeScreen_on_click_bg
            self.color_minimizeScreen_on_click_fg = color_minimizeScreen_on_click_fg
        
            
            def __move_window(e) -> None:
                self.parent.geometry(f"+{e.x_root}+{e.y_root}")

            def __on_enter(e,widget:str) -> None:
                if widget == "exit":
                    self.exit_button.configure(bg = self.color_exit_on_enter_bg, fg = self.color_exit_on_enter_fg)
                elif widget == "fullScreen":
                    self.fullScreen_button.configure(bg = self.color_fullScreen_on_enter_bg, fg = self.color_fullScreen_on_enter_fg)
                # elif widget == "minimizeScreen":
                    # self.minimizeScreen_button.configure(bg = self.color_minimizeScreen_on_enter_bg, fg = self.color_minimizeScreen_on_enter_fg)

            def __on_leave(e,widget:str) -> None:
                if widget == "exit":
                    self.exit_button.configure(bg = self.color_exit_on_leave_bg, fg = self.color_exit_on_leave_fg)
                elif widget == "fullScreen":
                    self.fullScreen_button.configure(bg = self.color_fullScreen_on_leave_bg, fg = self.color_fullScreen_on_leave_fg)
                # elif widget == "minimizeScreen":
                    # self.minimizeScreen_button.configure(bg = self.color_minimizeScreen_on_leave_bg, fg = self.color_minimizeScreen_on_leave_fg)

            
            def __fullScreen():
                self.parent.overrideredirect(False)
                state = not self.parent.attributes('-fullscreen')
                self.parent.attributes('-fullscreen', state)
                self.parent.overrideredirect(True)
            
            #! fix the error
            # def __minimizeScreen():
            #     self.parent.overrideredirect(False)
            #     self.parent.iconify()
            
            
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
                text=self.exit_default_text,
                image=exit_default_icon,
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
            self.fullScreen_button = Button(
                self.frame,
                text=self.fullScreen_default_text,
                image=self.fullScreen_default_icon,
                bg = self.color_fullScreen_defualt_bg,
                fg = self.color_fullScreen_defualt_fg,
                font = self.title_font,
                command=__fullScreen,
                width=3,
                bd=0,
                cursor="hand2",
                activebackground = self.color_fullScreen_on_click_bg,
                activeforeground = self.color_fullScreen_on_click_fg,
            )
            
            #! erorr: can't minimize
            # self.minimizeScreen_button = Button(
            #     self.frame,
            #     text=self.minimizeScreen_default_text,
            #     image=self.minimizeScreen_default_icon,
            #     bg = self.color_minimizeScreen_defualt_bg,
            #     fg = self.color_minimizeScreen_defualt_fg,
            #     font = self.title_font,
            #     command=__minimizeScreen,
            #     width=3,
            #     bd=0,
            #     cursor="hand2",
            #     activebackground = self.color_minimizeScreen_on_click_bg,
            #     activeforeground = self.color_minimizeScreen_on_click_fg,
            # )
            self.exit_button.pack(side="right")
            self.fullScreen_button.pack(side="right",padx=5)
            # self.minimizeScreen_button.pack(side="right")
            self.exit_button.bind("<Enter>", lambda e :__on_enter(False,"exit"))
            self.fullScreen_button.bind("<Enter>", lambda e :__on_enter(False,"fullScreen"))
            # self.minimizeScreen_button.bind("<Enter>", lambda e :__on_enter(False,"minimizeScreen"))
            
            self.exit_button.bind("<Leave>", lambda e :__on_leave(False,"exit"))
            self.fullScreen_button.bind("<Leave>", lambda e :__on_leave(False,"fullScreen"))
            # self.minimizeScreen_button.bind("<Leave>", lambda e :__on_leave(False,"minimizeScreen"))

            self.frame.bind("<B1-Motion>", __move_window)
            
        def Set_title(self,**kwargs) -> None:
            self.label.configure(**kwargs)
            
        def Set_bg(self,**kwargs) -> None:
            self.frame.configure(**kwargs)
