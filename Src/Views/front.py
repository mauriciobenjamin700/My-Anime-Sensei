from tkinter import Label, Button, Text, Frame, Tk
from os.path import join, abspath,dirname
from PIL import Image, ImageTk
from tkinter import font

caminho = dirname(abspath(__file__))
print(caminho)


class Tela(Tk):
    def __init__(self,buscar_animes,model):
        super().__init__()

        self.geometry("1366x768")
        self.configure(bg='black')
        self.resizable(False,False)
        self.model = model
        self.buscar_animes = buscar_animes
        animado = join(caminho,'images',"animado.jpg")
        meio_animado = join(caminho,'images',"meio_animado.jpg")

        animado = Image.open(animado).resize((95,95)) # Essa imagem deve ser usada ao apertar o botão de busca
        self.animado = ImageTk.PhotoImage(animado) # avatar.configure(image=meio_animado)

        meio_animado = Image.open(meio_animado).resize((95,95)) # Essa é a imagem inicial e precisa ser vinculada ao usuario começar a digitar na "entry_buscar"
        self.meio_animado = ImageTk.PhotoImage(meio_animado) # usando bind.


        aguardando = "Me dê um exemplo de anime, irei procurar e te mostrar recomendações excelentes" # retorna ao normal ao cliente clicar dentro da Text
        self.textao = ""
        procurando = "Aguarde um pouco, estou procurando pelas melhores recomendações" #Isso será usado para trocar o texto do topo após clicar no botão
        encontrado = "Espero que goste de minhas recomendações!" # Deve ser implantado no final do código que esta executando a coleta de dados e inserindo no Text
        #usando o --> self.apresentar .configure(text=procurando)




        self.frame_a = Frame(self,bg="#7b7b7b")
        self.frame_a.place(relx=0.02,rely=0.05,relheight=0.3,relwidth=0.96)

        self.apresentar = Label(self.frame_a,bg="#7b7b7b",text="Me dê um exemplo de anime, irei procurar e te mostrar recomendações excelentes",font=("Palatino Linotype",16))
        self.apresentar.grid(row=0,column=0,columnspan=3)

        self.avatar = Label(self.frame_a,image=self.animado, bg="#918134") # Aqui é a carinha do avatar, ela deve mudar conforme o click no botão ou no click da entry
        self.avatar.grid(row=1,column=0,padx=10,rowspan=1)

        self.entry_buscar = Text(self.frame_a,font=("Arial",20),height=3,width=74,wrap='word') # Aqui é onde o usuario digita a procura por indicação
        self.entry_buscar.grid(row=1,column=1,sticky='nswe')

        self.entry_buscar.bind("<Button-1>",self.avatar.configure(image=self.meio_animado))

        self.confirmar_busca = Button(self.frame_a,text="Encontrar",bg="#f4ab55",height=5,command=self.disparar_busca) # esse é o botão que clica e envia os dados pro frame_b
        self.confirmar_busca.grid(row=1,column=2,padx=10,sticky='nswe')


        self.textao_da_busca = Text(self,bg=None,font=("Palatino Linotype",16))
        self.textao_da_busca.place(relx=0.02,rely=0.36,relheight=0.6,relwidth=0.96)

        self.textao_da_busca.insert("1.0",self.textao)


    def disparar_busca(self):
        text = self.entry_buscar.get("1.0", "end-1c")
        if len(text)> 0:
            self.textao = self.buscar_animes(text,self.model)
            self.textao_da_busca.insert("1.0",self.textao)


if __name__=="__main__":
    tela = Tela()
    tela.title("Recomendações")
    tela.mainloop()