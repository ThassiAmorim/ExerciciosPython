
import customtkinter

def clique():
    print("logar")

janela = customtkinter.CTk()
janela.geometry("400x200")

texto = customtkinter.CTkLabel(janela, text="Login")
texto.pack(padx=10, pady=10)


email = customtkinter.CTkEntry(janela, placeholder_text="Digite seu email")
email.pack(padx=10, pady=2)

senha = customtkinter.CTkEntry(janela, placeholder_text="Digite sua senha", show='*')
senha.pack(padx=10, pady=2)

botao = customtkinter.CTkButton(janela, text="Logar", command=clique)
botao.pack(padx=10, pady=10)



janela.mainloop()
