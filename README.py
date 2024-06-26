#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `criar um novo link simbólico` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `criar um novo link simbólico` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/using the `criar um novo link simbólico` on `Linux Ubuntu`._
# 

# ## Revisão(ões)/Versão(ões)

# | Revisão número | Data da revisão | Descrição da revisão                                    | Autor da revisão                                |
# |:--------------:|:---------------:|:--------------------------------------------------------|:------------------------------------------------|
# | 0              | 22/03/2024      | <ul><li>Revisão inicial/criação do documento.</li></ul> | <ul><li>Eden Denis F. da S. L. Santos</li></ul> |
# 

# ## Descrição [2]
# 
# ### `link simbólico`
# 
# Um link simbólico, também conhecido como symlink, é um tipo especial de arquivo que aponta para outro arquivo ou diretório em um sistema de arquivos. Ao contrário de um hard link, que aponta diretamente para os dados do arquivo, um symlink contém o caminho para o arquivo ou diretório de destino. Isso oferece flexibilidade, permitindo que um mesmo arquivo ou diretório seja acessado por meio de diferentes caminhos. Os symlinks são úteis para criar atalhos ou simplificar a organização de arquivos em um sistema, facilitando o acesso e a manutenção.
# 

# ## 1. Como configurar/instalar/usar o `criar um novo link simbólico` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `criar um novo link simbólico` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes APT. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo APT e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.7 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.8 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 

# Para criar um novo link simbólico pelo terminal no Kali Linux ou em qualquer outro sistema Unix-like, você pode usar o comando ln com a opção -s. Aqui está um exemplo de como fazer isso:
# 
# 1. **Abra o Terminal:** Você pode abrir o terminal procurando por ele no menu de aplicações ou pressionando `Ctrl + Alt + T`
# 
# 2. **Use o comando `ln`:** A sintaxe geral para criar um link simbólico é: `ln -s [opções] /caminho/para/arquivo/original /caminho/para/link`
# 
#     Por exemplo, se você quiser criar um link simbólico para o arquivo `/usr/share/backgrounds/imagem.jpg` e quer que o link seja criado na área de trabalho, o comando seria: `ln -s /usr/share/backgrounds/imagem.jpg ~/Desktop/link_para_imagem.jpg`
# 
#     No exemplo acima, /usr/share/backgrounds/imagem.jpg é o caminho para o arquivo original e ~/Desktop/link_para_imagem.jpg é o caminho onde você quer criar o link simbólico.
# 
# 3. **Importante:** Lembre-se de substituir os caminhos de exemplo pelos caminhos reais dos seus arquivos.
# 
# Após executar o comando, o link simbólico será criado no local especificado e apontará para o arquivo original. Você pode verificar se o link foi criado corretamente com o comando `ls -l`, que mostrará o link e para onde ele aponta.
# 

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `criar um novo link simbólico` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há.
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Alterar Papel de Parede.*** Disponível em: <https://chat.openai.com/c/773185e2-0b63-40f5-9b4e-2df63d6f516a> (texto adaptado). Acessado em: 22/03/2023 17:11.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 22/03/2024 17:10.
# 
