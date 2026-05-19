def numero_a_letras_entero(n):
    if n == 0: 
        return "cero"
        
    if n < 0:
        return "menos " + numero_a_letras_entero(abs(n))

    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
                "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    miles_digito = n // 1000
    resto_miles = n % 1000
    
    resultado_partes = []

    if miles_digito > 0:
        if miles_digito == 1:
            resultado_partes.append("mil")
        else:
            texto_miles = numero_a_letras_entero(miles_digito)
            if texto_miles == "uno":
                texto_miles = "un"
            elif texto_miles == "veintiuno":
                texto_miles = "veintiún"
            elif texto_miles.endswith("ciento uno"):
                texto_miles = texto_miles[:-3] + "un"
            elif texto_miles.endswith(" y uno"):
                texto_miles = texto_miles[:-3] + "ún"
            elif texto_miles.endswith("uno") and not texto_miles.endswith("veintiuno"):
                texto_miles = texto_miles[:-3] + "un"
                
            resultado_partes.append(f"{texto_miles} mil")

    if resto_miles > 0:
        c_digito = resto_miles // 100
        r_decena = resto_miles % 100

        if c_digito > 0:
            if c_digito == 1 and r_decena == 0:
                resultado_partes.append("cien")
            else:
                resultado_partes.append(centenas[c_digito])

        if r_decena > 0:
            if r_decena <= 20:
                resultado_partes.append(unidades[r_decena])
            elif r_decena < 30:
                resultado_partes.append("veinti" + unidades[r_decena - 20])
            else:
                dec = r_decena // 10
                uni = r_decena % 10
                if uni == 0:
                    resultado_partes.append(decenas[dec])
                else:
                    resultado_partes.append(f"{decenas[dec]} y {unidades[uni]}")

    return " ".join(resultado_partes)

def numero_a_letras(n):
    n = round(n, 4)
    parte_entera = int(abs(n))
    if parte_entera > 999999:
        raise ValueError("El número supera el rango permitido (-999,999 a 999,999).")

    if n.is_integer():
        return numero_a_letras_entero(int(n))
        
    str_n = f"{n:.4f}".rstrip('0')
    p_entera_str, p_decimal_str = str_n.split('.')
    
    p_entera_val = int(p_entera_str)
    txt_entera = numero_a_letras_entero(p_entera_val)
    if txt_entera == "" and p_entera_val == 0:
        txt_entera = "cero"
    elif n < 0 and p_entera_val == 0:
        txt_entera = "menos cero"

    digitos_map = {"0": "cero", "1": "uno", "2": "dos", "3": "tres", "4": "cuatro", 
                   "5": "cinco", "6": "seis", "7": "siete", "8": "ocho", "9": "nueve"}
    
    txt_decimal_partes = [digitos_map[d] for d in p_decimal_str]
    txt_decimal = " ".join(txt_decimal_partes)
    
    return f"{txt_entera} punto {txt_decimal}"