from Src import Tela
from Src import create_model, use_model

modelo = create_model()


tela = Tela(use_model,modelo)

tela.mainloop()