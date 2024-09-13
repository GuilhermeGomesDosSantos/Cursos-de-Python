# Utilizando o dicionário criado no item 1 (atividade 16):

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

pessoa = [{"nome": "Guilherme", "idade": 21, "cidade": "São Paulo"}]


pessoa[0]["idade"] = 22
pessoa[0]["profissão"] = "Programador"

del pessoa[0]["nome"]
print(pessoa)