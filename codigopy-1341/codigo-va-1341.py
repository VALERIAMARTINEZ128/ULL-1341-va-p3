# =========================================
# Autor: valeria yaretzi NC = 1341
# =========================================

import cv2
import numpy as np
from pathlib import Path

# -----------------------------------------
# 1. Definir las rutas del proyecto
# -----------------------------------------

CARPETA_PROYECTO = Path(__file__).resolve().parent.parent

RUTA_IMAGEN = (
    CARPETA_PROYECTO
    / "img-original-1341"
    / "img-congelador-1341.jpg"
)

CARPETA_RESULTADOS = (
    CARPETA_PROYECTO / "resultados-img-1341"
)

# Crear la carpeta de resultados si no existe
CARPETA_RESULTADOS.mkdir(parents=True, exist_ok=True)

# -----------------------------------------
# 2. Comprobar que existe la imagen
# -----------------------------------------

if not RUTA_IMAGEN.is_file():
    print("ERROR: No se encontro la imagen.")
    print("Coloca img-congelador-1341.jpg en:")
    print(RUTA_IMAGEN)
    raise SystemExit(1)

# -----------------------------------------
# 3. Obtener el tamaño del archivo
# -----------------------------------------

tamano_bytes = RUTA_IMAGEN.stat().st_size
tamano_kb = tamano_bytes / 1024
tamano_mb = tamano_bytes / (1024 * 1024)

# -----------------------------------------
# 4. Leer la imagen con OpenCV y convertir a RGB
# -----------------------------------------

imagen_bgr = cv2.imread(str(RUTA_IMAGEN), cv2.IMREAD_COLOR)

if imagen_bgr is None:
    print("ERROR: El archivo no es una imagen valida")
    print("o el formato no se pudo interpretar.")
    raise SystemExit(1)

# Convertir el orden de canales de BGR a RGB
imagen_rgb = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2RGB)

# -----------------------------------------
# 5. Obtener dimensiones y canales
# -----------------------------------------

alto, ancho, canales = imagen_rgb.shape

total_pixeles = ancho * alto
resolucion = f"{ancho} x {alto}"

# -----------------------------------------
# 6. Consultar propiedades de los pixeles (en RGB)
# -----------------------------------------

tipo_datos = str(imagen_rgb.dtype)
valor_minimo = int(np.min(imagen_rgb))
valor_maximo = int(np.max(imagen_rgb))
promedio = float(np.mean(imagen_rgb))

# Separación completa de canales RGB
promedio_r = float(np.mean(imagen_rgb[:, :, 0]))
promedio_g = float(np.mean(imagen_rgb[:, :, 1]))
promedio_b = float(np.mean(imagen_rgb[:, :, 2]))

# -----------------------------------------
# 7. Crear versiones completas de la imagen en cada canal
# -----------------------------------------

# Canal Rojo Completo (Solo R)
imagen_roja = np.zeros_like(imagen_rgb)
imagen_roja[:, :, 0] = imagen_rgb[:, :, 0]

# Canal Verde Completo (Solo G)
imagen_verde = np.zeros_like(imagen_rgb)
imagen_verde[:, :, 1] = imagen_rgb[:, :, 1]

# Canal Azul Completo (Solo B)
imagen_azul = np.zeros_like(imagen_rgb)
imagen_azul[:, :, 2] = imagen_rgb[:, :, 2]

# -----------------------------------------
# 8. Preparar el informe
# -----------------------------------------

informe = f"""
INFORME DE METADATOS Y PROPIEDADES - CONGELADOR (RGB)
=====================================================
Estudiante: valeria yaretzi NC = 1341

Nombre del archivo: {RUTA_IMAGEN.name}
Ruta del archivo: {RUTA_IMAGEN}
Formato por extension: {RUTA_IMAGEN.suffix.upper()}
Tamano en bytes: {tamano_bytes}
Tamano en KB: {tamano_kb:.2f}
Tamano en MB: {tamano_mb:.4f}

DIMENSIONES
-----------
Ancho: {ancho} pixeles
Alto: {alto} pixeles
Resolucion: {resolucion}
Total de pixeles: {total_pixeles:,}

CANALES Y DATOS
---------------
Numero de canales: {canales}
Orden de canales: RGB
Tipo de datos: {tipo_datos}
Valor minimo de pixel: {valor_minimo}
Valor maximo de pixel: {valor_maximo}
Promedio general de los valores: {promedio:.2f}

PROMEDIO POR CANAL
------------------
Rojo (R): {promedio_r:.2f}
Verde (G): {promedio_g:.2f}
Azul (B): {promedio_b:.2f}

Nota: Se extrajeron las tres imagenes completas correspondientes
a cada uno de los canales RGB.
"""

# -----------------------------------------
# 9. Mostrar el informe en la terminal
# -----------------------------------------

print(informe)

# -----------------------------------------
# 10. Guardar el informe automáticamente
# -----------------------------------------

ruta_informe = CARPETA_RESULTADOS / "metadatos-congelador-1341.txt"
ruta_informe.write_text(informe, encoding="utf-8")

# -----------------------------------------
# 11. Guardar copias completas de la imagen por canal
# -----------------------------------------
# -----------------------------------------
# 11. Guardar copias completas de la imagen por canal
# -----------------------------------------

# Para guardar con cv2.imwrite reconvertimos a BGR
cv2.imwrite(str(CARPETA_RESULTADOS / "congelador-canal-rojo-1341.jpg"), cv2.cvtColor(imagen_roja, cv2.COLOR_RGB2BGR))
cv2.imwrite(str(CARPETA_RESULTADOS / "congelador-canal-verde-1341.jpg"), cv2.cvtColor(imagen_verde, cv2.COLOR_RGB2BGR))
cv2.imwrite(str(CARPETA_RESULTADOS / "congelador-canal-azul-1341.jpg"), cv2.cvtColor(imagen_azul, cv2.COLOR_RGB2BGR))

# -----------------------------------------
# 12. Mostrar las imágenes completas en pantalla
# -----------------------------------------

cv2.imshow("Imagen Original - Valeria Yaretzi 1341", imagen_bgr)
cv2.imshow("Canal Rojo Completo (R) - 1341", cv2.cvtColor(imagen_roja, cv2.COLOR_RGB2BGR))
cv2.imshow("Canal Verde Completo (G) - 1341", cv2.cvtColor(imagen_verde, cv2.COLOR_RGB2BGR))
cv2.imshow("Canal Azul Completo (B) - 1341", cv2.cvtColor(imagen_azul, cv2.COLOR_RGB2BGR))

print("Presiona cualquier tecla en una ventana para cerrar...")
cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------------------
# 13. Finalizar
# -----------------------------------------

print("Practica completada correctamente.")
print("Informe:", ruta_informe)

# =========================================
print("valeria yaretzi NC = 1341")
# =========================================