# ============================================================
# PROYECTO DE FUNDAMENTOS DE PROGRAMACION - CIIN1205P
# PROTOTIPO DE MESA DE PARTES DIGITAL - BOTICA
# FACTURAS DE PROVEEDORES
# ============================================================
import json
import os
import re

NOMBRE_ARCHIVO = "facturas.json"

# ------------------------------------------------------------
# ETAPA 1: PERSISTENCIA Y MANEJO DE ARCHIVOS (JSON)
# Autor: Juan Orlando Correa Flores
# ------------------------------------------------------------
def cargar_facturas():
    # Lee las facturas desde el archivo JSON y las retorna como lista
    if not os.path.exists(NOMBRE_ARCHIVO):
        guardar_facturas([])
        return []
    try:
        with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except Exception as error:
        print(f"Error al leer el archivo: {error}")
        return []

def guardar_facturas(lista_facturas):
    # Guarda la lista de facturas en el archivo JSON
    try:
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(lista_facturas, archivo, ensure_ascii=False, indent=4)
        return True
    except Exception as error:
        print(f"Error al guardar en el archivo: {error}")
        return False

# ------------------------------------------------------------
# ETAPA 2: VALIDACIONES DE CADENAS Y EXPRESIONES REGULARES
# Autor: Zinedine Michael Callirgos Cabanillas
# ------------------------------------------------------------
def validar_ruc(ruc):
    # Valida que el RUC tenga exactamente 11 digitos numericos
    ruc_limpio = ruc.strip()
    return bool(re.fullmatch(r"^\d{11}$", ruc_limpio))

def validar_codigo_factura(codigo):
    # Valida que el codigo no este vacio y sea alfanumerico
    codigo_limpio = codigo.strip().upper()
    return len(codigo_limpio) > 0 and bool(re.fullmatch(r"^[A-Z0-9\-]+$", codigo_limpio))

def validar_fecha(fecha_str):
    # Valida que la fecha tenga formato AAAA-MM-DD y rangos validos
    fecha_limpia = fecha_str.strip()
    patron = r"^\d{4}-\d{2}-\d{2}$"
    if re.fullmatch(patron, fecha_limpia):
        partes = fecha_limpia.split("-")
        anio, mes, dia = int(partes[0]), int(partes[1]), int(partes[2])
        if 1900 <= anio <= 2100 and 1 <= mes <= 12 and 1 <= dia <= 31:
            return True
    return False

def existe_factura_duplicada(lista_facturas, codigo):
    # Verifica si el codigo de factura ya existe en el registro
    codigo_limpio = codigo.strip().upper()
    for factura in lista_facturas:
        if factura.get("codigo", "").upper() == codigo_limpio:
            return True
    return False

# ------------------------------------------------------------
# ETAPA 3: ALGORITMOS DE BUSQUEDA TEXTUAL Y SECUENCIAL
# Autor: Alvaro Leandro Gutierrez Carranza
# ------------------------------------------------------------
def buscar_por_codigo(lista_facturas, codigo_busqueda):
    # Busqueda secuencial por codigo exacto de factura
    codigo_limpio = codigo_busqueda.strip().upper()
    for factura in lista_facturas:
        if factura.get("codigo", "").upper() == codigo_limpio:
            return factura
    return None

def buscar_por_proveedor(lista_facturas, nombre_proveedor):
    # Busqueda parcial de facturas por nombre de proveedor
    proveedor_limpio = nombre_proveedor.strip().lower()
    resultados = []
    for factura in lista_facturas:
        if proveedor_limpio in factura.get("proveedor", "").lower():
            resultados.append(factura)
    return resultados

# ------------------------------------------------------------
# ETAPA 4: ALGORITMO DE ORDENAMIENTO POR SELECCION
# Autor: Cristian Omar Huaman Rojas
# ------------------------------------------------------------
def ordenar_por_fecha_seleccion(lista_facturas):
    # Ordena una copia de la lista por fecha utilizando el Algoritmo de Seleccion
    lista_copia = list(lista_facturas)
    n = len(lista_copia)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lista_copia[j].get("fecha", "") < lista_copia[min_idx].get("fecha", ""):
                min_idx = j
        # Intercambio de posiciones (Swap)
        lista_copia[i], lista_copia[min_idx] = lista_copia[min_idx], lista_copia[i]
    return lista_copia

# ------------------------------------------------------------
# ETAPA 5: INTERFAZ DE CONSOLA, MENU PRINCIPAL Y ORQUESTACION
# Autor: Anthony Rene Terraz Terrones
# ------------------------------------------------------------
def mostrar_menu_principal():
    # Muestra el menu de opciones en consola
    print("\n" + "="*60)
    print(" MESA DE PARTES DIGITAL - BOTICA (GESTION DE FACTURAS)")
    print("="*60)
    print("1. Registrar nueva factura de proveedor")
    print("2. Buscar factura por Codigo")
    print("3. Buscar facturas por Nombre de Proveedor")
    print("4. Ordenar y listar facturas por Fecha (Algoritmo Seleccion)")
    print("5. Mostrar todas las facturas registradas")
    print("6. Salir")
    print("="*60)
    return input("Seleccione una opcion (1-6): ").strip()

def mostrar_tabla_facturas(lista_facturas, titulo="LISTADO DE FACTURAS"):
    # Muestra la tabla de facturas formateada
    print(f"\n--- {titulo} ---")
    if not lista_facturas:
        print("No se encontraron registros de facturas.")
        return
    encabezado = f"{'CODIGO':<12} | {'RUC':<12} | {'PROVEEDOR':<25} | {'FECHA':<12} | {'OBSERVACION'}"
    linea = "-" * len(encabezado)
    print(linea)
    print(encabezado)
    print(linea)
    for f in lista_facturas:
        codigo = f.get("codigo", "")[:12]
        ruc = f.get("ruc", "")[:12]
        proveedor = f.get("proveedor", "")[:25]
        fecha = f.get("fecha", "")[:12]
        obs = f.get("observacion", "-")[:20]
        print(f"{codigo:<12} | {ruc:<12} | {proveedor:<25} | {fecha:<12} | {obs}")
    print(linea)

def ejecutar_registro(lista_facturas):
    # Realiza la captura de datos y validaciones para registrar una factura
    print("\n--- REGISTRO DE NUEVA FACTURA ---")
    codigo = input("Ingrese Codigo de Factura (ej. F001-00123): ").strip().upper()
    if not validar_codigo_factura(codigo):
        print("Error: Codigo invalido. Debe ser alfanumerico.")
        return
    if existe_factura_duplicada(lista_facturas, codigo):
        print(f"Error: Ya existe una factura registrada con el codigo '{codigo}'.")
        return
    ruc = input("Ingrese RUC del proveedor (11 digitos): ").strip()
    if not validar_ruc(ruc):
        print("Error: RUC invalido. Debe tener exactamente 11 digitos numericos.")
        return
    proveedor = input("Ingrese Nombre/Razon Social del proveedor: ").strip()
    if not proveedor:
        print("Error: El nombre del proveedor no puede estar vacio.")
        return
    fecha = input("Ingrese Fecha de factura (Formato AAAA-MM-DD): ").strip()
    if not validar_fecha(fecha):
        print("Error: Fecha invalida. Utilice el formato AAAA-MM-DD (ej. 2026-10-17).")
        return
    observacion = input("Observacion (opcional): ").strip()
    if not observacion:
        observacion = "Sin observaciones"
    
    nueva_factura = {
        "codigo": codigo,
        "ruc": ruc,
        "proveedor": proveedor,
        "fecha": fecha,
        "observacion": observacion
    }
    lista_facturas.append(nueva_factura)
    
    if guardar_facturas(lista_facturas):
        print("Factura registrada y guardada en archivo exitosamente.")
    else:
        print("Factura agregada en memoria pero fallo la persistencia.")

def main():
    # Funcion principal que ejecuta el bucle del programa
    lista_facturas = cargar_facturas()
    print(f"Sistema iniciado. Facturas cargadas desde archivo: {len(lista_facturas)}")
    
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == "1":
            ejecutar_registro(lista_facturas)
        elif opcion == "2":
            cod = input("\nIngrese Codigo de factura a buscar: ").strip()
            hallado = buscar_por_codigo(lista_facturas, cod)
            if hallado:
                mostrar_tabla_facturas([hallado], f"FACTURA ENCONTRADA ({cod})")
            else:
                print(f"No se encontro ninguna factura con el codigo '{cod}'.")
        elif opcion == "3":
            prov = input("\nIngrese nombre del proveedor a buscar: ").strip()
            resultados = buscar_por_proveedor(lista_facturas, prov)
            if resultados:
                mostrar_tabla_facturas(resultados, f"RESULTADOS PARA '{prov}'")
            else:
                print(f"No se encontraron facturas para el proveedor '{prov}'.")
        elif opcion == "4":
            if not lista_facturas:
                print("No hay facturas para ordenar.")
            else:
                lista_ordenada = ordenar_por_fecha_seleccion(lista_facturas)
                mostrar_tabla_facturas(lista_ordenada, "FACTURAS ORDENADAS POR FECHA (SELECCION)")
        elif opcion == "5":
            mostrar_tabla_facturas(lista_facturas, "TODAS LAS FACTURAS REGISTRADAS")
        elif opcion == "6":
            guardar_facturas(lista_facturas)
            print("\nGracias por usar la Mesa de Partes Digital. Datos guardados. Hasta luego.")
            break
        else:
            print("Opcion invalida. Ingrese un numero del 1 al 6.")

if __name__ == "__main__":
    main()