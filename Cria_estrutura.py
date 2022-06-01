# %%
import os
import sys

# %%
print('Bem-vindo!')

# %%
#Verificando diretório atual
print("Diretório inicial:\n", os.getcwd())

#Criando pasta principal do projeto
print('\nEscolha o nome do projeto. \nO diretório principal terá o mesmo nome.')   
pasta = input('Informe o nome do projeto: ')   
caminho = os.path.join(os.getcwd(), pasta) 

#Verificando se o diretório já existe
try:
    os.makedirs(caminho)
except:
    print('\nEste diretório já existe.\nNenhuma outra pasta foi criada. Tente novamente.\nFim.')
    #sys.exit()
else:
    print(f'\Diretório criado: \n {os.getcwd() + os.sep + pasta} ')

# %%
#Entrando na pasta principal do projeto
diretorio_projeto = os.getcwd() + os.sep + pasta
os.chdir(diretorio_projeto)

# %%
print("Diretório do projeto: \n", os.getcwd())

# %%
#Dicionário com os nomes das pastas a serem criadas
pastas_dic = {'dados':'arquivos utilizados no projeto que não serão armazenados no banco de dados.Exemplo: arquivos temporários, arquivos com resultado final de trabalhos, arquivos de fontes externas, etc...', \
              'docs':'documentação relevante, coletada ou produzida, a respeito do domínio e négócios abrangidos pelo trabalho.', \
              'notebooks':'cadernos Jupyter e outros arquivos para exploração dos dados, experimentos, etc...', \
              'relatorios':'relatórios produzidos e outras peças de documentos gerados do contexto do do projeto.'}

#Dicionário com os nomes das subpastas da pasta dados
sub_pastas_dic = {'original': 'subdiretório de dados. Guarda arquivos originais recebidos.', \
                  'tmp':'subdiretório de dados. Guarda arquivos de uso temporário.', \
                  'final': 'subdiretório de dados. Guarda arquivos finais gerados pelo projeto.'  }

# %%
#Lista de pacotes básicos sugeridos
pacotes_lista = ['pandas', 'numpy', 'matplotlib', 'mlflow']

# %%
#Criando pastas do projeto
for k in pastas_dic.keys():
    os.mkdir(k)

#Criando subpastas da pasta dados
for k in sub_pastas_dic.keys():
    os.mkdir('dados' + os.sep + k)

# %%
while True:

    pergunta = input('Deseja criar um ambiente virtual agora? (S para sim ou N para não): ') 

    if  (pergunta == 'S') or (pergunta == 's'):
        
        #Instalando pacote virtualenv
        print('\nInstalando virtualenv no python')
        os.system('pip install virtualenv')
        print('virtualenv instalado')

        #Criando ambiente virtual
        venv = input('Informe o nome ambiente virtual que deseja usar: ')  
        print(f'\nCriando virtualenv {venv}')
        os.system(f'virtualenv {venv}')
        print(f'virtualenv {venv} criado')

        #Instalando pacotes básicos
        for pacote in pacotes_lista:
            print(f'Instalando {pacote}')
            os.system(f'pip install {pacote}')
        print('Pacotes instados')
        
        break

    elif (pergunta == 'N') or (pergunta == 'n'):

        print('Ambiente não foi criado. ')
        break

    else:

        print('Não entendi sua resposta.\nDeseja criar um ambiente virtual agora? (S para sim ou N para não) ')
        continue


# %%
print('\n\nResumo:\n')
print('Diretórios criados:')
for k,v in pastas_dic.items():
    print(f'- Diretório {k}: {v}')
    if k == 'dados':
        for k2,v2 in sub_pastas_dic.items():
            print(f'  - Subdiretório {k2}: {v2}')


print('\nAmbiente virtual:')

if (pergunta == 'S') or (pergunta == 's'):
    print(f'Ambiente virtual {venv} criado')
    print('Pacotes instalados:')
    for pacote in pacotes_lista:
        print(f'- {pacote}')       
    
    #Ativa o ambiente virtual de acordo com o sistema operacional
    print('\nPara ativar o ambiente virtual no seu sistema operacional,\nvá para a pasta do projeto e utilize o comando abaixo:')
    #Windows
    if sys.platform.startswith('win32'):        
        print(f'{venv}\Scripts\Activate')
    #Linux ou MacOS
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        print(f'{venv}/bin/activate')
    else: 
        print('Ainda não temos suporte para o seu sistema operacional.')  
        
else:
    print('- Não foi criado um ambiente virtual. Se desejar criar, siga as instruções deste site: ')
    print('https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv\n')
      


