import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"Oi|Olá|E ai|Ola",
        ["Olá!", "Como posso te ajudar?", "Oi, como você está?"]
    ],

    [
        r"(?i)qual é o seu nome\??", 
        ["Me chamo FinBot, seu assistente financeiro!", "Pode me chamar de FinBot, especialista em investimentos."]
    ],

    [
        r"(?i)você pode me ajudar\??", 
        ["Claro! Posso te ajudar com conceitos de economia, dicas de investimento e muito mais."]
    ],

    [
        r"(?i)o que você faz\??", 
        ["Eu explico conceitos financeiros, dou dicas de investimento e tento deixar tudo mais simples pra você."]
    ],

    [
        r"(?i)qual a melhor forma de investir\??", 
        ["Depende do seu perfil! Renda fixa é mais segura, mas renda variável pode ter mais retorno. Quer que eu te explique melhor?"]
    ],

    [
        r"(?i)o que é CDI\??", 
        ["CDI é um índice de referência de juros no Brasil, muito usado em investimentos de renda fixa. Vale ficar de olho!"]
    ],

    [
        r"(?i)o que é CDB\??", 
        ["CDB é o Certificado de Depósito Bancário. Você empresta dinheiro para o banco e recebe de volta com juros. É uma forma comum de renda fixa!"]
    ],

    [
        r"(?i)o que é selic\??", 
        ["A Selic é a taxa básica de juros da economia brasileira. Ela influencia tudo: empréstimos, financiamentos e até a poupança."]
    ],

    [
        r"(?i)o que é renda fixa\??", 
        ["Renda fixa é um tipo de investimento onde você sabe (ou estima) quanto vai ganhar. Exemplos: Tesouro Direto, CDB, LCI."]
    ],

    [
        r"(?i)o que é renda variável\??", 
        ["É o tipo de investimento cujo retorno não é garantido, como ações ou criptomoedas. Pode ganhar muito... ou perder."]
    ],

    [
        r"(?i)qual investimento tem menos risco\??", 
        ["Normalmente, os de renda fixa como o Tesouro Selic. Mas lembre-se: risco baixo, retorno geralmente menor."]
    ],

    [
        r"(?i)investe em ações|ações são boas\??", 
        ["Ações podem ser ótimas no longo prazo. Mas é bom estudar o mercado e entender o seu perfil de investidor."]
    ],

    [
        r"(?i)o que é inflação\??", 
        ["Inflação é o aumento geral e contínuo dos preços. Com ela, o seu dinheiro perde poder de compra."]
    ],

    [
        r"(?i)qual o sentido da vida\??", 
        ["Fazer o dinheiro trabalhar pra você! E também: 42 😄"]
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
        r"(?i)vale a pena investir na poupança\??",
        ["A poupança é segura, mas rende pouco. Existem opções tão seguras quanto, com rendimentos melhores, como o Tesouro Selic."]
    ],

    
    [
        r"(?i)investimento de curto prazo\??",
        ["Para curto prazo, é bom investir em ativos de alta liquidez e baixo risco, como Tesouro Selic ou CDB com liquidez diária."]
    ],
    [
        r"(?i)o que é liquidez\??",
        ["Liquidez é a facilidade de transformar um investimento em dinheiro. Alta liquidez = resgate rápido."]
    ],

    [
        r"(?i)como funciona o tesouro direto\??",
        ["Você empresta dinheiro para o governo e recebe com juros depois. É uma das formas mais seguras de investir no Brasil."]
    ],

    [
        r"(?i)qual a diferença entre cdb e tesouro direto\??",
        ["Ambos são de renda fixa, mas o CDB é emitido por bancos e o Tesouro pelo governo. Tesouro tem mais segurança, CDB pode ter rentabilidade maior."]
    ],

    [
        r"(?i)o que é PIB\??",
        ["PIB é a soma de todos os bens e serviços produzidos no país. É uma forma de medir a economia."]
    ],

    [
        r"(?i)o que é taxa de juros\??",
        ["É o custo do dinheiro. Afeta empréstimos, financiamentos e até investimentos."]
    ],

    [
        r"(?i)o que é taxa básica de juros\??",
        ["É a taxa Selic! Ela é definida pelo Banco Central e influencia toda a economia."]
    ],

    [
        r"(?i)o que é câmbio|como funciona o câmbio\??",
        ["É a relação entre duas moedas, como real e dólar. O valor muda conforme a oferta e demanda."]
    ],

    [
        r"(?i)como economizar dinheiro\??",
        ["Anote seus gastos, corte supérfluos e defina metas de economia. Pequenas atitudes fazem diferença."]
    ],

    [
        r"(?i)como sair das dívidas\??",
        ["Organize suas dívidas, priorize as com maior juros e tente renegociar. Depois, monte uma reserva para emergências."]
    ],

    [
        r"(?i)o que é reserva de emergência\??",
        ["É um valor guardado para imprevistos, equivalente a 3 a 6 meses dos seus gastos mensais, em algo seguro e com liquidez."]
    ],

    [
        r"(?i)quanto devo guardar por mês\??",
        ["O ideal é guardar pelo menos 10% da sua renda. Se der mais, melhor ainda!"]
    ],

    [
        r"(?i)estou perdido|não sei por onde começar",
        ["Tudo bem, muita gente começa assim. Posso te guiar pelos primeiros passos do mundo financeiro. Vamos juntos!"]
    ],

    [
        r"(?i)o que são ações\??",
        ["Ações são pequenas partes de uma empresa. Ao comprar uma, você vira sócio e participa dos lucros (ou prejuízos)."]
    ],

    [
        r"(?i)o que são fundos imobiliários|FII\??",
        ["FIIs são fundos que investem em imóveis. Você ganha com aluguéis e valorização, sem precisar comprar imóveis diretamente."]
    ],

    [
        r"(?i)o que é day trade\??",
        ["É uma estratégia de compra e venda de ativos no mesmo dia. Pode dar lucro rápido, mas o risco é alto."]
    ],

    [
        r"(?i)renda passiva\??",
        ["Renda passiva é o dinheiro que entra sem você precisar trabalhar por ele, como aluguéis, dividendos ou juros de investimentos."]
    ],

    [
        r"(?i)dividendos\??",
        ["Dividendos são partes do lucro das empresas que são distribuídas aos acionistas. Uma forma de ganhar com ações sem vender."]
    ],

    [
        r"(?i)ETFs\??",
        ["ETFs são fundos que replicam índices como o Ibovespa. É uma forma prática e diversificada de investir em ações."]
    ],

    [
        r"(?i)o que é IPCA\??",
        ["O IPCA é o índice oficial da inflação no Brasil. Ele mede o aumento dos preços ao consumidor."]
    ],

    [
        r"(?i)o que é IGPM\??",
        ["O IGP-M é um índice de inflação usado para reajustar aluguéis e contratos. Ele pode variar bastante."]
    ],

    [
        r"(?i)taxa real x taxa nominal\??",
        ["A taxa nominal é a taxa 'bruta'. A real é descontada da inflação. O que importa mesmo é o quanto seu dinheiro ganha de verdade."]
    ],

    [
        r"(?i)como funciona a bolsa de valores\??",
        ["A bolsa é um ambiente onde ações e outros ativos são comprados e vendidos. Funciona pela lei da oferta e demanda."]
    ],

    [
        r"(?i)como funciona o home broker\??",
        ["É uma plataforma online que te permite comprar e vender ações por conta própria, direto do seu computador ou celular."]
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
        r"(?i)não entendo nada de finanças", 
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
        r"(?i)o que são ações\??",
        ["Ações são pequenas partes de uma empresa. Ao comprar uma, você vira sócio e participa dos lucros (ou prejuízos)."]
    ],

    [
        r"(?i)o que são fundos imobiliários|FII\??",
        ["FIIs são fundos que investem em imóveis. Você ganha com aluguéis e valorização, sem precisar comprar imóveis diretamente."]
    ],

    [
        r"(?i)o que é day trade\??",
        ["É uma estratégia de compra e venda de ativos no mesmo dia. Pode dar lucro rápido, mas o risco é alto."]
    ],

    [
        r"(?i)renda passiva\??",
        ["Renda passiva é o dinheiro que entra sem você precisar trabalhar por ele, como aluguéis, dividendos ou juros de investimentos."]
    ],

    [
        r"(?i)dividendos\??",
        ["Dividendos são partes do lucro das empresas que são distribuídas aos acionistas. Uma forma de ganhar com ações sem vender."]
    ],

    [
        r"(?i)ETFs\??",
        ["ETFs são fundos que replicam índices como o Ibovespa. É uma forma prática e diversificada de investir em ações."]
    ],

    [
        r"(?i)qual (meu|o) perfil de investidor\??",
        ["Existem 3 perfis principais:\n\n"
        "🟢 *Conservador*: busca segurança e prefere investimentos com baixo risco, como Tesouro Selic e CDBs.\n"
        "🟡 *Moderado*: aceita um pouco mais de risco, combina renda fixa com renda variável.\n"
        "🔴 *Arrojado*: busca altos retornos e tolera volatilidade, investe em ações, fundos e criptomoedas.\n\n"
        "Qual deles parece mais com você? "]
    ],

    [
        r"(?i)sou do perfil conservador|conservador",
        ["Como perfil conservador, o ideal é focar em segurança e liquidez.\n\n"
        "Sugestão: Tesouro Selic, CDBs com liquidez diária e fundos de renda fixa."]
    ],

    [
        r"(?i)tenho perfil conservador",
        ["Perfeito! Comece pelo Tesouro Direto (Selic) ou CDBs de bancos grandes. São seguros e rendem mais que a poupança."]
    ],

    [
        r"(?i)investidor conservador",
        ["Ótimo! Fundos de renda fixa, LCI/LCAs e Tesouro Selic são ótimos para esse perfil."]
    ],
    [
        r"(?i)sou do perfil moderado|moderado",
        ["Como investidor moderado, você pode diversificar.\n\n"
        "Ex: Tesouro IPCA, fundos multimercado e até ações de boas empresas."]
    ],

    [
        r"(?i)tenho perfil moderado",
        ["Excelente! Dá pra equilibrar segurança com algum risco. Misture renda fixa com renda variável aos poucos."]
    ],

    [
        r"(?i)investidor moderado",
        ["Fundos multimercado, debêntures e ETFs são boas opções pra quem quer mais rendimento com risco controlado."]
    ],

    [
        r"(?i)sou do perfil arrojado|arrojado",
        ["Você busca grandes retornos, mesmo com riscos maiores.\n\n"
        "Sugestão: ações, fundos de ações, criptomoedas e ETFs internacionais."]
    ],

    [
        r"(?i)tenho perfil arrojado",
        ["Legal! Lembre-se de manter uma reserva de emergência e investir com estratégia. Ações e cripto podem ser boas escolhas."]
    ],

    [
        r"(?i)investidor arrojado",
        ["Invista com foco no longo prazo. Diversifique em ações, fundos de investimento e novos mercados."]
    ],

    [
        r"(.*)\?", 
        [
            "Desculpe, não tenho uma resposta específica para essa pergunta.", 
            "Você pode reformular a pergunta.", 
            "Essa pergunta é um pouco fora da minha área, mas posso tentar te ajudar com outra coisa!",
            "Ainda não tenho uma resposta precisa pra isso. Quer tentar perguntar de outro jeito?"
        ]
    ],

    [
        r"(.*)", 
        [
            "Desculpe, não tenho uma resposta específica para essa pergunta.", 
            "Você pode reformular a pergunta.", 
            "Essa pergunta é um pouco fora da minha área, mas posso tentar te ajudar com outra coisa!",
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