![image](https://user-images.githubusercontent.com/56680251/110217904-8619d980-7e95-11eb-9978-89d5f4bd8224.png)
# Trabalho de Fundamentos de Ciência de Dados
Descrição e detalhamento do trabalho da disciplina de Fundamentos de Ciência de Dados.
Grupo composto por:
* Ana Vasconcelos
* Jivago Medeiros
* Rafael Escalfoni
* Silas Pereira
* Sírius Thadeu

## 1. Detalhamento e descrição do problema abordado:
Identificar qual o nível de protagonismo das mídias sociais nas eleições municipais do Rio de Janeiro. Adicionalmente, explorar qual a influência de tais plataformas sociais no resultado das eleições.

## 2. Descrição do dataset e sua fonte:
O dataset é composto por dados coletados do twitter sobre os candidatos à prefeitura do Rio de Janeiro. Os dados foram coletados utilizando a API oficial do Twitter no período entre 29/09/2020 à 01/12/2020.  
O dataset possui possui 3.3GB e possui 580.000 tweets que usaram em seu texto termos relacionados aos candidatos da época.  
Para mais detalhes sobre a proveniência do dataset, verificar a [seção 8](8-projeto-de-coleta-de-metadados-da-proveniência-dos-experimentos).

## 3. O quê pretendem fazer e o quê vão e como extrair (plano dos experimentos):
Os dados foram extraídos usando a API do twitter. Eles são retornados com base em termos pré-definidos e informados à API. Os termos utilizados combinam os nomes dos candidatos, o número de seu respectivo partido, a sigla do partido e o ano da eleição.
 
> [ {nomeCandidato} AND [ {numeroPartido} OR {siglaPartido} OR $ANO] ]

Os experimentos compreendem inicialmente uma seleção dos dados coletados, já que nem todas as informações serão úteis para as análises desejadas. Informações referentes ao texto descrito no tweet gerado e ao autor da postagem são de interesse dos experimentos.

Através da linguagem de programação python e suas principais bibliotecas para ciência de dados (como NumPy, Pandas, NLTK, Matplotlib, Seaborn, etc.) pretendemos explorar os dados anteriormente mencionados, realizando os tratamentos necessários para extrairmos as informações almejadas por esta pesquisa. Como estamos lidando com diversos tipos de dados distribuidos em colunas, cada coluna (ou conjunto de coluna com o mesmo tipo de dado) deverá passar por processos de extração e tratamento de dados distintos a fim de coletarmos as  informações necessárias.

Mais detalhes sobre o plano do experimento podem ser encontrados na [seção 7](#7-plano-do-experimento-a-ser-executado) deste documento.

## 4. Objetivos do Projeto:
### 4.1 Objetivo Geral:
* Identificar a relação entre as interações nas redes sociais (Twitter) e as eleições municipais de 2020 do Rio de Janeiro.
### 4.2 Objetivos Específicos:
* Analisar informações sobre o Perfil do usuário autor do tweet;
* Analisar a quantidade de menções aos candidatos;
* Análise de Sentimentos dos tweets;
* Análise Temporal dos tweets.

## 5. Métodos de data cleaning / tratamento de dados:
Em nosso projeto utilizaremos métodos de tratamento de dados voltados para cada tipo de dado encontrado e técnicas de processamento de texto (Atomização, Contagem de palavras, Divisão de frases, Radicalização, Normalização e Remoção das “stop words”) visando possibilitar uma análise textual automática, até mesmo realizando análise de sentimento quando possível.

No caso das colunas de tipos numéricos, verificaremos a existência de dados nulos ou NaN (Not a Number). Em caso positivo, de acordo com as regras descritivas da coluna em questão,  poderemos atribuir o valor padrão 0 (para as colunas onde a ocorrência desse valor não é possível naturalmente) ou o valor padrão negativo -1 (para as colunas onde a ocorrência de valores negativos não são possíveis naturalmente).

Já no caso das colunas tipo texto (String), verificaremos a existência de dados nulos e os substituiremos pela String vazia. Além disso, utilizaremos técnicas de processamento de texto para normalizar esses dados (uniformização das letras maiúsculas e minúsculas, remoção de acentuação, pontuação, caracteres inválidos, etc.).

Também poderemos utilizar métodos de detecção de outliers baseados em estatística, distância ou modelo, cada um sendo aplicado nos casos em que forem julgados mais aptos.
Para os dados textuais, o pré-processamento dos dados inclui:
* Nivelamento das palavras em minúsculas;
* Remoção de stopwords;
* Remoção de sufixos;
* Remoção dos atributos nulos;
* Remoção de atributos não relevantes;
* Identificação de outliers (tweets não relacionados ao contexto da Eleição, tweets inválidos/não úteis).

## 6. Apresentar a proposta de modelo de extração de conhecimento e visualização de dados que será adotado:
Em nosso projeto, poderemos utilizar alguns dos principais modelos de extração de conhecimento, quais sejam:
* Modelos estatísticos para descobrir padrões e construir modelos preditivos;
* Modelos de clusterização para agrupamento de dados, identificando dados semelhantes e não semelhantes entre si;
* Árvore de decisão, um modelo preditivo que forma um desenho que lembra uma árvore, cujas ramificações do modelo funcionam como métodos de classificação. A árvore de decisão é uma   técnica que permite a fácil interpretação dos dados e mostra o caminho a ser percorrido para alcançar determinado objetivo;
* Regras de associação, uma técnica que ajuda a encontrar associações entre dois ou mais itens. Ao definir relações entre as variáveis do dataset é possível descobrir padrões escondidos;
* Redes neurais, utilizadas com mais frequência nos estágios iniciais do processo de mineração de dados, servem para modelar relações entre os dados que entram e que saem do processo de mineração;
* Classificação, uma técnica que ajuda a obter informações importantes sobre dados e metadados. Está intimamente relacionada com a técnica de clusterização e utiliza a árvore de decisão ou rede neural;
* Visualização, técnicas utilizadas no início do processo de mineração de dados como um primeiro passo para descobrir padrões ocultos em um grande grupo de dados.

Quanto às técnicas de visualização de dados que poderão ser utilizadas em nossa pesquisa, histogramas e gráficos QQ permitem examinar a distribuição de uma única variável e gráficos  de dispersão mostram como duas variáveis estão relacionadas. Além disso, Boxplots são uma ótima ferramenta para visualizar valores fora de um determinado intervalo. Eles podem ser  estendidos com boxplots agrupados ou gráficos de violino que nos permitem comparar as distribuições entre subconjuntos de dados.

Gráficos de dispersão nos permitem obter uma noção das relações multivariadas, dentre outras coisas. Os histogramas também podem, às vezes, oferecer uma visão adicional se exibirmos  vários histogramas em um gráfico ou criarmos um histograma empilhado. Um mapa de calor pode ser gerado com base em uma matriz de correlação para nos auxiliar na análise do dataset.

Por fim, diversas outras técnicas de visualização de dados nos permite trabalhar de formas distintas com nosso dataset, cada uma com suas próprias vantagens:
* Histogramas permitem examinar a distribuição de variáveis contínuas;
* Boxplots permitem identificar outliers para variáveis contínuas;
* Boxplots Agrupados permitem descobrir valores inesperados em um determinado grupo;
* Gráficos de Violino permitem examinar a forma de distribuição e outliers;
* Gráficos de Dispersão permitem visualizar relações bivariadas;
* Gráficos de Linha permitem examinar tendências em variáveis contínuas.

## 7. Plano do experimento a ser executado:
Em nosso projeto usamos o Google Colab (https://colab.research.google.com/). O Google Colaboratory ou “Colab” permite escrever código Python diretamente no navegador, com fácil  compartilhamento e acesso gratuito a GPUs (e demais hardwares e softwares necessários). Nenhuma configuração extra é necessária para começar a trabalhar com essa ferramenta, exceto a instalação de algumas bibliotecas específicas do Python que porventura não estejam já instaladas no ambiente (e seja preciso utilizar durante o projeto), facilitando assim o trabalho de um cientista de dados.

O Google Colaboratory é construído sobre o Jupyter Notebook e fornece um ambiente interativo chamado notebook Colab que permite escrever e executar código (script Python). Os notebooks do Colab permitem combinar código executável e rich text em um só documento, além de imagens, HTML, LaTeX e muito mais. Os notebooks do Colab são armazenados na conta do Google Drive. É possível compartilhar os notebooks do Colab facilmente com outras pessoas e permitir que elas façam comentários ou até editem o documento. O Colab fornece completamentos automáticos para explorar atributos de objetos Python, bem como para visualizar rapidamente sua documentação.

É uma das ferramentas ideais para se trabalhar com Ciência de Dados, pois com o Colab podemos aproveitar todo o potencial das conhecidas bibliotecas Python para analisar e ver dados (numpy, matplotlib, pandas, etc.). É possível importar para os notebooks do Colab os dados de uma conta do Google Drive, do GitHub e de muitas outras fontes. Além disso, o Colab é altamente integrável com o Google Drive, permitindo montar um drive virtual para leitura e armazenamento perpétuo dos dados gerados pelos scripts Python (uma vez que o ambiente de execução do Colab é temporário, sendo “zerado” após longos períodos de inatividade do usuário – ou a pedido do próprio usuário). Os notebooks do Colab executam os códigos nos servidores em nuvem do Google, significando que podemos tirar proveito da potência de hardware do Google, como GPUs e TPUs, independentemente da potência do computador local, necessitando somente de um navegador (com acesso à internet).

Além do planejamento prévio descrito na [seção 3](#3-o-quê-pretendem-fazer-e-o-quê-vão-e-como-extrair-plano-dos-experimentos) deste documento, pretendemos usar também uma biblioteca de análise exploratória de dados chamada Sweetviz (https://pypi.org/project/sweetviz/). Ela pega os dataframes do pandas e cria um relatório HTML autocontido que pode ser visualizado em um navegador ou integrado em notebooks. Além de criar visualizações  perspicazes e bonitas com apenas duas linhas de código, ela fornece análises que levariam muito mais tempo para serem geradas manualmente, incluindo algumas que nenhuma outra biblioteca fornece tão rapidamente, como:
* **Análise de alvo:** mostra como um valor alvo (por exemplo, “Sobreviveu” no dataset do Titanic) se relaciona com outros recursos;
* **Comparações de dataset:** entre datasets (por exemplo, “Treino x Teste”) e intra-conjunto (por exemplo, “Homem x Mulher”);
* **Correlações / associações:** integração total de correlações e associações de dados numéricos e categóricos, tudo em um único gráfico e tabela.

Por fim, todos os scripts e artefatos desenvolvidos para este projeto estão disponíveis para acesso através do GitHub (https://github.com/FundamentosDataScienceEleicoesRJ2020/Sandbox).

## 8. Projeto de coleta de metadados da proveniência dos experimentos:
Para coletar os metadados de proveniência do dataset escolhido, descrito na [seção 2](#2-descrição-do-dataset-e-sua-fonte) deste documento, e gerar o respectivo grafo de proveniência  (mostrado abaixo) foi utilizada a biblioteca PROV do Python (https://pypi.org/project/prov/), em sua versão 2.0.0.  
TODO: imagem PROV

## 9. Projeto para tornar o experimento reprodutível:
Seguindo-se os preceitos dispostos em “Re-run, Repeat, Reproduce, Reuse, Replicate: Transforming Code into Scientific Contributions” (Fabien C. Y. Benureau e Nicolas P. Rougier), coletamos todas as informações necessárias de ambiente (Sistema Operacional e sua arquitetura; Linguagem de Programação e as bibliotecas utilizadas) para tornar o experimento reprodutível. Além disso, os scripts Python estão sendo criados com o maior zelo possível, visando documentar os passos executados durante todo o experimento e seguir as boas práticas de programação para tornar esses códigos reusáveis.

Também, durante toda a escrita do artigo será documentada a metodologia utilizada, bem como descritos os processos, algoritmos e modelos utilizados durante o projeto, visando assim   permitir que este experimento seja replicado por outros cientistas. A seguir, descrevemos as configurações de ambiente utilizadas durante este projeto.

Para o experimento, utilizamos a ferramenta Google Colab, que possui as seguintes configurações de ambiente de execução:
* Sistema Operacional Ubuntu 18.04.5 LTS (Bionic Beaver), com kernel Linux versão 4.19.112+ (Chromium OS versão 10.0.0) e arquitetura x86_64 (64-bit) com ordem de byte “Little  Endian” e dois processadores Intel® Xeon® de 2.20GHz cada;
* Python na versão 3.7.10 [GCC  7.5.0] e as bibliotecas Pandas versão 1.1.5, Beautiful Soup versão 4.6.3, PROV versão 2.0.0 e Sweetviz versão 2.0.9.

Mais informações sobre as configurações do ambiente utilizado durante o experimento podem ser visualizadas através do arquivo **Environment.conf**, disponível no GitHub (https://github.com/FundamentosDataScienceEleicoesRJ2020/Sandbox/tree/main/artefatos).
