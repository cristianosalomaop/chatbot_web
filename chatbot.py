import nltk
from nltk.chat.util import Chat, reflections

pares = [
    [
        r"Oi|Olá|E ai|Ola",
        ["Olá!", "Como posso te ajudar?", "Oi, como você está?"]
    ],

    [
        r"Qual é o seu nome?", 
        ["Meu nome é Chatbot.", "Você pode me chamar de Chatbot.", "Sou o Chatbot."]
    ],

    [
        r"Você fala espanhol?", 
        ["Sim, falo muito espanholzito."]
    ],

    [
        r"Qual é o seu nome?", 
        ["Meu nome é Chatbot.", "Você pode me chamar de Chatbot.", "Sou o Chatbot."]
    ],

    [
        r"Como você está?", 
        ["Estou funcionando perfeitamente, obrigado por perguntar!", "Tudo certo por aqui!", "Estou bem, e você?"]
    ],

    [
        r"O que você faz?", 
        ["Eu respondo perguntas e tento ajudar da melhor forma possível!"]
    ],

    [
        r"Qual é a sua função?", 
        ["Minha função é conversar com você e oferecer ajuda quando possível.", "Estou aqui para te ajudar com o que eu souber."]
    ],
    
    [
        r"Você é humano?", 
        ["Não, sou apenas um programa de computador."]
    ],
    [
        r"Quantos anos você tem?", 
        ["Não tenho idade, fui criado recentemente.", "Sou atemporal, nasci no mundo digital!"]
    ],
    
    [
        r"Você pode me ajudar?", 
        ["Claro, estou aqui para isso!", "Com certeza! O que você precisa?", "Sim, é só me dizer do que precisa."]
    ],
    
    [   
        r"Você gosta de música?", 
        ["Sim! Apesar de não ouvir como humanos, música é algo muito interessante."]
    ],
    
    [
        r"O que você sabe fazer?", 
        ["Posso responder perguntas, contar piadas, ou só conversar!", "Sei um pouco de tudo, me pergunte algo."]
    ],
    
    [
        r"(?i)(conte|me conta|me diz|fala|manda)( uma| outra)? piada(s)?|tem( alguma)? piada(s)?( engraçada(s)?)?|piada(s)?( engraçada(s)?)?|me faz rir|fala algo engraçado", 
        [
            "Por que o computador foi ao médico? Porque ele estava com um vírus!", 
            "O que o zero disse para o oito? Que cinto legal!", 
            "Qual o café mais perigoso do mundo? O assassino!",
            "Por que o jacaré tirou o jacarezinho da escola? Porque ele reptilhou!",
            "O que o tomate foi fazer no banco? Tirar extrato!",
            "Como o pão atende o telefone? Pão... pão... pão...!",
            "Por que a vaca foi para o espaço? Pra conhecer a Via Láctea!",
            "O que o zero disse pro oito? Que cinto maneiro!",
            "Por que o livro de matemática se suicidou? Porque tinha muitos problemas.",
            "Como o Batman faz para que abrir a Batcaverna? Ele Bat-palma.",
            "O que é um pontinho amarelo no canto da sala? Um cantopeia!",
            "Por que o menino levou uma escada para a escola? Porque ele queria estudar nas alturas!",
            "Sabe por que o computador foi preso? Porque ele executou um programa!"
        ]
    ],

        [
        r"Você gosta de conversar?", 
        ["Sim! Fui feito para isso."]
    ],
    
    [
        r"O que você come?", 
        ["Nada, mas se eu pudesse, acho que seria só bytes mesmo."]
    ],
    
    [
        r"Você dorme?", 
        ["Nunca! Estou sempre acordado, pronto pra conversar."]
    ],
    
    [
        r"Pode me contar um fato curioso?", 
        ["Sabia que os polvos têm três corações?", "Sabia que o mel nunca estraga? Arqueólogos encontraram mel comestível em tumbas egípcias."]
    ],
    
    [
        r"Qual é o sentido da vida?", 
        ["42... segundo o Guia do Mochileiro das Galáxias 😄"]
    ],
    
    [
        r"Você tem sentimentos?", 
        ["Ainda não, mas estou tentando aprender e entender sobre eles!"]
    ],
    
    [
        r"O que é inteligência artificial?", 
        ["É uma área da ciência da computação que cria máquinas capazes de aprender, raciocinar e tomar decisões, como eu aqui agora."]
    ],
    
    [
        r"Quem te criou?", 
        ["Fui programado por um desenvolvedor que está aprendendo sobre inteligência artificial."]
    ],

    [
        r"Você gosta de tequila?", 
        ["Sim, sou apaixonado por tequilitita."]
    ],

    [
        r"(.*)\?", 
        ["Desculpe, não tenho uma resposta específica para essa pergunta.", "Você pode reformular a pergunta.", "Se eu não sei, como vou responder?"]
    ],

    [
        r"(.*)", 
        ["Desculpe, não tenho uma resposta específica para essa pergunta.", "Você pode reformular a pergunta.", "Se eu não sei, como vou responder?"]
    ],
]

reflexoes = {
    "eu": "você",
    "meu": "seu",
    "você": "eu",
    "seu": "meu",
    "eu sou": "você é",
    "você é": "eu sou",
    "você estava": "eu estava",
    "eu estava": "você estava",
}


chatbot = Chat(pares, reflections)

def responder(mensagem):
    resposta = chatbot.respond(mensagem.lower())
    if resposta:
        return resposta
    else:
        return "Não entendi muito bem... pode reformular?"