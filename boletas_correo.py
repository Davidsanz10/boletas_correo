from fpdf import FPDF
import glob
import os
from enviar_email import enviar_email

class PDF(FPDF):
    # Configurar Cabecera
    def header(self):
        self.set_font("Arial", "B", 12)
        nombre_archivo = os.path.splitext(os.path.basename(self.nombre_boleta))[0]
        self.cell(0, 10, nombre_archivo, align="C", ln=1)
    # Configurar Pie de Pagina
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", align="C")
        
ruta_archivos_txt = "boletas_python/*.txt"

# Obtener la lista de archivos TXT en la ruta especificada
archivos_txt = glob.glob(ruta_archivos_txt)

archivo_pdf  = "consolidado_boletas.pdf"

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Combinar los archivos en PDF
for archivo_txt in archivos_txt:
    pdf.nombre_boleta = archivo_txt
    with open(archivo_txt, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=contenido)

pdf.output(archivo_pdf )

#print("Archivo PDF combinado creado con éxito: ", archivo_pdf )

destinatario = "davidsanz482@gmail.com"
asunto = "Archivo PDF consolidado de Boletas"
cuerpo = "Muy buenas, Estimada Área de Finanzas mando el consolidado de boletas en formato PDF"


enviar_email(destinatario, asunto, cuerpo, archivo_pdf)