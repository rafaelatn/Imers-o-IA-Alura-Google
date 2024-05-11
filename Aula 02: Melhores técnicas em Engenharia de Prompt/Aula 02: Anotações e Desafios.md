#### [↩Voltar para o Início](https://github.com/rafaelatn/Imersao-IA-Alura-Google/tree/main?tab=readme-ov-file)
## 📝Minhas anotações - 07/05/24
## 1. Sobre os prompts
Prompt = comando. Seja claro com suas instruções para a IA. Quanto mais específico seu prompt, melhor será a resposta dada. 

## 2. Alucinação
A alucinação da IA acontece quando não há um bom direcionamento para a tarefa solicitada. Existe duas situações de alucinação: 

1. **Grafo da IA forte (muita informação aprendida sobre o tema do comando) para pouco prompt.** Exemplo: Perguntar para IA qual foi o primeiro elefante a pisar na Lua. A resposta conterá fatos verídicos sobre o evento misturados com fictícios, inventados para preencher os "furos" da realidade.
2. **Grafo da IA fraco (pouca informação aprendida sobre o tema do comando) para prompt robusto.** Exemplo: Perguntar sobre a vida de uma subcelebridade, talvez conhecida na sua região, mas, não mundialmente.

### Nestes casos, a solução será pedir a *justificativa* das respostas dadas.

## 3. Tipos de Prompt

>🚨 Serão exemplificados nos desafios.

### Zero-shot-Prompting
É o comando que não possui nenhuma referência de como a resposta deve ser gerada. 

### Few-shot-Learning
É o comando que possui alguma referência para a geração da resposta. Quando utilizamos esta estratégia de prompt, mostramos para a IA, com dados irrelevantes para o verdadeiro projeto, o estilo de comando a ser feito e também o padrão de resposta desejada.

### Chain-of-Thought
A cadeia de pensamento será construída no momento de escrita do comando, em que a tarefa será dividida em partes menores e detalhada  passo a passo, como o raciocínio humano faz diariamente.

### Least-to-Most-Prompting
Aqui, o prompt com a problemática será dividido pela própria IA, que solucionará das menores para as maiores tarefas.

### Self Consistency
Quando os dados necessitam de uma precisão maior, enviamos o mesmo prompt várias vezes para gerar diversas respostas e então pedimos para que a IA avalie a sua consistência.

--- 

# 👩🏼‍💻 Desafio 01
>### "Utilizar o Few-shot-Learning e o Chain-of-Thought para um problema do seu cotidiano".

# Prompt Few-shot-Learning
Para a técnica do "Few-shot-Learning", exemplifiquei para o Gemini (versão 1.5 Pro disponível no Google IA Studio) como queria que os textos que leio para treinar minha leitura em coreano fossem traduzidos:

```
Coreano:안녕하세요! 민준입니다. 21 살이에요. 저는 부산에 태어났는데 서울에 살아요. 브라질을 만나고 싶어요. 브라질은 너무 아름답잖아요.저는 포르투갈어를 공부하지만 너무 어렵고 달라요. 아직 포르투갈어를 못해요.
Português: Olá! Sou Minjun. Tenho 21 anos. Eu nasci em Busan, mas moro em Seoul. Quero conhecer o Brasil. O Brasil é muito bonito.Eu estou estudando português, mas é muito difícil e diferente. Ainda não consigo falar português.

Coreano: 숲에서 토끼가 산책하고 있어요. 그는 그의 친구들을 봤어요. 그는 배가 고파서 정원에서 그는 당근과 딸기를 먹었어요. 그는 나무에서 새들이랑 노래해요. 푸른색 호수에서 그와 물고기들은 수영해요. 긴 하루였어요! 오늘 밤 그는 푹 잘 거예요.	
Português: O coelho está caminhando pela floresta. Ele encontrou seus amigos. Como estava com fome, comeu uma cenoura e um morango do jardim. Perto da árvore, ele cantou com os pássaros. No lago azul, ele nadou com os peixes. Foi um dia longo! Ele vai dormir muito bem esta noite.

Coreano: 산골 마을에 홀어머니와 오누이가 살고 있었다.하루는 어머니가 산 너머에 있는 잔칫집에 일을 하러 갔다.어머니가 일을 마치고 돌아오는데 어디선가 커다란 호랑이가 나타났다.
Português:
```
# Resposta

Português: Uma mãe viúva e seus dois filhos viviam em uma aldeia nas montanhas. Um dia, a mãe foi trabalhar em uma festa do outro lado da montanha. Quando a mãe estava voltando do trabalho, um grande tigre apareceu de algum lugar.

---
# Prompt Chain-of-Thought

Tendo o mesmo problema do meu cotidiano em mente (tradução de textos em idiomas diferentes), utilizei a técnica "Chain-of-Thought" para explicar, passo a passo, o que queria que fosse feito com o trecho de uma história coreana.

```
옛날 어느 마을에 가난한 노부부가 살고 있었다.이 부부에게는 자식이 없었다.어느 날 할아버지는 산에 갔다.산에서 나무를 했다.
한참 나무를 한 후에 할아버지는 힘들어서 쉬고 있었다.그 때 새 소리가 들려왔다.할아버지는 새를 잡고 싶어서 그 새를 따라갔다.
깊은 숲속으로 그 새를 따라갔다.할아버지는 목이 말랐다.곧 샘물을 찾았다.물을 마시자마자 할아버지는 잠이 들었다.
1- Analise o texto acima;
2- Traduza para o português e o inglês;
3- Crie, em português, uma tabela com os principais tópicos exibidos na história;
4- Identifique o nível necessário para a sua total compreensão e considerações finais.
```
# Resposta

## Análise do Texto

**1. Análise**
O texto apresenta uma narrativa em coreano que parece ser o início de um conto tradicional. Elementos como um casal de idosos sem filhos e um cenário rural sugerem um contexto folclórico. A narrativa introduz um conflito potencial ao colocar o personagem principal (o avô) em uma situação inesperada, adormecendo após beber água de uma fonte misteriosa na floresta.

**2. Traduções**

*Português:*
> Era uma vez, em uma certa vila, um velho casal pobre que vivia. Este casal não tinha filhos.
Um dia, o avô foi para a montanha. Ele cortou lenha na montanha. Depois de cortar lenha por um tempo, o avô estava cansado e descansando. Naquele momento, ele ouviu o som de um pássaro. O avô queria pegar o pássaro, então ele o seguiu.
Ele o seguiu até a floresta profunda. O avô estava com sede. Logo ele encontrou uma fonte. Assim que bebeu a água, o avô adormeceu.

*Inglês:*
> Once upon a time, in a certain village, there lived a poor old couple. This couple had no children. One day, the grandfather went to the mountain. He chopped wood in the mountain. After chopping wood for a while, the grandfather was tired and resting. At that moment, he heard the sound of a bird. The grandfather wanted to catch the bird, so he followed it. He followed it deep into the forest. The grandfather was thirsty. Soon he found a spring. As soon as he drank the water, the grandfather fell asleep.
> 
**3. Tabela de Tópicos**
   
| Tópico | Descrição |
|--------|-----------|
|Cenário | Vila rural|
| Personagens	| Casal de idosos sem filhos |
|Conflito |	Avô adormece após beber água de uma fonte misteriosa |
|Tema	| Folclore/conto tradicional |
|Possíveis temas secundários |	Pobreza, desejo por filhos, mistério |

**4. Nível e Considerações**
   
**Nível de dificuldade:** Iniciante a Intermediário

O texto utiliza vocabulário e estruturas gramaticais relativamente simples. No entanto, algumas palavras e expressões podem ser desconhecidas para iniciantes completos, como "노부부" (casal de idosos) ou "샘물" (fonte).
Considerações finais:
O texto apresenta um início interessante para uma história com potencial para explorar temas como a vida rural, a solidão e o sobrenatural. Seria interessante continuar a leitura para descobrir o que acontece com o avô após adormecer e quais são as consequências de sua ação.

---
# Prompt Extra (Zero-shot-Prompting)

Utilizamos esta técnica sem mesmo perceber e o exemplo que darei agora mostra isso. **Pequeno contexto:** estava testando as funções do Google IA Studio e acabei pedindo para ela analisar uma foto minha em uma corrida sem exemplificar a resposta desejada nem detalhar os passos a serem seguidos.

```
(Imagem subida para a IA)
Analise esta foto.  Relate os possíveis sentimentos exibidos na feição e postura do corpo.
Além disso, crie uma pequena trilha sonora que esteja relacionada à foto enviada.
```
# Resposta

Na imagem, a corredora demonstra foco e determinação. Seu olhar fixo à frente, a postura ereta e o movimento impulsionado dos braços revelam a concentração em seu objetivo.

A trilha sonora ideal para a foto seria uma música eletrônica com batidas aceleradas, transmitindo energia e vigor, como:
- "Run Boy Run" - Woodkid: Uma faixa épica e inspiradora que evoca a busca por liberdade e superação.
- "Till I Collapse" - Eminem ft. Nate Dogg: Uma canção impetuosa que incentiva a persistência e a busca pela vitória.
- "Stronger" - Kanye West: Um hino de autoafirmação e poder, ideal para motivar a corredora em sua jornada.
  
A combinação da imagem com a trilha sonora escolhida cria uma atmosfera de força, foco e determinação, características essenciais para qualquer corredor em busca de seus objetivos.

---

# 👩🏼‍💻 Desafio 02
>### "Escolher seu site preferido de notícias, pegar nove textos com o título e as ensinar para a IA. Na décima notícia apresentada, apenas fornecer o seu contéudo e perguntar qual seria um possível título tendo como base sua percepção de padrões. Além disso, pedir para ela justificar sua escolha de manchete".

Para este desafio decidi utilizar as notícias do "the news". O jornal compartilha por email cerca de cinco manchetes por dia, então, escolhi as do dia 07/05/24 e 08/05/24.

# Prompt
```
Analise os títulos e o conteúdo das noticias abaixo. Com base na sua análise, sugira um título para o décimo texto, explicando como chegou em tal conclusão e expondo os padrões percebidos.

---

Hamas aceita proposta de cessar-fogo que está longe do que Israel deseja.

Um representante do Hamas disse que o grupo terrorista concordou com uma proposta de cessar-fogo apresentada por negociadores do Egito e Catar.O acordo faria com que os dois lados do conflito pausassem completamente os ataques na Faixa de Gaza por 42 dias no mínimo.Então a guerra vai acabar? Autoridades de Israel disseram que a proposta ainda está “longe das exigências do país”, principalmente porque não existe um consenso sobre a libertação de reféns.O assunto é prioridade do governo de Netanyahu. A inteligência israelense diz que, dos 240 sequestrados pelo Hamas nos ataques de 07/10, 128 civis continuam sob o poder dos terroristas.Autoridades de Israel, inclusive, dizem que o Hamas teria aceitado o cessar-fogo apenas para os israelenses serem vistos como a parte que se recusou a chegar a um compromisso.Ou seja, não existe perspectiva para o fim da guerra em Gaza — que já dura 7 meses. Mesmo assim, Israel enviou uma delegação ao Egito para continuar com as negociações.De olho na situação, os EUA mandaram até diretor da CIA para participar das conversas. Recentemente, o governo aprovou mais de US$ 20 bi para Israel, o que causou protestos nas universidades.Enquanto isso, os ataques continuam:🇵🇸 O Hamas atacou uma região de ajuda humanitária na fronteira de Israel e Gaza, fechando uma das principais passagens de suprimentos;🇮🇱 Depois de emitir uma ordem de evacuação para 100 mil civis palestinos, forças israelenses bombardearam a cidade de Rafah.

---

Desastre no RS gera impactos econômicos para todo o país.

A maior enchente da história do Rio Grande do Sul retirou milhares de famílias de suas casas, destruiu partes de cidades e causou quase 100 mortes até agora, com mais de 350 cidades em estado de calamidade.Além de todo esse caos humanitário, que falamos ontem aqui, toda a tragédia impacta diretamente na economia — não só da região, mas de todo o país.Explicando: Para começo de conversa, o RS é responsável por nada menos que 58% de todo o arroz produzido no Brasil. Além disso, tem também 15% das lavouras de soja.Mas não para nas plantações… As inundações podem ter afetado ainda mais os frigoríferos e a pecuária. Pense que boa parte dos animais — porcos, bois, vacas — morreram com as enchentes.Estamos falando de bilhões de reais💰Com as unidades operacionais e de distribuição praticamente paradas, a perda deve ser grande.Usando como referência, apesar da causa ser totalmente diferente, a greve dos caminhoneiros de 2018 gerou prejuízo de R$ 3 bilhões na indústria nacional.Na época da paralisação, os preços de produtos básicos para o consumidor final subiram mais de 80%.Isso sem falar que, na atual situação, diversas estradas, pontes e rodovias — por onde toda essa produção escoa — desabaram. A restauração delas pode custar mais de R$ 1 bilhão para o governo.Além disso, o aeroporto Salgado Filho, em Porto Alegre, foi fechado por tempo indeterminado.Zoom out: Os prejuízos financeiros causados por desastres ambientais somaram mais de R$ 105 bilhões em 2023. Só as chuvas, no ano passado, incluindo o ciclone no RS, deixaram danos de R$ 51,4 bilhões.

---

O que a tecnológica AI tem a ver com o mercado de gás natural?

Muito dado para pouca energia. Por mais contraditório ou aleatório que isso possa parecer, o mercado de gás natural tem muito a agradecer pelo boom da inteligência artificial.Pare para pensar: Com tanta informação para armazenar, as BIG TECHs têm feito investimentos multibilionários na construção de data centers — que, por sua vez, precisam de muita energia para funcionar.Caso você não saiba… Assim como a “nuvem” onde você guarda os seus arquivos, todos os dados que alimentam os chatbots de AI precisam, na verdade, de um espaço físico.Até 2030, o consumo energético dos data centers deve quase triplicar — passando de 11 para 42 gigawatts.Ao mesmo tempo, o gás natural parece ser o único meio que pode suprir tanta demanda — as fontes de energia limpa não estão dando conta.Com isso, o gás natural deve fornecer 60% da energia necessária para os data centers de AI nos próximos anos.A “era dourada” do gás. É assim que os produtores batizaram o movimento, já que a procura pela modalidade deve crescer em mais de 30% só nos EUA. Os preços podem aumentar 46% em 6 anos.O impacto ambiental 😷Apesar do nome ter uma vibe clean, ambientalistas criticam que o gás natural é um combustível fóssil que gera emissão de gases poluentes — ainda que em menor nível do que o petróleo.Os data centers são responsáveis por 45% dos gases de efeito estufa da indústria TECH. Com o gás natural, as emissões de CO₂ podem mais do que duplicar até 2030, chegando a 220 milhões de toneladas por ano.PS: No Brasil, os grandes data centers consomem quase a mesma quantidade de energia que o Tocantins inteiro.

---

Shein quer abocanhar mercado da Amazon — e vice-versa.

A briga do e-commerce. A Shein quer basicamente virar a nova Amazon, expandindo para venda de mais produtos além de roupas, sapatos e acessórios.A ideia da gigante chinesa é fechar negócio com empresas como a Colgate/Palmolive, Hasbro e outras focadas em cuidados com a pele para ser um dos marketplaces dessas categorias.A gigante já tinha aberto espaço na plataforma para marcas e varejistas no ano passado.Um raio-x do movimento: Focando muito em tendências entre jovens, principalmente através do TikTok, a Shein já domina o mercado de roupas na internet.Para se ter uma ideia, em abril de 2022, a companhia foi avaliada em US$ 100 bilhões, mais que as concorrentes do fast fashion H&M e Zara juntas.Ainda assim, quando falamos de e-commerce como um todo, seus US$ 2 bilhões de lucro anual ainda ficam bem longe dos US$ 30 bi da Amazon.Enquanto isso, do outro lado…A Amazon, que detém 37% do mercado de varejo nos EUA, está fazendo o movimento contrário: quer vender e ampliar sua presença no mercado de roupas.Para isso, a BIG TECH está reduzindo as taxas de comissão para os vendedores do setor.Pense que, hoje, a Amazon tem uma vantagem clara em relação à Shein: entregas rápidas. Enquanto o Prime entrega em apenas 24h, os clientes da Shein costumam esperar até duas semanas paras os pedidos chegarem.

---

Grécia está criando cidade inteligente no melhor estilo Dubai.

A maior smart city da Europa. A cidade de Ellinikon, a 20 minutos de Atenas, está saindo do papel e pretende gerar meros € 10 bilhões em receitas fiscais.A planta começou a ser criada há mais de 10 anos, usando o terreno onde ficava um antigo aeroporto da Grécia.💰 Foco no χρήματα (dinheiro): Como os prédios modernos estão sendo construídos, a grande empresa imobiliária por trás da criação da cidade já vendeu € 641 milhões em apartamentos.Por que cidade inteligente? A tendência é que as metrópoles que tenham infraestrutura, transporte e espaços públicos integrados à tecnologia para aumentar os benefícios e qualidade de vida do cidadão apareçam e cresçam cada vez mais.A moderna Dubai, por exemplo, está no topo da lista das cidades onde as pessoas querem morar e trabalhar.Em números, o mercado de smart cities foi avaliado em US$ 600 bilhões em 2023 e tem projeção de crescer 25% por ano até 2029.Só na Grécia, o esperado é que a cidade adicione 2,5 pontos ao PIB, com a criação de 80 mil novos empregos — ajudando o país a sair de uma crise econômica.🌎 Ao todo, 142 cidades do mundo são consideradas smart cities. Para surpresa do estagiário, das 10 mais bem ranqueadas, 7 ficam na Europa. Clique para ver.O que mais foi relevante no mundo da economia?Disputada ela… Paramount busca negociações com Sony/Apollo e SkydanceProjeção da Selic: Possível desaceleração dos cortes divide mercado, com taxa a 10,5% em maioFechou a R$ 5,07. Dólar e Ibovespa fecham na estabilidade, enquanto Bolsas em NY disparam. 

---

O sonho da casa própria parece distante para os americanos.

Dependentes dos aluguéis. Apenas 13% dos inquilinos americanos acreditam que um dia vão conseguir comprar uma casa — uma mínima histórica para esse número.Em contrapartida, 74% de quem mora de aluguel acredita que comprar um imóvel é algo difícil, vendo a casa própria como algo distante da realidade.Por que isso importa? Esse é mais um reflexo das atuais altas taxas de juros, que estão no patamar de 5,25% e 5,5%, o nível mais alto em 23 anos.Pense que os juros são o custo do dinheiro. Logo, o impacto direto disso é que pegar empréstimos e financiamentos fica mais caro, afastando o americano dessa possibilidade.Talking numbers: Em 2022, quando as taxas passaram a subir consideravelmente, visando controlar a inflação, o número de pedidos de empréstimos caiu 44% na terra do Tio Sam.🏘️ O preço médio de uma casa em 2023 está em um nível recorde, chegando a quase US$ 400 mil dólares no ano passado.Ao mesmo tempo, espera-se que o custo do aluguel aumente quase 10% no próximo ano, mesmo com as perspectivas de que o Fed diminua os juros. Nem o aluguel tá fácil…Nota de rodapé: Os mais prejudicados são os jovens, que estão deixando a casa dos pais mais tarde. “Bem na minha vez de ser adulto…”.

---

As atualizações da maior catástrofe do Rio Grande do Sul.

Mobilização nacional. Diante da tragédia causada pelas fortes chuvas no Rio Grande do Sul, o Congresso decretou calamidade pública no estado até o final do ano.Isso significa que, agora, o governo federal pode enviar recursos ao RS sem se preocupar com as regras fiscais que limitam os gastos da União.A preocupação com os gaúchos e os recursos para o estado aumentaram com os últimos desdobramentos da tragédia:O número de vítimas subiu para 95, e o de afetados para 1,5 milhão;Cidades do sul do estado estão em alerta de “perigo extremo de tempestades”;Porto Alegre está em racionamento e 85% da população está sem água;A Marinha enviou o maior navio de guerra da América Latina para o estado;Um jacaré chegou a ser visto nas ruas de um bairro de Porto Alegre.A corrente do bem faz a diferença 🤝Uma verdadeira onda de apoio se formou no Brasil inteiro diante da repercussão da catástrofe:💰 O SOS Rio Grande do Sul recebeu mais de R$ 38M em doações; a maior vaquinha que vimos, do @badincolono, já arrecadou mais de R$ 51M;🏄‍♂️ Surfistas se mobilizaram e ajudaram a resgatar 200 crianças de regiões alagadas;⛑️ A equipe de ajuda emergencial realizou o salvamento de mais de 20 mil pessoas nos últimos dias;🦮 Mais de 6 mil animais foram resgatados em áreas inundadas;🚰 Fábricas de cerveja tiveram a produção paralisada para envasar água potável.

---

O app de músicas que é “bom demais pra ser verdade”.

Um app gratuito com faixas dos maiores artistas do mundo e que não tem anúncios no meio da música. Esse é o Musi, que virou queridinho da Gen Z neste ano.A “magia” do Musi, na verdade, não é tão mágica assim. Ele basicamente funciona como um player de vídeos que já estão no YouTube, com a diferença de que é possível organizá-los em playlists.Esse modelo de negócio fez a empresa faturar US$ 107 milhões só na América do Norte nos últimos dois anos.🤔 E como eles ganham dinheiro? Anúncios. A diferença é que eles são silenciosos e podem ser fechados em 15 segundos. Assim, as músicas não são interrompidas e nem existe um limite de plays. Uma versão ads-free está disponível por US$ 6.O Musi já foi baixado 66M de vezes desde o lançamento, sendo 8,5M só no ano passado. Isso é mais do que os concorrentes Deezer e Pandora.Com todo esse boom, gravadoras e empresários da música já mostraram resistência, dizendo que o business praticado pelo Musi é ilegal.Isso porque o app não tem licença para retransmitir os vídeos do YouTube, além de não remunerar os artistas, nem pagar direitos autorais, como fazem Spotify, Deezer e outros streamings — movimentando US$ 29 bi por ano.O outro lado: A defesa do app diz que não há nada de errado, já que ele apenas disponibiliza os vídeos, sem permitir o download deles.

---

Mr Beast se separou da empresa por trás dos seus negócios.

Cortou relações. Depois de 6 anos trabalhando com a Night Media, o maior youtuber do mundo terminou seu relacionamento com a sua “gestora de talentos”.Talvez você não saiba, mas por trás de diversos canais de YouTube há uma terceira empresa que monta todo o business — deixando o influenciador focado na parte mais criativa da coisa.Fazendo um paralelo, é como se o Casimiro abrisse mão da parceria com a LiveMode, que é a empresa por trás da CazéTV.O motivo por trás: O creator de 26 anos — sim, o Mr Beast só tem 26 anos — quer ter mais controle nos negócios, que hoje tem uma receita anual de U$ 700 milhões, criando seu próprio time interno.Pra se ter uma ideia, além de ter o maior canal do YouTube do planeta, com 256 milhões de inscritos, ele também tem sua marca de doces Feastables e da rede de fast food MrBeast Burguer.O movimento mostra a tendência de criadores de conteúdo de buscarem mais autonomia, à medida que seus negócios vão muito além do conteúdo — passando a ter produtos e marcas próprias envolvidas.Zoom out: O mercado de creators global já tem uma média de 300 milhões de criadores de conteúdo, valendo cerca de US$ 250 bilhões globalmente, e podendo dobrar em 4 anos.

---

Mirando o mercado internacional, a brasileira Suzano fez uma oferta de US$ 15 bilhões para comprar a americana International Paper.A proposta é realmente grande. A Suzano é a empresa de papel e celulose #1 do Brasil, enquanto a IP é maior do mundo no ramo — sim, a brasileira está tentando comprar um ativo maior do que ela mesma.Tanto que, para sustentar a oferta, que vai ser toda em dinheiro e à vista, a empresa está negociando um financiamento. Para se ter uma ideia, só o valor de mercado da Suzano é de cerca de US$ 15 bi.Presença global: Se a IP concordar em vender seus ativos, a Suzano tem o potencial de se tornar um grupo super relevante no comércio global de embalagens de papel, atuando nos 5 continentes.No Brasil, a empresa ficaria com as duas maiores marcas de papel A4 do país: a Report, que já é sua, e a Chamex, que é da IP.By the numbers: Depois do boom da pandemia, o mercado de papel e celulose movimenta, hoje, mais de US$ 350 bilhões no mundo todo.📉 A Faria Lima não curtiu… Enquanto as ações da IP subiram, as da Suzano caíram 10% depois da notícia. A análise foi de que a empresa pode estar tentando dar um passo maior do que a própria perna. Cenas para os próximos capítulos…

```
# Resposta
**Sugestão de título para o décimo texto:**

## *Suzano mira expansão global com oferta bilionária pela líder do mercado International Paper*

**Justificativa:**
Analisei os títulos e conteúdos das notícias anteriores e identifiquei alguns padrões:

**Foco no impacto:** Os títulos geralmente destacam o impacto ou consequência principal do evento noticiado.

**Clareza e concisão:** Os títulos são curtos, diretos e informativos, evitando jargões ou termos complexos.

**Uso de números:** Quando relevante, os títulos utilizam números para quantificar o impacto do evento, como valores monetários ou porcentagens.

**Menção das empresas envolvidas:** Quando se trata de negócios ou fusões, os títulos costumam mencionar as empresas envolvidas.
Com base nesses padrões, o título sugerido acima destaca o principal objetivo da Suzano (expansão global) e o meio pelo qual ela pretende atingir esse objetivo (oferta bilionária pela International Paper), além de mencionar ambas as empresas envolvidas na negociação.


**Padrões percebidos nos títulos:**


**Ação + Objetivo/Consequência:** Vários títulos seguem a estrutura de mencionar a ação principal seguida do objetivo ou consequência, como "Hamas aceita proposta de cessar-fogo" e "Shein quer abocanhar mercado da Amazon".

**Local + Evento:** Alguns títulos especificam a localização geográfica do evento, como "Desastre no RS gera impactos econômicos" e "Grécia está criando cidade inteligente".

**Problema + Impacto:** Em alguns casos, os títulos destacam um problema e seu impacto, como "O sonho da casa própria parece distante para os americanos" e "As atualizações da maior catástrofe do Rio Grande do Sul".

**Conclusão:**
O título sugerido para o décimo texto segue os padrões identificados nas notícias anteriores, sendo claro, conciso e informativo, ao mesmo tempo em que destaca o impacto e as empresas envolvidas na notícia.

> ## Manchete verdadeira: *Suzano quer comprar a maior empresa de papel e celulose do mundo*

---

# *Fim das anotações/ desafios do dia dois.*
#### [↩Voltar para o Início](https://github.com/rafaelatn/Imersao-IA-Alura-Google/tree/main?tab=readme-ov-file)


