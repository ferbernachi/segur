import sys

# Zuk aurkitutako ordezkapen gako finkoa.
CLAVE_DE_SUSTITUCION = {
    'A': 'D', 'C': 'I', 'D': 'P', 'E': 'A',
    'F': 'X', 'G': 'J', 'H': 'T', 'I': 'O',
    'J': 'N', 'K': 'R', 'L': 'Z', 'M': 'H',
    'N': 'S', 'O': 'F', 'P': 'M', 'Q': 'B',
    'R': 'C', 'S': 'Q', 'T': 'L', 'U': 'G',
    'V': 'Y', 'X': 'E', 'Z': 'U',
    'v': 'V' 
    # Hemen ez dauden karaktereak (B, W, K, zenbakiak, espazioak...)
    # jatorrizkoan bezala geratuko dira.
}

def descifrar_con_clave_fija(texto_cifrado):
    """
    Testua karakterez karaktere itzultzen du gako finkoa erabiliz.
    """
    testu_deszifratua = ""
    for caracter in texto_cifrado:
        # Karakterea gure gakoan badago, ordezkatu egiten dugu.
        if caracter in CLAVE_DE_SUSTITUCION:
            testu_deszifratua += CLAVE_DE_SUSTITUCION[caracter]
        # Gakoan ez badago, bere horretan uzten dugu.
        else:
            testu_deszifratua += caracter
    return testu_deszifratua

def main():
    """
    Funtzio nagusia: fitxategia irakurri eta emaitza erakusten du.
    """
    # 1. Fitxategi izen bat pasatu digutela egiaztatu.
    if len(sys.argv) != 2:
        print("Erabilera: python3 deszifratzaile_automatikoa.py <zifratutako_fitxategia.txt>")
        sys.exit(1)

    nombre_archivo = sys.argv[1]

    # 2. Fitxategi zifratuaren edukia irakurri.
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            contenido_cifrado = f.read()
    except FileNotFoundError:
        print(f"Errorea: '{nombre_archivo}' fitxategia ez da aurkitu.")
        sys.exit(1)

    # 3. Edukia deszifratu eta pantailan erakutsi.
    texto_final = descifrar_con_clave_fija(contenido_cifrado)
    print(texto_final)

if __name__ == "__main__":
    main()
