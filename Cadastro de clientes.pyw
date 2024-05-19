import tkinter as tk

def cadastrar_cliente():
	cpf_cnpj = entrada_cpf_cnpj.get()
	nome = entrada_nome.get()
	endereco = entrada_endereco.get()
	bairro = entrada_bairro.get()
	cidade = entrada_cidade.get()
	estado = entrada_estado.get()
	uf = entrada_uf.get()
	telefone_fixo = entrada_telefone_fixo.get()
	telefone_celular = entrada_telefone_celular.get()

# Aqui você pode adicionar código para salvar os dados em algum lugar
# por exemplo, em um banco de dados

# Cria uma root
root = tk.Tk()
root.title('Cadastro de Clientes')
root.geometry('250x230')
root.resizable('False', 'False')

# Labels
tk.Label(root, text="CPF/CNPJ:").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Nome:").grid(row=1, column=0, sticky="w")
tk.Label(root, text="Endereço:").grid(row=2, column=0, sticky="w")
tk.Label(root, text="Bairro:").grid(row=3, column=0, sticky="w")
tk.Label(root, text="Cidade:").grid(row=4, column=0, sticky="w")
tk.Label(root, text="Estado:").grid(row=5, column=0, sticky="w")
tk.Label(root, text="UF:").grid(row=6, column=0, sticky="w")
tk.Label(root, text="Telefone Fixo:").grid(row=7, column=0, sticky="w")
tk.Label(root, text="Telefone Celular:").grid(row=8, column=0, sticky="w")

# Campos de entrada
entrada_cpf_cnpj = tk.Entry(root, width=24)
entrada_cpf_cnpj.grid(row=0, column=1)

entrada_nome = tk.Entry(root, width=24)
entrada_nome.grid(row=1, column=1)

entrada_endereco = tk.Entry(root, width=24)
entrada_endereco.grid(row=2, column=1)

entrada_bairro = tk.Entry(root, width=24)
entrada_bairro.grid(row=3, column=1)

entrada_cidade = tk.Entry(root, width=24)
entrada_cidade.grid(row=4, column=1)

entrada_estado = tk.Entry(root, width=24)
entrada_estado.grid(row=5, column=1)

entrada_uf = tk.Entry(root, width=24)
entrada_uf.grid(row=6, column=1)

entrada_telefone_fixo = tk.Entry(root, width=24)
entrada_telefone_fixo.grid(row=7, column=1)

entrada_telefone_celular = tk.Entry(root, width=24)
entrada_telefone_celular.grid(row=8, column=1)

# Botão de cadastro
botao_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_cliente)
botao_cadastrar.grid(row=9, column=1, pady=10)

# Loop principal
root.mainloop()