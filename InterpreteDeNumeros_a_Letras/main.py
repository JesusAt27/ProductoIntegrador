from lexer import lexer
from parser_eval import Parser
from traductor import numero_a_letras

if __name__ == "__main__":
    while True:
        print("\n   COMPILADOR INTERACTIVO CON PARÉNTESIS Y DECIMAL  ")
        print("1. Modo Traducción Directa")
        print("2. Modo Inspección de Árbol Sintáctico (AST)")
        print("3. Salir\n")
        
        opcion = input("Selecciona una opción (1-3): ").strip()
        
        if opcion == '3':
            print("¡Hasta luego!")
            break
            
        if opcion in ('1', '2'):
            entrada = input("\nIntroduce la operación (ej: (1 + 2) * 3): ").strip()
            if not entrada:
                continue
                
            try:
                tokens = lexer(entrada)
                analizador = Parser(tokens)
                arbol_ast = analizador.expresion()
                resultado, texto_traducido = arbol_ast.evaluar()
                resultado_letras = numero_a_letras(resultado)
                
                if opcion == '1':
                    print("\n--- RESULTADO DE LA TRADUCCIÓN ---")
                    print(f" -> Resultado Real: {resultado}")
                    print(f" -> Operación Evaluada: {texto_traducido}")
                    print(f" -> Resultado en Letras: {resultado_letras}\n")
                elif opcion == '2':
                    print("\n--- ÁRBOL DE SINTAXIS ABSTRACTA (AST) ---")
                    arbol_ast.mostrar_arbol()
                    print(f"\n -> Evaluación matemática del árbol: {resultado}\n")
                    
            except (SyntaxError, ZeroDivisionError, ValueError) as e:
                print(f"\n[Error de Compilación]: {e}\n")
            except Exception as e:
                print(f"\n[Error Inesperado]: {e}\n")
        else:
            print("\nOpción no válida. Intenta de nuevo.\n")