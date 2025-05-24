# Compilador Antrax - README

## ✨ Descripción general

**Antrax** es un compilador desarrollado con **ANTLR**, **Clang** y **LLVM Lite**, capaz de traducir código fuente personalizado (.nx) a **LLVM IR** y binarios ejecutables. El proyecto ofrece una cadena de herramientas completa, desde el análisis sintáctico hasta la generación de código, así como un entorno de desarrollo integrado (IDE).

---

## 📂 Estructura del proyecto

```
antlr4_data/            # Gramática ANTLR y archivos generados
├── Antrax.g4           # Definición de gramática principal
├── AntraxLexer.py      # Analizador léxico generado
├── AntraxParser.py     # Analizador sintáctico generado
├── AntraxIRVisitor.py  # Visitante personalizado para generación de IR
└── ...                 # Otros archivos auxiliares generados por ANTLR

Antrax_compiler/        # Componentes del compilador
└── compiler.py         # Lógica principal del compilador

Antrax_IDE/             # IDE gráfico
├── GUI.py              # Interfaz gráfica
└── assets/             # Recursos visuales del IDE (iconos, etc.)

bin/                    # Binarios generados
exe/                    # Ejecutables para Windows
ll/                     # Archivos intermedios LLVM IR
nx/                     # Archivos de ejemplo (.nx)
obj/                    # Archivos objeto intermedios

main.py                 # Punto de entrada del compilador
```

---

## 🌟 Características principales

* **Análisis léxico/sintáctico**: Frontend basado en ANTLR.
* **Generación de IR**: Utiliza LLVM Lite para representar el código.
* **Optimización**: Soporte de pases de optimización con LLVM.
* **Generación de código**: Producción de LLVM IR, objetos y ejecutables.
* **IDE integrado**: Interfaz gráfica con resaltado de sintaxis y controles de compilación.

---

## 📊 Dependencias

* Python 3.9+
* ANTLR 4
* LLVM (con bindings para Python)
* Clang
* LLVM Lite

### Paquetes de Python

```bash
pip install antlr4-python3-runtime llvmlite
```

### Dependencias del sistema (Linux/Unix)

```bash
sudo apt-get install llvm clang x86_64-w64-mingw32-gcc
```

---

## ⚙️ Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/usuario/antrax-compiler.git
cd antrax-compiler
```

2. Instala las dependencias necesarias.

---

## 💻 Uso

### 📥 Línea de comandos

```bash
python main.py [comando] [opciones]
```

Opciones disponibles:

* `-o salida` - Especifica el nombre del archivo de salida.
* `-emit-llvm` - Genera solo el IR de LLVM.
* `-optimize` - Aplica optimizaciones.

### 📽️ IDE

Ejecuta la interfaz gráfica:

```bash
python Antrax_IDE/GUI.py
```

---

## 📒 Ejemplos

* Archivos de entrada .nx disponibles en el directorio `nx/`
* Salidas IR generadas en `ll/`

---

## ⚒️ Proceso de compilación

1. **Análisis léxico/sintáctico**:

```python
lexer = AntraxLexer(InputStream(source_code))
stream = CommonTokenStream(lexer)
parser = AntraxParser(stream)
tree = parser.root()
```

2. **Generación de IR**:

```python
visitor = AntraxIRVisitor()
module_ir = visitor.visit(tree)
```

3. **Optimización**:

```bash
opt -S -O2 input.ll -o optimized.ll
```

4. **Generación de binarios**:

#### Linux:

```bash
clang -o salida input.ll
```

#### Windows:

```bash
llc -filetype=obj -mtriple=x86_64-pc-windows-gnu input.ll
x86_64-w64-mingw32-gcc -o salida.exe input.obj
```

---

## 🔧 Comandos disponibles

```bash
python main.py visit archivo.nx          # Analiza el árbol de derivación
python main.py llvm archivo.nx salida.ll # Genera LLVM IR
python main.py exec archivo.nx           # Ejecuta el código directamente
python main.py bin archivo.nx salida     # Genera binario ejecutable
```

---

## 🔄 Ejemplo completo de flujo

```bash
# Generar IR\python main.py llvm nx/test1.nx output.ll

# Optimizar IR
opt -S -O2 output.ll -o optimized.ll

# Ejecutable en Linux
clang optimized.ll -o programa

# Ejecutable en Windows
llc -filetype=obj -mtriple=x86_64-pc-windows-gnu optimized.ll
x86_64-w64-mingw32-gcc optimized.obj -o programa.exe
```

---




