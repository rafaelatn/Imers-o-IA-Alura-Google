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

# Desafio 01
>### "Utilizar o Few-shot-Learning e o Chain-of-Thought para um problema do seu cotidiano".
Para a técnica do "Few-shot-Learning", exemplifiquei para o Gemini (versão 1.5 Pro disponível no Google IA Studio) como queria que os textos que leio para treinar minha leitura em coreano fossem traduzidos:

# Prompt Few-shot-Learning
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

# Desafio 02
>### "Escolher seu site preferido de notícias, pegar nove textos com o título e as ensinar para a IA. Na décima notícia apresentada, apenas forneça o seu contéudo e pergunte qual seria um possível título tendo como base sua percepção de padrões. Além disso, peça para ela justificar sua escolha de manchete".



