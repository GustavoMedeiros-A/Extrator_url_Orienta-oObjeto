endereco = "Eua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"


import re # Regular Expression - RegEx


# 5 dígitos + hífen (opcional) + 3 dígitos

# Cria-se um padrão de busca para buscar, digamos, uma "substring".
# A "?" serve para dizer que o que vem antes pode, ou não, existir.
# A {} (chave) serve pra dizer quantas vezes o padrão deve se repetir.
# O hífen diz que o que está dentro do colchete vai de tal até tal (ex: 0 até 9 = 0-9).


# Usa-se seach() para buscar um padrão dentro de uma string inteira
# E o match() para verificar se aquela string inteira bate com aquele padrão


padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()  # group() serve para retornar todos as substring encontradas no "match".
    print(cep)