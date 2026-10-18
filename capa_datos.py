# ============================================================
# PROYECTO DE FUNDAMENTOS DE PROGRAMACIÓN - CIIN1205P
# PROTOTIPO DE MESA DE PARTES DIGITAL - BOTICA (FACTURAS DE PROVEEDORES)
# INSTRUCCIONES PARA LOS INTEGRANTES:
# Cada uno debe pegar SU código en el lugar que le corresponde.
# ============================================================

# ------------------------------------------------------------
# ETAPA 1: PERSISTENCIA Y MANEJO DE ARCHIVOS (JSON)
# Autor: Juan Orlando Correa Flores
# ------------------------------------------------------------
import json
import os
import re

NOMBRE_ARCHIVO = "facturas.json"

def cargar_facturas():
    # Lee las facturas desde el archivo JSON y las retorna como lista.
    if not os.path.exists(NOMBRE_ARCHIVO):
        guardar_facturas([])
        return []
    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except Exception as error:
        print(f"[ERROR DATOS] No se pudo leer el archivo: {error}")
        return []

def guardar_facturas(lista_facturas):
    # Guarda la lista de facturas en el archivo JSON.
    try:
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(lista_facturas, archivo, ensure_ascii=False, indent=4)
        return True
    except Exception as error:
        print(f"[ERROR DATOS] No se pudo guardar en el archivo: {error}")
        return False

# ------------------------------------------------------------
# ETAPA 2: VALIDACIONES DE CADENAS Y EXPRESIONES REGULARES
# Autor: Zinedine Michael Callirgos Cabanillas
# PEGA AQUÍ TU CÓDIGO (validar_ruc, validar_codigo_factura, validar_fecha, existe_factura_duplicada)
# ------------------------------------------------------------

# ------------------------------------------------------------
# ETAPA 3: ALGORITMOS DE BÚSQUEDA TEXTUAL Y SECUENCIAL
# Autor: Alvaro Leandro Gutierrez Carranza
# PEGA AQUÍ TU CÓDIGO (buscar_por_codigo, buscar_por_proveedor)
# ------------------------------------------------------------

# ------------------------------------------------------------
# ETAPA 4: ALGORITMO DE ORDENAMIENTO POR SELECCIÓN
# Autor: Cristian Omar Huaman Rojas
# PEGA AQUÍ TU CÓDIGO (ordenar_por_fecha_seleccion)
# ------------------------------------------------------------

# ------------------------------------------------------------
# ETAPA 5: INTERFAZ DE CONSOLA, MENÚ PRINCIPAL Y ORQUESTACIÓN
# Autor: Anthony Rene Terraz Terrones
# PEGA AQUÍ TU CÓDIGO (mostrar_menu_principal, mostrar_tabla_facturas, ejecutar_registro, main)
# ------------------------------------------------------------