from tkinter import *
from customtkinter import CTkScrollableFrame
from os.path import join, abspath,dirname
from PIL import Image, ImageTk
from tkinter import font

caminho = dirname(abspath(__file__))
print(caminho)



tela = Tk()

tela.geometry("1366x768")
tela.configure(bg='black')
tela.resizable(False,False)

animado = join(caminho,'images',"meio_animado.jpg")
meio_animado = join(caminho,'images',"animado.jpg")

animado = Image.open(animado).resize((95,95)) # Essa imagem deve ser usada ao apertar o botão de busca
animado = ImageTk.PhotoImage(animado) # avatar.configure(image=meio_animado)

meio_animado = Image.open(meio_animado).resize((95,95)) # Essa é a imagem inicial e precisa ser vinculada ao usuario começar a digitar na "entry_buscar"
meio_animado = ImageTk.PhotoImage(meio_animado) # usando bind.

textao = 'Doli1\ndoli3\ndoli4\ndoli5\ndoli6\ndoli7\ndoli8\ndoli9\ndoli10'
procurando = "Aguarde um pouco, estou procurando pelas melhores recomendações" #Isso será usado para trocar o texto do topo após clicar no botão
#usando o --> apresentar .configure(text=procurando)
aguardando = "Me dê um exemplo de anime, irei procurar e te mostrar recomendações excelentes" # retorna ao normal ao cliente clicar dentro da Text

frame_a = Frame(tela,bg="#7b7b7b")
frame_a.place(relx=0.02,rely=0.05,relheight=0.3,relwidth=0.96)

apresentar = Label(frame_a,bg="#7b7b7b",text="Me dê um exemplo de anime, irei procurar e te mostrar recomendações excelentes",font=("Palatino Linotype",16))
apresentar.grid(row=0,column=0,columnspan=3)

avatar = Label(frame_a,image=animado, bg="#918134") # Aqui é a carinha do avatar, ela deve mudar conforme o click no botão ou no click da entry
avatar.grid(row=1,column=0,padx=10)

# Criar a fonte com um tamanho maior
fonte_maior = font.Font(size=14)  # Definir o tamanho da fonte como 14

entry_buscar = Text(frame_a,font=("Arial",20),height=3,width=74,wrap='word') # Aqui é onde o usuario digita a procura por indicação
entry_buscar.grid(row=1,column=1,sticky='nswe')

entry_buscar.insert("1.0",textao)
entry_buscar.bind("<Button-1>",avatar.configure(image=animado))

confirmar_busca = Button(frame_a,text="Encontrar",bg="#f4ab55",height=5) # esse é o botão que clica e envia os dados pro frame_b
confirmar_busca.grid(row=1,column=2,padx=10,sticky='nswe')


textao_da_busca = Text(tela,bg=None,font=("Palatino Linotype",16))
textao_da_busca.place(relx=0.02,rely=0.36,relheight=0.6,relwidth=0.96)
textao_da_busca.insert("1.0",textao)


tela.mainloop()