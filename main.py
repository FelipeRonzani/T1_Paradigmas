class NumeroPorExtenso:
    def __init__(self, numero):
        # Construtor da classe que inicializa o número e as listas de unidades, dezenas, dezenas completas e centavos
        self.numero = numero # Atributo que armazena o número fornecido
        self.unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
        self.dezena = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
        self.dezena_completa = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
        self.centena = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
        self.milhares = ["", "mil", "milhão", "milhões"]
        self.centavos = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte", "vinte e um", "vinte e dois", "vinte e três", "vinte e quatro", "vinte e cinco", "vinte e seis", "vinte e sete", "vinte e oito", "vinte e nove", "trinta", "trinta e um", "trinta e dois", "trinta e três", "trinta e quatro", "trinta e cinco", "trinta e seis", "trinta e sete", "trinta e oito", "trinta e nove", "quarenta", "quarenta e um", "quarenta e dois", "quarenta e três", "quarenta e quatro", "quarenta e cinco", "quarenta e seis", "quarenta e sete", "quarenta e oito", "quarenta e nove", "cinquenta", "cinquenta e um", "cinquenta e dois", "cinquenta e três", "cinquenta e quatro", "cinquenta e cinco", "cinquenta e seis", "cinquenta e sete", "cinquenta e oito", "cinquenta e nove", "sessenta", "sessenta e um", "sessenta e dois", "sessenta e três", "sessenta e quatro", "sessenta e cinco", "sessenta e seis", "sessenta e sete", "sessenta e oito", "sessenta e nove", "setenta", "setenta e um", "setenta e dois", "setenta e três", "setenta e quatro", "setenta e cinco", "setenta e seis", "setenta e sete", "setenta e oito", "setenta e nove", "oitenta", "oitenta e um", "oitenta e dois", "oitenta e três", "oitenta e quatro", "oitenta e cinco", "oitenta e seis", "oitenta e sete", "oitenta e oito", "oitenta e nove", "noventa", "noventa e um", "noventa e dois", "noventa e três", "noventa e quatro", "noventa e cinco", "noventa e seis", "noventa e sete", "noventa e oito", "noventa e nove"]

        # Versão em inglês
        self.unidades_en = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        self.dezena_en = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.dezena_completa_en = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        self.milhares_en = ["", "thousand", "million", "million"]
        self.centavos_en = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "thirty", "thirty one", "thirty two", "thirty three", "thirty four", "thirty five", "thirty six", "thirty seven", "thirty eight", "thirty nine", "forty", "forty one", "forty two", "forty three", "forty four", "forty five", "forty six", "forty seven", "forty eight", "forty nine", "fifty", "fifty one", "fifty two", "fifty three", "fifty four", "fifty five", "fifty six", "fifty seven", "fifty eight", "fifty nine", "sixty", "sixty one", "sixty two", "sixty three", "sixty four", "sixty five", "sixty six", "sixty seven", "sixty eight", "sixty nine", "seventy", "seventy one", "seventy two", "seventy three", "seventy four", "seventy five", "seventy six", "seventy seven", "seventy eight", "seventy nine", "eighty", "eighty one", "eighty two", "eighty three", "eighty four", "eighty five", "eighty six", "eighty seven", "eighty eight", "eighty nine", "ninety", "ninety one", "ninety two", "ninety three", "ninety four", "ninety five", "ninety six", "ninety seven", "ninety eight", "ninety nine"]

    def numero_por_extenso(self):
        inteiro, decimal = str(self.numero).split(".")
        inteiro = int(inteiro)
        decimal = int(decimal)

        extenso = self._extenso_inteiro(inteiro)
        if decimal > 0:
            extenso += " e " + self._extenso_centavos(decimal)
        else:
            extenso += " e zero centavos"  # Caso o valor dos centavos seja zero
        
        # Chamando os métodos para a versão em inglês
        extenso_en = self._extenso_inteiro_ingles(inteiro)
        if decimal > 0:
            extenso_en += " and " + self._extenso_centavos_ingles(decimal)
        else:
            extenso_en += " and zero cents"

        return extenso, extenso_en

    def _extenso_inteiro(self, numero):
        if numero == 0:
            return "zero"
        
        partes = []
        milhar_contador = 0

        # Para cada casa (unidade, dezena, centena)
        while numero > 0:
            parte_atual = numero % 1000
            if parte_atual > 0:
                partes.insert(0, self._porcento_parte(parte_atual, milhar_contador))
            numero //= 1000
            milhar_contador += 1
        
        return " ".join(partes).strip()

    def _extenso_inteiro_ingles(self, numero):
        if numero == 0:
            return "zero"
        
        partes = []
        milhar_contador = 0

        # Para cada casa (unidade, dezena, centena)
        while numero > 0:
            parte_atual = numero % 1000
            if parte_atual > 0:
                partes.insert(0, self._porcento_parte_ingles(parte_atual, milhar_contador))
            numero //= 1000
            milhar_contador += 1
        
        return " ".join(partes).strip()
    
    def _porcento_parte(self, numero, milhar_contador):
        unidade = self.unidades[numero % 10]
        dezena = self.dezena[(numero // 10) % 10]
        centena = self.centena[(numero // 100) % 10]
        
        centena_str = f"{centena}" if centena else ""
        if centena and (dezena or unidade):
            centena_str += " e "

        dezena_str = f"{dezena}" if dezena else ""
        if dezena and unidade:
            dezena_str += " e "

        unidade_str = f"{unidade}" if unidade else ""

        if milhar_contador == 0:
            return f"{centena_str}{dezena_str}{unidade_str}".strip()
        elif milhar_contador == 1:
            return f"{centena_str}{dezena_str}{unidade_str} mil".strip()
        elif milhar_contador == 2:
            return f"{centena_str}{dezena_str}{unidade_str} milhão" if numero == 1 else f"{centena_str}{dezena_str}{unidade_str} milhões"
        elif milhar_contador == 3:
            return f"{centena_str}{dezena_str}{unidade_str} bilhões"

    def _porcento_parte_ingles(self, numero, milhar_contador):
        unidade = self.unidades_en[numero % 10]
        dezena = self.dezena_en[(numero // 10) % 10]
        centena = self.unidades_en[(numero // 100) % 10]
        
        centena_str = f"{centena} hundred" if centena else ""
        if centena and (dezena or unidade):
            centena_str += " and "

        dezena_str = f"{dezena}" if dezena else ""
        if dezena and unidade:
            dezena_str += " and "

        unidade_str = f"{unidade}" if unidade else ""

        if milhar_contador == 0:
            return f"{centena_str}{dezena_str}{unidade_str}".strip()
        elif milhar_contador == 1:
            return f"{centena_str}{dezena_str}{unidade_str} thousand".strip()
        elif milhar_contador == 2:
            return f"{centena_str}{dezena_str}{unidade_str} million" if numero == 1 else f"{centena_str}{dezena_str}{unidade_str} millions"
        elif milhar_contador == 3:
            return f"{centena_str}{dezena_str}{unidade_str} billion"
        
    def _extenso_centavos(self, numero):
        if numero == 0:
            return "zero centavos"
        elif numero < 100:
            return self.centavos[numero] + " centavo" + ("s" if numero > 1 else "")
        else:
            return "Erro: Centavos inválidos"
        
    def _extenso_centavos_ingles(self, numero):
        if numero == 0:
            return "zero cents"
        elif numero < 100:
            return self.centavos_en[numero] + " cent" + ("s" if numero > 1 else "")
        else:
            return "Error: Invalid cents"
        
def numero_por_extenso_imperativo(numero):
    try:
        numero_float = float(numero)
    except ValueError:
        return "Formato de número inválido!"

    inteiro, decimal = str(numero_float).split(".")
    inteiro = int(inteiro)
    decimal = int(decimal)

    extenso = extenso_inteiro(inteiro)
    extenso_en = extenso_inteiro_ingles(inteiro)

    if decimal == 0:
        extenso += " e zero centavos"
    else:
        extenso += f" e {extenso_centavos(decimal)}"
    
    # Para centavos em inglês
    if decimal == 0:
        extenso_en += " and zero cents"
    elif decimal > 0:
        extenso_en += " and " + extenso_centavos_ingles(decimal)
    
    return extenso, extenso_en

def extenso_inteiro(numero):
    if numero == 0:
        return "zero"

    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
    
    partes = []

    if numero >= 1_000_000:
        milhoes = numero // 1_000_000
        partes.append(f"{extenso_inteiro(milhoes)} {'milhão' if milhoes == 1 else 'milhões'}")
        numero %= 1_000_000

    if numero >= 1_000:
        milhares = numero // 1_000
        if milhares == 1:
            partes.append("mil")
        else:
            partes.append(f"{extenso_inteiro(milhares)} mil")
        numero %= 1_000

    if numero == 100:
        partes.append("cem")
    elif numero >= 100:
        centena = numero // 100
        resto = numero % 100
        partes.append(centenas[centena])
        if resto > 0:
            partes.append(extenso_inteiro(resto))
        numero = 0

    if 10 <= numero < 20:
        partes.append(especiais[numero - 10])
    elif numero >= 20:
        dezena = numero // 10
        unidade = numero % 10
        partes.append(dezenas[dezena])
        if unidade > 0:
            partes.append(unidades[unidade])
    elif numero > 0:
        partes.append(unidades[numero])

    return " e ".join(partes)

def extenso_inteiro_ingles(numero):
    if numero == 0:
        return "zero"

    unidades_en = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    dezenas_en = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    especiais_en = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    centenas_en = ["", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]

    partes = []

    if numero >= 1_000_000:
        milhoes = numero // 1_000_000
        partes.append(f"{extenso_inteiro_ingles(milhoes)} {'million' if milhoes == 1 else 'millions'}")
        numero %= 1_000_000

    if numero >= 1_000:
        milhares = numero // 1_000
        if milhares == 1:
            partes.append("one thousand")
        else:
            partes.append(f"{extenso_inteiro_ingles(milhares)} thousand")
        numero %= 1_000

    if numero == 100:
        partes.append("one hundred")
    elif numero >= 100:
        centena = numero // 100
        resto = numero % 100
        partes.append(centenas_en[centena])
        if resto > 0:
            partes.append(extenso_inteiro_ingles(resto))
        numero = 0

    if 10 <= numero < 20:
        partes.append(especiais_en[numero - 10])
    elif numero >= 20:
        dezena = numero // 10
        unidade = numero % 10
        partes.append(dezenas_en[dezena])
        if unidade > 0:
            partes.append(unidades_en[unidade])
    elif numero > 0:
        partes.append(unidades_en[numero])

    return " and ".join(partes)

def extenso_centavos(numero):
    if numero == 0:
        return "zero centavos"

    dezenas_centavos = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    especiais_centavos = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    unidades_centavos = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]

    partes = []

    if 10 <= numero < 20:
        partes.append(especiais_centavos[numero - 10])
    elif numero >= 20:
        dezena = numero // 10
        unidade = numero % 10
        partes.append(dezenas_centavos[dezena])
        if unidade > 0:
            partes.append(unidades_centavos[unidade])
    elif numero > 0:
        partes.append(unidades_centavos[numero])

    return " e ".join(partes) + " centavos"

def extenso_centavos_ingles(numero):
    centavos_en = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
                   "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", 
                   "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", 
                   "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "thirty", 
                   "thirty one", "thirty two", "thirty three", "thirty four", "thirty five", "thirty six", 
                   "thirty seven", "thirty eight", "thirty nine", "forty", "forty one", "forty two", "forty three", 
                   "forty four", "forty five", "forty six", "forty seven", "forty eight", "forty nine", "fifty", 
                   "fifty one", "fifty two", "fifty three", "fifty four", "fifty five", "fifty six", "fifty seven", 
                   "fifty eight", "fifty nine", "sixty", "sixty one", "sixty two", "sixty three", "sixty four", 
                   "sixty five", "sixty six", "sixty seven", "sixty eight", "sixty nine", "seventy", "seventy one", 
                   "seventy two", "seventy three", "seventy four", "seventy five", "seventy six", "seventy seven", 
                   "seventy eight", "seventy nine", "eighty", "eighty one", "eighty two", "eighty three", 
                   "eighty four", "eighty five", "eighty six", "eighty seven", "eighty eight", "eighty nine", 
                   "ninety", "ninety one", "ninety two", "ninety three", "ninety four", "ninety five", 
                   "ninety six", "ninety seven", "ninety eight", "ninety nine"]
    
    if numero == 0:
        return "zero cents"
    elif numero < 100:
        return centavos_en[numero] + " cent" + ("s" if numero > 1 else "")
    else:
        return "Error: Invalid cents"

def menu_objetivo():
    while True:
        print("\nEscolha o programa:")
        print("1 - Programa Orientado a Objetos")
        print("2 - Programa Imperativo")
        print("3 - Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            numero = input("Digite um número com ponto flutuante: ")
            numero = numero.replace(",", ".")  # Substitui a vírgula por ponto
            try:
                numero = float(numero)
                numero_extenso = NumeroPorExtenso(numero)
                print(f"Número por extenso: {numero_extenso.numero_por_extenso()}")
            except ValueError:
                print("Formato de número inválido!")
        elif opcao == '2':
            numero = input("Digite um número com ponto flutuante: ")
            numero = numero.replace(",", ".")  # Substitui a vírgula por ponto
            try:
                numero = float(numero)
                print(f"Número por extenso: {numero_por_extenso_imperativo(numero)}")
            except ValueError:
                print("Formato de número inválido!")
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Rodar o menu
menu_objetivo()
