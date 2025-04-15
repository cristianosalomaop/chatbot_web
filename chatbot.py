import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(?i)oi|olá|ola|e aí|e ai",
        ["Olá!", "Como posso te ajudar?", "Oi, como você está?"]
    ],

    [
        r"(?i)qual (é|e) o seu nome\??", 
        ["Me chamo FinBot, seu assistente financeiro!", "Pode me chamar de FinBot, especialista em investimentos."]
    ],

    [
        r"(?i)com o que você pode me ajudar\??", 
        ["Posso te ajudar com conceitos de economia e financeiro, dicas de investimento e tento deixar tudo mais simples pra você."]
    ],

    [
        r"(?i)qual (é|e) a melhor forma de investir\??", 
        ["Depende do seu perfil! Renda fixa é mais segura, mas renda variável pode ter mais retorno. Quer que eu te explique melhor?"]
    ],

    [
        r"(?i)o que (é|e) CDI|CDI\??", 
        ["CDI é um índice de referência de juros no Brasil, muito usado em investimentos de renda fixa. Vale ficar de olho!"]
    ],

    [
        r"(?i)o que (é|e) CDB|CDB\??", 
        ["CDB é o Certificado de Depósito Bancário. Você empresta dinheiro para o banco e recebe de volta com juros. É uma forma comum de renda fixa!"]
    ],

    [
        r"(?i)o que (é|e) selic|selic\??", 
        ["A Selic é a taxa básica de juros da economia brasileira. Ela influencia tudo: empréstimos, financiamentos e até a poupança."]
    ],

    [
        r"(?i)o que (é|e) renda fixa|renda fixa\??", 
        ["Renda fixa é um tipo de investimento onde você sabe (ou estima) quanto vai ganhar. Exemplos: Tesouro Direto, CDB, LCI."]
    ],

    [
        r"(?i)o que (é|e) renda vari(á|a)vel|renda vari(á|a)vel\??", 
        ["É o tipo de investimento cujo retorno não é garantido, como ações ou criptomoedas. Pode ganhar muito... ou perder."]
    ],

    [
        r"(?i)qual investimento tem menos risco\??", 
        ["Normalmente, os de renda fixa como o Tesouro Selic. Mas lembre-se: risco baixo, retorno geralmente menor."]
    ],

    [
        r"(?i)investimento em a(ç|c)(õ|o)es|a(ç|c)(õ|o)es (é|e) uma boa op(ç|c)(ã|a)o|a(ç|c)(õ|o)es\??", 
        ["Ações podem ser ótimas no longo prazo. Mas é bom estudar o mercado e entender o seu perfil de investidor."]
    ],

    [
        r"(?i)o que (é|e) inflaç(ã|a)o\??", 
        ["Inflação é o aumento geral e contínuo dos preços. Com ela, o seu dinheiro perde poder de compra."]
    ],

    [
        r"(?i)quem te criou\??", 
        ["Fui criado por um desenvolvedor apaixonado por finanças e tecnologia."]
    ],

    [
        r"(?i)como começar a investir\??",
        ["Primeiro, defina seus objetivos e descubra seu perfil de investidor. Depois, comece com produtos simples como o Tesouro Direto."]
    ],

    [
        r"(?i)vale a pena investir na poupan(ç|c)a|poupan(ç|c)a\??",
        ["A poupança é segura, mas rende pouco. Existem opções tão seguras quanto, com rendimentos melhores, como o Tesouro Selic."]
    ],

    [
        r"(?i)investimento de curto prazo|curto prazo\??",
        ["Para curto prazo, é bom investir em ativos de alta liquidez e baixo risco, como Tesouro Selic ou CDB com liquidez diária."]
    ],

    [
        r"(?i)o que (é|e) liquidez|liquidez\??",
        ["Liquidez é a facilidade de transformar um investimento em dinheiro. Alta liquidez = resgate rápido."]
    ],

    [
        r"(?i)como funciona o tesouro direto|tesouro direto\??",
        ["No tesouro direto você empresta dinheiro para o governo e recebe com juros depois. É uma das formas mais seguras de investir no Brasil."]
    ],

    [
        r"(?i)qual a diferença entre CDB e tesouro direto\??",
        ["Ambos são de renda fixa, mas o CDB é emitido por bancos e o Tesouro pelo governo. Tesouro tem mais segurança, CDB pode ter rentabilidade maior."]
    ],

    [
        r"(?i)o que (é|e) PIB|PIB\??",
        ["PIB é a soma de todos os bens e serviços produzidos no país. É uma forma de medir a economia."]
    ],

    [
        r"(?i)o que (é|e) taxa de juros|taxa de juros\??",
        ["É o custo do dinheiro. Afeta empréstimos, financiamentos e até investimentos."]
    ],

    [
        r"(?i)o que (é|e) taxa b(á|a)sica de juros|taxa b(á|a)sica de juros\??",
        ["É a taxa Selic! Ela é definida pelo Banco Central e influencia toda a economia."]
    ],

    [
        r"(?i)o que (é|e) c(â|a)mbio|como funciona o c(â|a)mbio|c(â|a)mbio\??",
        ["É a relação entre duas moedas, como real e dólar. O valor muda conforme a oferta e demanda."]
    ],

    [
        r"(?i)como economizar dinheiro\??",
        ["Anote seus gastos, corte supérfluos e defina metas de economia. Pequenas atitudes fazem diferença."]
    ],

    [
        r"(?i)como sair das d(í|i)vidas\??",
        ["Organize suas dívidas, priorize as com maior juros e tente renegociar. Depois, monte uma reserva para emergências."]
    ],

    [
        r"(?i)o que (é|e) reserva de emerg(ê|e)ncia|reserva de emerg(ê|e)ncia\??",
        ["É um valor guardado para imprevistos, equivalente a 3 a 6 meses dos seus gastos mensais, em algo seguro e com liquidez."]
    ],

    [
        r"(?i)quanto devo guardar por m(ê|e)s\??",
        ["O ideal é guardar pelo menos 10% da sua renda. Se der mais, melhor ainda!"]
    ],

    [
        r"(?i)não sei por onde começar|não sei como começar a investir|como começar a investir\??",
        ["Tudo bem, muita gente começa assim. Posso te guiar pelos primeiros passos do mundo financeiro. Primeiro, vamos descobrir seu perfil de investidor, para isso me confirme digitando perfil de investidor ou qual o meu perfil de investidor"]
    ],

    [
        r"(?i)o que s(ã|a)o a(ç|c)(õ|o)es\??",
        ["Ações são pequenas partes de uma empresa. Ao comprar uma, você vira sócio e participa dos lucros (ou prejuízos)."]
    ],

    [
        r"(?i)o que s(ã|a)o (ffis|fundos imobili(á|a)rios)|ffis\??",
        ["FIIs são fundos que investem em imóveis. Você ganha com aluguéis e valorização, sem precisar comprar imóveis diretamente."]
    ],

    [
        r"(?i)o que (é|e) day trade|day trade\??",
        ["É uma estratégia de compra e venda de ativos no mesmo dia. Pode dar lucro rápido, mas o risco é alto."]
    ],

    [
        r"(?i)renda passiva\??",
        ["Renda passiva é o dinheiro que entra sem você precisar trabalhar por ele, como aluguéis, dividendos ou juros de investimentos."]
    ],

    [
        r"(?i)o que (é|e) etfs|etfs\??",
        ["ETFs são fundos que replicam índices como o Ibovespa. É uma forma prática e diversificada de investir em ações."]
    ],

    [
        r"(?i)qual (meu|o) perfil de investidor|perfil de investidor\??",
        ["Existem 3 perfis principais:\n\n"
         "🟢 *Conservador*: busca segurança e prefere investimentos com baixo risco, como Tesouro Selic e CDBs.\n"
         "🟡 *Moderado*: aceita um pouco mais de risco, combina renda fixa com renda variável.\n"
         "🔴 *Arrojado*: busca altos retornos e tolera volatilidade, investe em ações, fundos e criptomoedas.\n\n"
         "Qual deles parece mais com você? "]
    ],

    [
        r"(?i)(sou|tenho perfil) conservador|investidor conservador",
        ["Como perfil conservador, o ideal é focar em segurança e liquidez.\n\n"
         "Sugestão: Tesouro Selic, CDBs com liquidez diária e fundos de renda fixa."]
    ],

    [
        r"(?i)(sou|tenho perfil) moderado|investidor moderado",
        ["Como investidor moderado, você pode diversificar.\n\n"
         "Ex: Tesouro IPCA, fundos multimercado e até ações de boas empresas."]
    ],

    [
        r"(?i)(sou|tenho perfil) arrojado|investidor arrojado",
        ["Você busca grandes retornos, mesmo com riscos maiores.\n\n"
         "Sugestão: ações, fundos de ações, criptomoedas e ETFs internacionais."]
    ],

    [
        r"(?i)tenho medo de perder dinheiro", 
        ["Todo investidor já sentiu isso. Por isso é importante estudar e começar com investimentos mais seguros."]
    ],

    [
        r"(?i)e se a bolsa cair\??", 
        ["Oscilações fazem parte. No longo prazo, ela costuma se recuperar. Ter estratégia e calma é o segredo."]
    ],

    [
        r"(?i)n(ã|a)o entendo nada de finan(ç|c)as", 
        ["Relaxa! Eu tô aqui pra te ajudar a aprender passo a passo. Vamos juntos nessa jornada."]
    ],

    [
        r"(?i)muito obrigado|valeu|obrigado",
        ["De nada! Se precisar de mais ajuda financeira, estou por aqui."]
    ],

    [
        r"(?i)tchau|até mais|falou",
        ["Tchau! Invista bem e volte quando quiser!"]
    ],

    [
        r"(.*)\?", 
        [
            "Desculpe, não tenho uma resposta específica para essa pergunta.", 
            "Você pode reformular a pergunta.", 
            "Não sei a resposta dessa pergunta, mas posso tentar te ajudar com outra coisa!",
            "Ainda não tenho uma resposta precisa pra isso. Quer tentar perguntar de outro jeito?"
        ]
    ],

    [
        r"(.*)", 
        [
            "Desculpe, não tenho uma resposta específica para essa pergunta.", 
            "Você pode reformular a pergunta.", 
            "Não sei a resposta dessa pergunta, mas posso tentar te ajudar com outra coisa!",
            "Ainda não tenho uma resposta precisa pra isso. Quer tentar perguntar de outro jeito?"
        ]
    ],
]



reflections = {
    "eu": "você",
    "meu": "seu",
    "você": "eu",
    "seu": "meu",
    "eu sou": "você é",
    "você é": "eu sou",
    "você estava": "eu estava",
    "eu estava": "você estava",
}


chatbot = Chat(pairs, reflections)

def responder(mensagem):
    resposta = chatbot.respond(mensagem.lower())
    if resposta:
        return resposta
    else:
        return "Não entendi muito bem... pode reformular?"