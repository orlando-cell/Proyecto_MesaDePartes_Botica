from capa_datos import cargar_facturas, guardar_facturas
#Etapa4:
def ordenar_por_fecha_seleccion(lista_facturas):
    
    lista_copia = list(lista_facturas)
    n = len(lista_copia)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if lista_copia[j].get("fecha", "") < lista_copia[min_idx].get("fecha", ""):
                min_idx = j

        
        lista_copia[i], lista_copia[min_idx] = lista_copia[min_idx], lista_copia[i]

    return lista_copia

#Etapa5:
def mostrar_menu_principal():
    print("\n" + "="*60)
    print("   MESA DE PARTES DIGITAL - BOTICA (GESTIÓN DE FACTURAS)")
    print("="*60)
    print("1. Registrar nueva factura de proveedor")
    print("2. Buscar factura por Código")
    print("3. Buscar facturas por Nombre de Proveedor")
    print("4. Ordenar y listar facturas por Fecha (Algoritmo Selección)")
    print("5. Mostrar todas las facturas registradas")
    print("6. Salir")
    print("="*60)
    return input("Seleccione una opción (1-6): ").strip()

def mostrar_tabla_facturas(lista_facturas, titulo="LISTADO DE FACTURAS"):
    print(f"\n--- {titulo} ---")
    if not lista_facturas:
        print("No se encontraron registros de facturas.")
        return
    
    encabezado = f"{'CÓDIGO':<12} | {'RUC':<12} | {'PROVEEDOR':<25} | {'FECHA':<12} | {'OBSERVACIÓN'}"
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
    print("\n--- REGISTRO DE NUEVA FACTURA ---")
    codigo = input("Ingrese Código de Factura (ej. F001-00123): ").strip().upper()
    if not validar_codigo_factura(codigo):
        print("Error: Código inválido. Debe ser alfanumérico.")
        return
    
    if existe_factura_duplicada(lista_facturas, codigo):
        print(f"Error: Ya existe una factura registrada con el código '{codigo}'.")
        return
    
    ruc = input("Ingrese RUC del proveedor (11 dígitos): ").strip()
    if not validar_ruc(ruc):
        print("Error: RUC inválido. Debe tener exactamente 11 dígitos numéricos.")
        return
        
    proveedor = input("Ingrese Nombre/Razón Social del proveedor: ").strip()
    if not proveedor:
        print("Error: El nombre del proveedor no puede estar vacío.")
        return
        
    fecha = input("Ingrese Fecha de factura (Formato AAAA-MM-DD): ").strip()
    if not validar_fecha(fecha):
        print("Error: Fecha inválida. Utilice el formato AAAA-MM-DD (ej. 2026-10-17).")
        return
        
    observacion = input("Observación (opcional): ").strip()
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
        print("Factura agregada en memoria pero falló la persistencia.")

def main():
    lista_facturas = cargar_facturas()
    print(f"Sistema iniciado. Facturas cargadas desde archivo: {len(lista_facturas)}")
    
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == "1":
            ejecutar_registro(lista_facturas)
            
        elif opcion == "2":
            cod = input("\nIngrese Código de factura a buscar: ").strip()
            hallado = buscar_por_codigo(lista_facturas, cod)
            if hallado:
                mostrar_tabla_facturas([hallado], f"FACTURA ENCONTRADA ({cod})")
            else:
                print(f"No se encontró ninguna factura con el código '{cod}'.")
                
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
                mostrar_tabla_facturas(lista_ordenada, "FACTURAS ORDENADAS POR FECHA (ALGORITMO SELECCIÓN)")
                
        elif opcion == "5":
            mostrar_tabla_facturas(lista_facturas, "TODAS LAS FACTURAS REGISTRADAS")
            
        elif opcion == "6":
            guardar_facturas(lista_facturas)
            print("\nGracias por usar la Mesa de Partes Digital! Datos guardados. Hasta luego.")
            break
            
        else:
            print("Opción inválida. Ingrese un número del 1 al 6.")

if __name__ == "__main__":
    main()







