import customtkinter as ctk
import hashlib as h
from time import sleep

is_main = __name__ == "__main__"

def animar_entrada(janela, velocidade=10):
    """Animação de entrada deslizando da direita para a esquerda"""
    largura = janela.winfo_width()
    x_inicial = janela.winfo_screenwidth()
    x_final = x_inicial - largura - 20

    for x in range(x_inicial, x_final, -velocidade):
        janela.geometry(f"+{x}+20")
        janela.update()
        sleep(0.01)

def animar_saida(janela, velocidade=10):
    """Animação de saída deslizando para a direita"""
    x_inicial = janela.winfo_x()
    largura = janela.winfo_screenwidth()
    
    for x in range(x_inicial, largura, velocidade):
        janela.geometry(f"+{x}+20")
        janela.update()
        sleep(0.01)
    janela.destroy()

def mostrar_conquista(titulo="Título", descricao="Descrição", texto_icone="🎮"):
    """Mostra uma notificação de conquista com animação"""
    # Cria a janela fora da tela (à direita)

    
    popup = ctk.CTk()
    popup.title("Achievement PopUp")
    popup.overrideredirect(1)
    
    popup.attributes('-topmost', True)
    popup.geometry(f"300x80+{popup.winfo_screenwidth()}+20")  # Largura x Altura + X + Y

    # Ícone
    icone = ctk.CTkLabel(
        popup,
        text=texto_icone, 
        text_color='gold',
        font=('Arial', 44),
        width=50, height=50
    )
    icone.place(x=20, y=10)
    
    # Textos
    ctk.CTkLabel(
        popup, 
        text=titulo, 
        text_color='white',
        font=('Arial', 15, 'bold'),
        anchor='w',
        width=200
    ).place(x=80, y=15)
    
    ctk.CTkLabel(
        popup, 
        text=descricao, 
        text_color='lightgray',
        font=('Arial', 12),
        anchor='w',
        width=200
    ).place(x=80, y=35)
    
        # Mostra a janela com animação
    popup.after(100, lambda: animar_entrada(popup))
    
    # Fecha após 3 segundos com animação
    popup.after(3000, lambda: animar_saida(popup))
    popup.mainloop()

def criar_login(usuario_correto="admin", textos=["Login", "Usuario", "Senha", "Entrar", "Sucesso", "Login realizado!"]):
    def verificar():
        # Hash the input password for comparison
        with open("assets/user.json","r") as f:
            user_data= f.read()
        input_hash = h.sha384(entrada_senha.get().encode('utf-8')).hexdigest()
        if entrada_usuario.get() == usuario_correto and input_hash == user_data[0]['password_384']:
            mostrar_conquista(textos[4], textos[5])
            return 1
        else:
            mostrar_conquista("Erro", "Dados incorretos")
            return 0

    # Configuração da janela
    janela = ctk.CTk()
    janela.title(textos[0])
    janela.geometry("350x250")
    
    # Frame principal
    frame = ctk.CTkFrame(janela)
    frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    # Elementos da interface
    ctk.CTkLabel(frame, text=f"{textos[1]}:").pack(pady=5)
    entrada_usuario = ctk.CTkEntry(frame, width=200)
    entrada_usuario.pack(pady=5)
    
    ctk.CTkLabel(frame, text=f"{textos[2]}:").pack(pady=5)
    entrada_senha = ctk.CTkEntry(frame, show="*", width=200)
    entrada_senha.pack(pady=5)
    
    ctk.CTkButton(frame, text=textos[3], command=verificar, fg_color="gold", text_color= "black").pack(pady=10)
    
    # Focar no campo de usuário
    entrada_usuario.focus()

    janela.mainloop()

if is_main:
    criar_login()
    mostrar_conquista("Conquista Desbloqueada!", "Você completou o desafio!", "🏆")