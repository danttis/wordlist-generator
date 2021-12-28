# Wordlist Generator
Uma das grandes fraquezas dos ataques de força bruta são a quantidade de senhas necessárias
imagine uma senha de 5 caracteres nela misturada senhas e números e 10 caracteres especiais
para chegarmos a uma combinação correta teríamos que fazer todas as possibilidades,
para cada dígito da senha teríamos 26 letras minusculas + 26 letras maiúsculas+10 dígitos decimais + 10 caracteres especiais, imaginando que não podemos ter caracteres repetidos na senha teríamos 72 possibilidades para o primeiro termo 71 para o segundo, 70 para o terceiro, 69 para o quarto, 68 para o quinto, para sabermos o total de combinações 72x71X70x69x68, cerca de um bilhão e seiscentos e setenta e oito milhões e novecentos e oitenta e cinco mil e duzentos e oitenta, senhas diferentes.<br>
Agora imagine em situações de senhas de 20 ou 30 caracteres onde os termos podem se repetir, a lista de senhas ficaria gigantesca, a ponto de computadores comuns não suportarem.<br>
Pensando nisso criei esse script simples que criar lista de palavras a partir de palavras chaves, aumentando a eficácia no acerto da senha, essas mesmas podem ser encontradas em dados conhecidos do local a ser testado.
Não me responsabilizo pelo mal uso desse script, tudo aqui é open source, fique a vontade para copiar modificar e melhorar.
