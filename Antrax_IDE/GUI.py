from ast import mod
from calendar import c
from doctest import master
from math import e
import os
import time

import tkinter as tk

from tkinter import filedialog
from unittest import result
from PIL import Image, ImageTk

from Antrax_compiler import compiler

ruta_base = os.path.dirname(__file__)
ruta_icono = os.path.join(ruta_base, "assets", "Dragon_icon.png")


Font_tuple = ("Monaco Menlo Consolas", 10, "normal")


class App:
    file_name = ""
    extension_file = ""
    path_file = ""

    def __init__(self):
        tk.Tk().withdraw()
        self.path_file = filedialog.askopenfilename(title="Selecciona un archivo")
        base_name = os.path.basename(self.path_file).split(".")
        self.file_name = base_name[0]
        self.extension_file = base_name[1]

    def getContent(self):
        file = open(self.path_file, "r")
        content = file.read()
        file.close()
        return content

    def openFile(self):
        tk.Tk().withdraw()
        self.path_file = filedialog.askopenfilename()
        base_name = os.path.basename(self.path_file).split(".")
        self.file_name = base_name[0]
        self.extension_file = base_name[1]

    def changeFile(self, path):
        tk.Tk().withdraw()
        self.path_file = path
        base_name = os.path.basename(self.path_file).split(".")
        self.file_name = base_name[0]
        self.extension_file = base_name[1]


class MenuBar(tk.Menu):
    def __init__(self, master):
        self.master = master
        super().__init__()
        tk.Menu.__init__(self, master)
        self.configure(background="#151e21", fg="#00c8e0")
        # self.master
        file_menu = tk.Menu(self, tearoff=0, background="#151e21", fg="#00c8e0")
        file_menu.add_command(label="Abrir", command=master.openFile)
        file_menu.add_command(label="Guardar", command=master.saveFile)
        file_menu.add_command(label="Guardar Como", command=master.saveFileAs)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.quit)

        edit_menu = tk.Menu(self, tearoff=0, background="#151e21", fg="#00c8e0")
        edit_menu.add_command(label="Deshacer", command=master.inputTxt.edit_undo)
        edit_menu.add_command(label="Resacer", command=master.inputTxt.edit_redo)

        help_menu = tk.Menu(self, tearoff=0, background="#151e21", fg="#00c8e0")
        help_menu.add_command(label="Informacion", command=master.openInfo)

        execute_nx = tk.Menu(self, tearoff=0, background="#151e21", fg="#00c8e0")

        # add execute nx childs

        execute_nx.add_command(
            label="Con Optimizacion", command=self.execute_nx_with_opt
        )
        execute_nx.add_command(
            label="Sin Optimizacion", command=self.execute_nx_without_opt
        )
        execute_nx.add_command(
            label="Generar .exe", command=self.execute_nx_generate_exe
        )

        execute_ll = tk.Menu(self, tearoff=0, background="#151e21", fg="#00c8e0")

        # add execute ll childs

        execute_ll.add_command(label="Ejecutar", command=self.execute_ll)
        execute_ll.add_command(label="Generar .exe", command=self.execute_ll_generate_exe)

        generate_ll = tk.Menu(self, tearoff=0, background="#151e21", fg="#00c8e0")

        # add generate ll childs
        generate_ll.add_command(
            label="Sin optimizar", command=self.generate_ll_without_opt
        )
        generate_ll.add_command(
            label="Optimizacioon automatica", command=self.generate_ll_with_opt
        )
        generate_ll.add_command(
            label="Optimizacioon manual", command=self.generate_ll_with_manual_opt
        )

        complie_menu = tk.Menu(self, tearoff=0, background="#151e21", fg="#00c8e0")

        complie_menu.add_cascade(
            label="Ejecutar .nx", menu=execute_nx, background="#151e21"
        )
        complie_menu.add_cascade(
            label="Ejecutar .ll", menu=execute_ll, background="#151e21"
        )
        complie_menu.add_cascade(
            label="Generar .ll", menu=generate_ll, background="#151e21"
        )

        self.add_cascade(label="Archivo", menu=file_menu, background="#151e21")
        self.add_cascade(label="Editar", menu=edit_menu, background="#151e21")
        self.add_cascade(label="Compilacion", menu=complie_menu, background="#151e21")
        self.add_cascade(label="Ayuda", menu=help_menu, background="#151e21")

    def log_step(self, message, start_time):
        elapsed = time.time() - start_time
        self.master.write_to_console(f"{message}: {elapsed:.3f} segundos")
        return time.time()

    def execute_nx_with_opt(self):
        try:
            self.master.write_to_console("Ejecutando .nx con optimización")
            t = time.time()

            # Análisis Léxico y Sintáctico
            tree = compiler.Lexical_Syntactic_Analysis(
                self.master.inputTxt.get("1.0", tk.END)
            )
            t = self.log_step("Análisis Léxico y Sintáctico", t)

            # Generación de código intermedio
            module_ir = compiler.Intermediate_Code_Generation(tree)
            t = self.log_step("Generación de Código Intermedio", t)

            # Optimización
            module_ir = compiler.Intermediate_Code_Optimization(module_ir, passes="-O2")
            t = self.log_step("Optimización de Código Intermedio", t)

            # Guardado
            compiler.save_intermediate_code(module_ir, app.file_name)
            t = self.log_step("Guardando Código Intermedio", t)

            # Generación binaria
            compiler.bin_generate(app.file_name, app.file_name)
            t = self.log_step("Generación de Archivo Binario", t)

            # Ejecución
            results = compiler.bin_execute(app.file_name)
            t = self.log_step("Ejecución de Archivo Binario", t)

            # Resultados
            self.master.write_to_console("======================")
            self.master.write_to_console(results.stdout)
            if results.stderr:
                self.master.write_to_console("Error de ejecución: " + results.stderr, "error")
            self.master.write_to_console("Fin de ejecución")
            self.master.write_to_console("======================")

        except Exception as e:
            print('error', e)
            self.master.write_to_console("Error: " + str(e), "error")
            self.master.write_to_console("======================")


    def execute_nx_without_opt(self):
        try:
            self.master.write_to_console("Ejecutando .nx sin optimización")
            t = time.time()

            tree = compiler.Lexical_Syntactic_Analysis(
                self.master.inputTxt.get("1.0", tk.END)
            )
            t = self.log_step("Análisis Léxico y Sintáctico", t)

            module_ir = compiler.Intermediate_Code_Generation(tree)
            t = self.log_step("Generación de Código Intermedio", t)

            compiler.save_intermediate_code(module_ir, app.file_name)
            t = self.log_step("Guardando Código Intermedio", t)

            compiler.bin_generate(app.file_name, app.file_name)
            t = self.log_step("Generación de Archivo Binario", t)

            results = compiler.bin_execute(app.file_name)
            t = self.log_step("Ejecución de Archivo Binario", t)

            self.master.write_to_console("======================")
            self.master.write_to_console(results.stdout)
            if results.stderr:
                self.master.write_to_console("Error de ejecución: " + results.stderr, "error")
            self.master.write_to_console("Fin de ejecución")
            self.master.write_to_console("======================")

        except Exception as e:
            print('error', e)
            self.master.write_to_console("Error: " + str(e), "error")
            self.master.write_to_console("======================")


    def execute_nx_generate_exe(self):
        try:
            self.master.write_to_console("Generando .exe")
            t = time.time()

            tree = compiler.Lexical_Syntactic_Analysis(
                self.master.inputTxt.get("1.0", tk.END)
            )
            t = self.log_step("Análisis Léxico y Sintáctico", t)

            module_ir = compiler.Intermediate_Code_Generation(tree)
            t = self.log_step("Generación de Código Intermedio", t)

            module_ir = compiler.Intermediate_Code_Optimization(module_ir, passes="-O2")
            t = self.log_step("Optimización de Código Intermedio", t)

            compiler.save_intermediate_code(module_ir, app.file_name)
            t = self.log_step("Guardando Código Intermedio", t)

            compiler.generate_exe(app.file_name, app.file_name)
            t = self.log_step("Generación de Archivo .exe", t)

            self.master.write_to_console(f"Archivo .exe generado en ./exe/{app.file_name}.exe")
            self.master.write_to_console("======================")

        except Exception as e:
            print('error', e)
            self.master.write_to_console("Error: " + str(e), "error")
            self.master.write_to_console("======================")


    def execute_ll(self):
        try:

            start_time = time.time()
            module_ir = self.master.inputTxt.get("1.0", tk.END)
            compiler.save_intermediate_code(module_ir, app.file_name)
            self.master.write_to_console(
                "Guardando codigo intermedio" + str(time.time() - start_time) + " segundos"
            )

            compiler.bin_generate(app.file_name, app.file_name)
            self.master.write_to_console(
                "Generando archivo Binario" + str(time.time() - start_time) + " segundos"
            )

            results = compiler.bin_execute(app.file_name)
            self.master.write_to_console(
                "Ejecutando archivo Binario" + str(time.time() - start_time) + " segundos"
            )

            self.master.write_to_console("======================")
            self.master.write_to_console(results.stdout)
            if results.stderr:
                self.master.write_to_console(
                    "Error de ejecucion: " + results.stderr,"error"
                )
            self.master.write_to_console("fin de ejecucion" + str(time.time() - start_time) + " segundos")
            self.master.write_to_console("======================")
        except Exception as e:
            print('error',e)
            self.master.write_to_console(
                "Error: " + str(e), "error"
            )
            self.master.write_to_console("======================")

    def execute_ll_generate_exe(self):
        try:
            start_time = time.time()
            module_ir = self.master.inputTxt.get("1.0", tk.END)
            compiler.save_intermediate_code(module_ir, app.file_name)
            self.master.write_to_console(
                "Guardando codigo intermedio" + str(time.time() - start_time) + " segundos"
            )

            compiler.generate_exe(app.file_name, app.file_name)
            self.master.write_to_console(
                "Generando archivo .exe" + str(time.time() - start_time) + " segundos"
            )

            self.master.write_to_console(
                "archivo .exe generado en ./exe/" + app.file_name + ".exe"
            )
            self.master.write_to_console("======================") 
        except Exception as e:
            print('error',e)
            self.master.write_to_console(
                "Error: " + str(e), "error"
            )
            self.master.write_to_console("======================")


    def generate_ll_without_opt(self):
        try:
            self.master.write_to_console("Generando .ll sin optimización")
            total_start = time.time()

            start = time.time()
            tree = compiler.Lexical_Syntactic_Analysis(self.master.inputTxt.get("1.0", tk.END))
            self.master.write_to_console(f"Análisis Léxico y Sintáctico: {time.time() - start:.3f} segundos")

            start = time.time()
            module_ir = compiler.Intermediate_Code_Generation(tree)
            self.master.write_to_console(f"Generación de código intermedio: {time.time() - start:.3f} segundos")

            start = time.time()
            compiler.save_intermediate_code(module_ir, app.file_name)
            self.master.write_to_console(f"Guardando código intermedio: {time.time() - start:.3f} segundos")

            self.master.changeFile(f"./ll/{app.file_name}.ll")
            self.master.write_to_console(f"Archivo .ll generado en ./ll/{app.file_name}.ll")
            self.master.write_to_console(f"Tiempo total: {time.time() - total_start:.3f} segundos")
            self.master.write_to_console("======================")

        except Exception as e:
            print("error", e)
            self.master.write_to_console("Error: " + str(e), "error")
            self.master.write_to_console("======================")

    def generate_ll_with_opt(self):
        try:
            self.master.write_to_console("Generando .ll con optimización")
            total_start = time.time()

            start = time.time()
            tree = compiler.Lexical_Syntactic_Analysis(self.master.inputTxt.get("1.0", tk.END))
            self.master.write_to_console(f"Análisis Léxico y Sintáctico: {time.time() - start:.3f} segundos")

            start = time.time()
            module_ir = compiler.Intermediate_Code_Generation(tree)
            self.master.write_to_console(f"Generación de código intermedio: {time.time() - start:.3f} segundos")

            start = time.time()
            module_ir = compiler.Intermediate_Code_Optimization(module_ir, passes="-O2")
            self.master.write_to_console(f"Optimización: {time.time() - start:.3f} segundos")

            start = time.time()
            compiler.save_intermediate_code(module_ir, app.file_name)
            self.master.write_to_console(f"Guardando código intermedio: {time.time() - start:.3f} segundos")

            self.master.changeFile(f"./ll/{app.file_name}.ll")
            self.master.write_to_console(f"Archivo .ll generado en ./ll/{app.file_name}.ll")
            self.master.write_to_console(f"Tiempo total: {time.time() - total_start:.3f} segundos")
            self.master.write_to_console("======================")

        except Exception as e:
            print("error", e)
            self.master.write_to_console("Error: " + str(e), "error")
            self.master.write_to_console("======================")

    def generate_ll_with_manual_opt(self):
        try:
            self.master.write_to_console("Generando .ll con optimización manual")
            total_start = time.time()

            start = time.time()
            tree = compiler.Lexical_Syntactic_Analysis(self.master.inputTxt.get("1.0", tk.END))
            self.master.write_to_console(f"Análisis Léxico y Sintáctico: {time.time() - start:.3f} segundos")

            start = time.time()
            module_ir = compiler.Intermediate_Code_Generation(tree)
            self.master.write_to_console(f"Generación de código intermedio: {time.time() - start:.3f} segundos")

            start = time.time()
            module_ir = compiler.Intermediate_Code_Optimization(module_ir, passes="-O2")
            self.master.write_to_console(f"Optimización manual: {time.time() - start:.3f} segundos")

            start = time.time()
            compiler.save_intermediate_code(module_ir, app.file_name)
            self.master.write_to_console(f"Guardando código intermedio: {time.time() - start:.3f} segundos")

            self.master.changeFile(f"./ll/{app.file_name}.ll")
            self.master.write_to_console(f"Archivo .ll generado en ./ll/{app.file_name}.ll")
            self.master.write_to_console(f"Tiempo total: {time.time() - total_start:.3f} segundos")
            self.master.write_to_console("======================")

        except Exception as e:
            print("error", e)
            self.master.write_to_console("Error: " + str(e), "error")
            self.master.write_to_console("======================")

class PopupWindowConfirmation:
    def __init__(self, parent):
        self.parent = parent
        self.gui = tk.Toplevel(self.parent)
        self.gui.resizable(False, False)
        self.gui.title("Antrax IDE")
        self.parent.update_idletasks()
        width = 500
        height = 200
        x = (self.parent.winfo_screenwidth() // 4) - (width // 4)
        y = (self.parent.winfo_screenheight() // 4) - (height // 4)
        self.gui.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.gui.wait_visibility()

        self.header = tk.Frame(self.gui, bg="#151e21", width=500, height=100)
        self.header.grid(row=0, column=0, sticky="NW")
        self.header.grid_propagate(0)
        self.header.update()
        self.title = tk.Label(
            self.header,
            text="No has guardado el archivo, que deseas hacer?",
            background="#151e21",
            fg="#00c8e0",
        )
        self.title.place(
            x=250,
            y=50,
            anchor="center",
        )

        self.body = tk.Frame(self.gui, bg="#151e21", width=500, height=100)
        self.body.grid(row=1, column=0, sticky="NW")
        self.body.grid_propagate(0)
        self.body.update()

        self.buttonCancel = tk.Button(
            self.body,
            text="Cancelar",
            background="#151e21",
            fg="#00c8e0",
            command=self.cancel,
        )
        self.buttonCancel.place(x=25, y=50, anchor="w")
        self.buttonSave = tk.Button(
            self.body,
            text="Guardar",
            background="#151e21",
            fg="#00c8e0",
            command=self.save,
        )
        self.buttonSave.place(x=275, y=50, anchor="w")
        self.buttonNotSave = tk.Button(
            self.body,
            text="No Guardar",
            background="#151e21",
            fg="#00c8e0",
            command=self.notSave,
        )
        self.buttonNotSave.place(x=375, y=50, anchor="w")

    def cancel(self):
        self.gui.destroy()

    def save(self):
        self.gui.destroy()
        self.parent.saveFile()
        app.openFile()
        self.parent.title(app.file_name)
        self.parent.path["text"] = app.path_file
        self.parent.inputTxt.delete("1.0", tk.END)
        self.parent.inputTxt.insert("1.0", app.getContent())
        self.parent.inputTxt.edit_reset()
        return 0

    def notSave(self):
        self.gui.destroy()
        app.openFile()
        self.parent.title(app.file_name)
        self.parent.path["text"] = app.path_file
        self.parent.inputTxt.delete("1.0", tk.END)
        self.parent.inputTxt.insert("1.0", app.getContent())
        self.parent.inputTxt.edit_reset()
        return


class PopupWindowInfo:
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.gui = tk.Toplevel(self.parent, background="#151e21")
        self.gui.resizable(False, False)
        self.gui.title("Antrax IDE")
        self.parent.update_idletasks()
        width = 600
        height = 200
        x = (self.parent.winfo_screenwidth() // 4) - (width // 4)
        y = (self.parent.winfo_screenheight() // 4) - (height // 4)
        self.gui.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.gui.wait_visibility()

        self.image = tk.Frame(self.gui, bg="#151e21", width=250, height=200)
        self.image.grid(row=0, column=0, sticky="NW")
        self.image.grid_propagate(0)
        self.image.update()

        img = ImageTk.PhotoImage(Image.open(ruta_icono).resize((250, 200)))

        label = tk.Label(self.image, image=img, background="#151e21")
        label.image = img
        label.pack()
        self.Content = tk.Frame(self.gui, bg="#151e21", width=300, height=200)
        self.Content.grid(row=0, column=1, sticky="NW")
        self.Content.grid_propagate(0)
        self.Content.update()

        tk.Label(
            self.Content,
            text="Antrax IDE",
            fg="light green",
            bg="#151e21",
            font="Helvetica 16 bold italic",
        ).pack()
        tk.Label(
            self.Content,
            text="Este programa se distribuye con la esperanza de que sea útilpara modificar y crear archivos de Texto. de mas misma manera intuitivo de usar.",
            fg="#00c8e0",
            bg="#151e21",
            wraplength=300,
            anchor="w",
        ).pack(fill="both")

        tk.Label(
            self.Content,
            text="Antrax IDE es software libre: puede redistribuirlo y/o modificarlo bajo los términos de la Licencia Pública General",
            fg="#00c8e0",
            bg="#151e21",
            wraplength=300,
            anchor="w",
        ).pack(fill="both")


class Window(tk.Toplevel):
    pending_save = False

    def __init__(self):
        super().__init__()

        self.geometry("800x600+100+100")
        self.configure(background="#151e21")
        self.title("Artrax File")
        img = tk.Image("photo", file=ruta_icono)
        self.tk.call("wm", "iconphoto", self._w, img)
        self.path = tk.Label(
            self, text=app.path_file, background="#151e21", fg="#00c8e0"
        )
        self.path.pack(side=tk.TOP, padx=5, pady=5)

        # Frame principal para organizar los dos widgets de texto
        main_frame = tk.Frame(self, background="#151e21")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Editor de texto principal (input)
        self.inputTxt = tk.Text(
            main_frame,
            relief=tk.RAISED,
            borderwidth=1,
            background="#151e21",
            fg="#00c8e0",
            font=Font_tuple,
            insertbackground="#00c8e0",
            undo=True,
            maxundo=-2,
        )
        self.inputTxt.pack(fill=tk.BOTH, expand=True)

        # Separador visual
        separator = tk.Frame(
            main_frame, height=2, bd=1, relief=tk.SUNKEN, background="#00c8e0"
        )
        separator.pack(fill=tk.X, pady=5)

        # Consola de salida
        self.consoleOutput = tk.Text(
            main_frame,
            relief=tk.RAISED,
            borderwidth=1,
            background="#151e21",
            fg="#00c8e0",
            font=Font_tuple,
            height=1010,
            state="disabled",
        )
        self.consoleOutput.pack(fill=tk.BOTH, expand=True)

        # Opcional: Configurar tags para diferentes tipos de mensajes en la consola
        self.consoleOutput.tag_config("error", foreground="#ff5555")
        self.consoleOutput.tag_config("success", foreground="#55ff55")
        self.consoleOutput.tag_config("info", foreground="#00c8e0")

        def OnKeyPress(e):
            self.pending_save = True

        self.inputTxt.bind("<KeyPress>", OnKeyPress)
        self.inputTxt.insert("1.0", app.getContent())
        self.inputTxt.edit_reset()
        self.inputTxt.pack(fill="both", expand=True, padx=25, pady=25)
        self.config(menu=MenuBar(self))
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.mainloop()

    def openFile(self):
        if self.pending_save:
            window = PopupWindowConfirmation(self)
        else:
            app.openFile()
            self.title(app.file_name)
            self.path["text"] = app.path_file
            self.inputTxt.delete("1.0", tk.END)
            self.inputTxt.insert("1.0", app.getContent())
            self.inputTxt.edit_reset()

    def changeFile(self, path):
        if self.pending_save:
            window = PopupWindowConfirmation(self)
        else:
            app.changeFile(path)
            self.title(app.file_name)
            self.path["text"] = app.path_file
            self.inputTxt.delete("1.0", tk.END)
            self.inputTxt.insert("1.0", app.getContent())
            self.inputTxt.edit_reset()

    def saveFile(self):
        content = self.inputTxt.get("1.0", tk.END)
        file = open(app.path_file, "w")
        file.write(content)
        file.close
        self.inputTxt.edit_reset()
        self.pending_save = False

    def saveFileAs(self):
        tk.Tk().withdraw()
        path_file = filedialog.asksaveasfilename()
        content = self.inputTxt.get("1.0", tk.END)
        file = open(path_file, "w")
        file.write(content)
        file.close
        self.inputTxt.edit_reset()
        self.pending_save = False

    def openInfo(self):
        PopupWindowInfo(self)

    def write_to_console(self, message, tag=None):
        """Escribe un mensaje en la consola de salida."""
        self.consoleOutput.config(state="normal")
        if tag:
            self.consoleOutput.insert(tk.END, message + "\n", tag)
        else:
            self.consoleOutput.insert(tk.END, message + "\n")
        self.consoleOutput.config(state="disabled")
        self.consoleOutput.see(tk.END)

    def on_close(self):
        import os
        import sys

        self.destroy()
        self.quit()
        os._exit(0)

    def write_to_console(self, text, message_type="info"):
        self.consoleOutput.config(state="normal")
        self.consoleOutput.insert(tk.END, text + "\n", message_type)
        self.consoleOutput.see(tk.END)  # Auto-scroll al final
        self.consoleOutput.config(
            state="disabled"
        )  # Opcional para hacerla de solo lectura


app = App()
root = Window()
