import argparse
import subprocess
from pathlib import Path
import re

from antlr4 import *
from antlr4_data.ValidationListener import ValidationListener
from antlr4_data.AntraxIRVisitor import AntraxIRVisitor

from antlr4_data.AntraxLexer import AntraxLexer
from antlr4_data.AntraxParser import AntraxParser
from antlr4_data.AntraxBaseVisitor import AntraxBaseVisitor


from llvmlite import binding
import ctypes


def validate_file(path: Path):
    """Valida si el archivo existe y tiene extensión .nx"""
    if not path.suffix == ".nx":
        raise ValueError("Error: El archivo debe tener extensión .nx")

    if not path.is_file():
        raise FileNotFoundError(f"Error: El archivo '{path}' no existe.")


def read_code(path: Path):
    """Lee el código fuente del archivo y lo devuelve como string"""
    try:
        with path.open("r", encoding="utf-8") as file:
            return file.read()
    except OSError as e:
        raise ValueError(f"Error al leer el archivo: {e}")


def Lexical_Syntactic_Analysis(source_code):
    """Realiza el análisis léxico y sintáctico del código fuente"""
    print("Realizando análisis léxico y sintáctico...")
    lexer = AntraxLexer(InputStream(source_code))
    stream = CommonTokenStream(lexer)
    parser = AntraxParser(stream)
    tree = parser.root()

    # Imprimir el árbol sintáctico
    # print("Árbol sintáctico:")
    # print(tree.toStringTree(recog=parser.ruleNames))

    return tree


def Intermediate_Code_Generation(tree):
    """Genera el código intermedio a partir del árbol sintáctico"""
    print("Generando código intermedio...")
    visitor = AntraxIRVisitor()
    module_ir = visitor.visit(tree)

    return module_ir


def Intermediate_Code_Optimization(module_ir, passes="-O2"):
    """Optimiza el código intermedio"""
    input_path = "./ll/temp.ll"
    output_path = "./ll/optimized.ll"

    with open(input_path, "w") as f:
        f.write(str(module_ir))

    subprocess.run(["opt", "-S", passes, input_path, "-o", output_path])

    with open(output_path, "r") as f:
        optimized_ir = f.read()
    return optimized_ir


def save_intermediate_code(module_ir, output_path):
    """Guarda el código intermedio en un archivo"""
    print("Guardando código intermedio...")
    with open("./ll/" + output_path + ".ll", "w") as f:
        f.write(str(module_ir))


def bin_generate(input_file, output_file):
    """Genera el código binario a partir del código intermedio"""
    print("Generando código binario...")

    subprocess.run(
        ["clang", "-o", "./bin/" + output_file, "./ll/" + input_file + ".ll"],
        check=True,
    )


def bin_execute(binary_path):
    """Ejecuta el código binario generado"""
    print("Ejecutando código binario...")
    result = subprocess.run(
        ["./bin/" + binary_path],  # Comando a ejecutar
        capture_output=True,  # Capturar stdout y stderr
        text=True,  # Decodificar la salida como texto
    )

    return result


def generate_exe(input_file, output_file):
    """Genera el código binario a partir del código intermedio"""
    print("Generando archivo .exe ...")

    subprocess.run(
        [
            "llc",
            "-filetype=obj",
            "-mtriple=x86_64-pc-windows-gnu",
            "./ll/" + input_file + ".ll",
            "-o",
            "./obj/" + input_file + ".obj",
        ],
        check=True,
    )

    subprocess.run(
        [
            "x86_64-w64-mingw32-gcc",
            "-o",
            "./exe/" + output_file + ".exe",
            "./obj/" + input_file + ".obj",
        ],
        check=True,
    )


def visit_tree(source_code):
    """Ejecuta el código fuente"""
    lexer = AntraxLexer(InputStream(source_code))
    stream = CommonTokenStream(lexer)
    parser = AntraxParser(stream)
    tree = parser.root()

    walker = ParseTreeWalker()
    my_listener = ValidationListener()
    walker.walk(my_listener, tree)

    visitor = AntraxBaseVisitor()
    visitor.visit(tree)


def generate_llvm_ir(source_code, output_path):
    """Genera el código LLVM IR y lo guarda en un archivo"""

    tree = Lexical_Syntactic_Analysis(source_code)

    visitor = AntraxIRVisitor()
    module_ir = visitor.visit(tree)

    # Guardar el módulo IR en un archivo
    with open(output_path, "w") as f:
        f.write(str(module_ir))
    print(f"Archivo LLVM IR guardado en: {output_path}")


def generate_bin(path):
    """Genera el código LLVM IR y lo guarda en un archivo"""
    source_code = read_code(path)

    tree = Lexical_Syntactic_Analysis(source_code)
    module_ir = Intermediate_Code_Generation(tree)
    print(module_ir)

    bin_generate(module_ir)


def execute(source_code):
    """Ejecuta el código fuente"""
    lexer = AntraxLexer(InputStream(source_code))
    stream = CommonTokenStream(lexer)
    parser = AntraxParser(stream)
    tree = parser.root()

    visitor = AntraxIRVisitor()
    module_ir = visitor.visit(tree)

    # Inicializar LLVM
    binding.initialize()
    binding.initialize_native_target()
    binding.initialize_native_asmprinter()

    # Crear el motor JIT
    target = binding.Target.from_default_triple()
    target_machine = target.create_target_machine()
    backing_mod = binding.parse_assembly(str(module_ir))
    backing_mod.verify()
    engine = binding.create_mcjit_compiler(backing_mod, target_machine)

    # Obtener la función 'main' y ejecutarla
    main_func = engine.get_function_address("main")
    main = ctypes.CFUNCTYPE(ctypes.c_int)(main_func)
    main()  # Ejecutar la función main


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Verifica si un archivo con extensión .nx existe en la ruta proporcionada."
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Comando para recorrer el árbol
    visit_parser = subparsers.add_parser(
        "visit", help="Recorre el árbol sintáctico con un visitor en python"
    )
    visit_parser.add_argument("nx", type=Path, help="Ruta del archivo nx")

    # Comando para generar LLVM IR y guardarlo
    llvm_parser = subparsers.add_parser(
        "llvm", help="Genera el árbol en LLVM IR y guarda en un archivo .ll"
    )
    llvm_parser.add_argument("nx", type=Path, help="Ruta del archivo nx")
    llvm_parser.add_argument("output", type=Path, help="Archivo de salida .ll")

    # Comando para generar y ejecutar
    exec_parser = subparsers.add_parser("exec", help="Genera el árbol y lo ejecuta")
    exec_parser.add_argument("nx", type=Path, help="Ruta del archivo nx")

    args = parser.parse_args()
    validate_file(args.nx)
    source_code = read_code(args.nx)

    # Ejecutar la opción elegida
    if args.command == "visit":
        visit_tree(source_code)
    elif args.command == "llvm":
        generate_llvm_ir(source_code, args.output)
    elif args.command == "exec":
        execute(source_code)
    elif args.command == "bin":
        generate_bin(source_code, args.output)
