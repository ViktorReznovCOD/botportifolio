import telebot, requests
from io import BytesIO
user = 'ViktorReznovCOD'
url_users = "http://api.github.com/users/"
tokengit="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" # 06/11...dura 7 dias
tokenBot='6973468825:AAFFi385adbJPZiTvo3NXG5OHZ44COpLeNM' ## var 'tokenBot' recebe o token da API, em seguida é passada como parâmetro na criação do objeto 'bot', que recebe telebot.Telebot(tokenBot)
bot = telebot.TeleBot(tokenBot)

@bot.message_handler(commands=['github','Github'])
def f_github(message):
    response = requests.get(f"{url_users}{user}")
    resposta = response.json()
    #bot.reply_to(message,f"Avatar {resposta['avatar_url']}")
    bot.reply_to(message,f" Meu perfil no github 😎\n\n Clique aqui para me visitar: {resposta['html_url']}\n")
@bot.message_handler(commands=['linkedin','Linkedin'])
def f_linkedin(message):
    bot.reply_to(message,'Infelizmente não desenrolei ainda uma apresentação do linkedin mais maneira... então vai essa por enquanto:\nhttps://linkedin.com/in/araujofelipe97/')
# URL dos repositórios: http://www.api.github.com/users/{user}
# a ideia é consumir as informações do meu git, pro bot responder em conversa....
@bot.message_handler(commands=['repositorios'])
def repo_git(message):
    response_repo=requests.get(f"{url_users}{user}")
    resposta = response_repo.json()
    print("USUÁRIO",resposta['login'])
@bot.message_handler(commands=['help','ajuda'])
def help_command(message):
    msg_ajuda = "COMANDOS\n '/github'\n'/linkedin'"
    bot.reply_to(message,f'{msg_ajuda}')
# Passar mensagem geral:
#   dento do @bot.message_handler(), adicionar o codigo "func=lambda message:True"
@bot.message_handler(func=lambda message:True)
def mensagedefault(message):
    response = requests.get(f'{url_users}ViktorReznovCOD') # aqui eu faço uma request na pagina da api
    resposta = response.json() # uso json nos dados
    url_avatar = resposta["avatar_url"]  #aqui eu guardo o valor da chave 'avatar_url' dentro da variavel 'url_avatar'
    img = requests.get(url_avatar) # aqui eu guardo o valor de 'url_avatar' (a imagem) dentro da var 'img'
    imgembytes = BytesIO(img.content)
    bot.send_photo(message.chat.id,imgembytes) # aqui vou enviar a fotinha de perfil
    bot.send_message(message.chat.id,f'Olá! bem vindos ao meu bot de porfólio do Felipe Araújo 😊🤝\n\n Sinta-se a vontade para interagir com alguns comandos. Para visualizar os comandos, digite /ajuda')
    
bot.infinity_polling()