import os
import io
import csv
# import cv2
import json
# import rembg #! can't import because it's not suported in python3.12
import pandas as pd
from tkinter import Tk, Frame, mainloop, PhotoImage, END, ttk , filedialog
from customtkinter import CTkFont, CTkTextbox
from PIL import Image, ImageTk


class File_Handler:
    """initializer

    -----
    an easy and short way to deal with files\n

    Get_file_path()
    -----
            Get the path of a file with filedaialog without importing any thing

    -----
    Edit_Text_File()
    -----
            opening the file in a built in Text Editor
            make sure that the file is `.txt`\n
            otherwise it might looks ugly\n
            `filename` the path of the file to Edit, you can get it from
            `Get_file_path()` easily

    -----
    Get_contents_from_json()
    -----
            Get the contents of a `JSON` file

    -----
    Get_csv_content_as_list()
    -----
            Get the contents of a `CSV` file as a `list` of `dict`

    -----
    Get_csv_content_as_table()
    -----
            Get the contents of a `CSV` file as a table

    -----
    Get_text_from_txt()
    -----
            Get the contents of a `txt` file

    -----
    Add_to_JSON_file()
    -----
            adding some data to `JSON` file

    -----
    Add_to_txt_file()
    -----
            adding some data to `txt` file\n
            `replace: bool` if replace then replace all the content of `txt` file and add the new text

    -----
    bg_remover()
    -----
            removing the Background of the image

    -----
    local_sql()
    -----
            creating a local sql
    """

    def __init__(self):
        self.__content: str
        self.__file: str
        self._Version = "Version: 1.5"
        self._Publisher = "NooR MaseR"
    
    def Get_file_path(self) -> str:  # type: ignore
        "Get the file path"
        global file
        file = filedialog.askopenfilename(title="Pick a file", filetypes=[
                                                                        ("All files", "*.*"),
                                                                        ("Text file", "*.txt"),
                                                                        ("JSON file", "*.json"),
                                                                        ("CSV files", "*.csv"),
                                                                        ("Excel files", "*.xlsx"),
                                                                        ("PNG files", "*.png"),
                                                                        ("jpeg files", "*.jpeg"),
                                                                        ("jpg files", "*.jpg"),
                                                                        ],
                                        )
        if file:
            self.__file = file
            return f"{file}"

    class ask_to_save_as:
        "Get the path for saving the file"
        
        def __str__(self) -> str:
            return self.__file
        
        def __init__(self,content: str) -> None: 
            assert content, "content can not be empty"
            self.__content = content
            self.__file = filedialog.SaveAs(defaultextension=".*txt", filetypes=[
                                                                                ("Text file", "*.txt"),
                                                                                ("JSON file", "*.json"),
                                                                                ("CSV files", "*.csv"),
                                                                                ("Excel files", "*.xlsx"),
                                                                                ("PNG files", "*.png"),
                                                                                ("jpeg files", "*.jpeg"),
                                                                                ("jpg files", "*.jpg"),
                                                                                ("All files", "*.*"),
                                                                                ]
                                            ).show()
            
        def Save(self) -> None:
            with io.open(self.__file,"w") as f:
                f.write(self.__content)
                f.close()
                
    def remove_file(self,path: str) -> None :
        os.remove(path)

    def Edit_Text_File(self, filename: str):
        """
        opening the file in a built in Text Editor
        make sure that the file is `.txt`\n
        otherwise it might looks ugly\n
        ----
        `filename: str` the path of the file to Edit, you can get it from `Get_file()` easily
        """

        def Save(text):
            with io.open(self.__file, "w") as f:
                f.write(text)
            quit()

        if filename.endswith(".txt"):
            with io.open(filename, "r") as f:
                self.__content = f.read()
            app = Tk()
            app.geometry("600x500")
            app.title("Text Editor")

            fonte = CTkFont(family="Arial", size=18)

            textframe = ttk.Frame(app)
            textframe.pack(fill="both", expand=1)
            text_box = CTkTextbox(textframe, font=fonte, undo=True, corner_radius=0)
            text_box.insert("end", self.__content)
            text_box.pack(fill="both", expand=1)

            buttons_frame = Frame(app, height=30)
            buttons_frame.pack(fill="x")
            cancel_button = ttk.Button(buttons_frame, text="Cancel", command=quit)
            cancel_button.place(x=5)
            save_button = ttk.Button(
                buttons_frame,
                text="Save",
                command=lambda: Save(text_box.get("1.0", END)),
            )
            save_button.place(x=125)
            mainloop()
        else:
            raise TypeError("file extention is not txt")

    def Get_contents_from_json(self, file_path: str) -> dict:
        "Get the contents of a `JSON` file"
        if file_path.endswith(".json"):
            with io.open(file_path, "r") as f:
                self.__content = json.load(f)
            return self.__content
        else:
            raise TypeError("this is not a json file!!!!!!!!!!!!!!!")

    def Get_csv_content_as_list(self, file_path: str) -> list:
        "Get the contents of a `CSV` file as a `list` of `dict`"
        if file_path.endswith(".csv"):
            with io.open(file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                items = list(reader)
            return items
        else:
            raise TypeError("this is not a csv file!!!!!!!!!!!!!!!")

    def Get_csv_content_as_table(self, file_path: str) -> pd.DataFrame:
        """
        Get the contents of a `CSV` file as a table\n
        >>> csv_file = File_Handler()
        >>> file = csv_file.Get_file_path()
        >>> content = csv_file.Get_csv_content_as_table(file)
        >>> print(content)\n
        ---
        you can rename any row using `rename()`
        >>> renamed_row = content.rename(columns= {"row to replace":"replace with"})
        >>> print(renamed_raw)\n
        ---
        you can get any raw by slicing it\n
        for examble
        >>> print(renamed_raw['Email'])

        """
        if file_path.endswith(".csv"):
            reader = pd.read_csv(file_path, encoding="utf-8")
            return reader
        else:
            raise TypeError("this is not a csv file!!!!!!!!!!!!!!!")

    def Get_web_csv_file(self, url: str, encoding: str = "utf-8") -> pd.DataFrame:
        """
        Get the contents of a `CSV` file from internet\n
        >>> db = File_Handler()
        >>> content = db.Get_web_csv_file(file)
        >>> print(content)\n
        ---
        you can rename any row using `rename()`
        >>> renamed_row = content.rename(columns= {"row to replace":"replace with"})
        >>> print(renamed_raw)\n
        ---
        you can get any raw by slicing it\n
        for examble
        >>> print(renamed_raw['ID'])
        """
        try:
            reader = pd.read_csv(url, encoding=encoding)
            return reader
        except:
            raise Exception("failed to get the csv file online")

    def Get_tables_from_web(
        self, url: str, encode: str | None = None
    ) -> list[pd.DataFrame] | str:
        "Get the tables or csv files online"
        if url:
            try:
                reader = pd.read_html(url, encoding=encode)
                if reader:
                    return reader
                else:
                    return f"No Tables has been Found in {url}"
            except:
                raise TypeError(
                    "This url is Not currect please make sure to copy the same url that contain the tables."
                )
        else:
            raise Exception("url cannot be empty!!!!!")

    def Get_excel_content(self, file_path: str) -> pd.DataFrame:
        """Get the contents of `Excel` file\n
        >>> db = File_Handler()
        >>> file = db.Get_file_path()
        >>> content = db.Get_excel_content(file)
        >>> print(content)\n
        ---
        you can rename any row using `rename()`
        >>> renamed_row = content.rename(columns= {"row to replace":"replace with"})
        >>> print(renamed_raw)\n
        ---
        you can get any raw by slicing it\n
        for examble
        >>> print(renamed_raw['ID'])
        """
        if file_path.endswith(".xlsx" or "xls"):
            reader = pd.read_excel(file_path)
            return reader
        else:
            raise TypeError("this is not a Excel file!!!!!!!!!!!!!!!")

    def Get_text_from_txt(self, file_path: str) -> str:
        "Get the contents of a `txt` file"
        if file_path.endswith(".txt"):
            with io.open(file_path, "r") as f:
                self.__content = f.read()
            return self.__content
        else:
            raise TypeError("this is not a text file!!!!!!!!!!!!!!!")

    def Add_to_JSON_file(
        self, filename: str, text: str | int | float, indentation: int = 4
    ):
        """adding some data to `JSON` file

        >>> edit = File_Handler()
        >>> text = edit.Get_contents_from_json('path/to/json/file')
        >>> text["Key"] = "value"
        >>> edit.Add_to_JSON_file(file, text)

        """
        assert indentation >= 0, "can not add negative indentation"
        if filename.endswith(".json"):
            with io.open(filename, "w") as f:
                json.dump(text, f, indent=indentation)
        else:
            raise TypeError("this is not a json file !!!!!!!!!!!!!!!")

    def Add_to_txt_file(self, file_path: str, text_to_add: str, replace: bool = True):
        """
        adding some data to `txt` file\n
        `replace: bool` if replace then replace all the content of `txt` file and add the new text
        """
        if file_path.endswith(".text"):
            if replace:
                with io.open(file_path, "w") as f:
                    f.write(text_to_add)
            else:
                with io.open(file_path, "a") as f:
                    f.write(text_to_add)
        else:
            raise TypeError("this is not a text file !!!!!!!!!!!!!!!")

#? ==========================SOON==========================
# class bg_remover:
#     """
#     removes the Background from the image\n
#     `image_path` the path to the image to remove\n
#     `image_output_path` the path followed by the file name without Extention for saving

#     -----
#     Examble
#     -----
#             >>> from TOOLS.File_Handler import bg_remover
#                 path = 'path/to/image'
#                 image_remover = bg_remover(image_path = path, image_output_path = "path/for/saving/removed/image/image name")\n
#                 if you want to return the image as PIL you can use `return_image_as_pil()`\n
#                 >>> photo = image_remover.return_image_as_pil()\n
#                 if you want the path of the output or input you can use:
#                 >>> print(image_remover._image_output_path)
#                 >>> print(image_remover._image_output_name)
#                 >>> print(image_remover._image_path)
#     """

#     def __init__(self, image_path: str, image_output_path: str) -> None:
#         self._image_path = image_path
#         self._image_output_path = image_output_path + ".png"
#         self._image_types: tuple = (
#             ".jpg",
#             ".jpeg",
#             ".png",
#             ".gif",
#             ".bmp",
#             ".tif",
#             ".tiff",
#         )
#         _, extention = os.path.splitext(image_path)
#         if extention in self._image_types:
#             photo = cv2.imread(self._image_path)
#             print("Please wait while removing the Background")
#             self.__removed = rembg.remove(photo)
#             cv2.imwrite(self._image_output_path, self.__removed)  # type: ignore
#         else:
#             raise TypeError(
#                 f"Extention {extention} is unrecognized, this is not an image"
#             )

#     def return_image_as_pil(self, size: tuple[int, int] = (200, 200)) -> PhotoImage:
#         "return the removed image as PIL for UI like for using it on tkinter"
#         return ImageTk.PhotoImage(Image.open(self._image_output_path).resize(size))  # type: ignore



