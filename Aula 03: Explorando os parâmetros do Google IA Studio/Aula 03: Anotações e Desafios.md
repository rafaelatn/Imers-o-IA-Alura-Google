#### [↩Voltar para o Início](https://github.com/rafaelatn/Imersao-IA-Alura-Google/tree/main?tab=readme-ov-file)
## 📝Minhas anotações - 08/05/24
## 1. Formas de Prompt
1. **Chat Prompt:** IA armazena o histórico da conversa (comandos e respostas).
2. **Freeform Prompt:** agrega perguntas em requisição única.
3. **Structured Prompt:** estrutura comandos como banco de dados (recomendado para Few-shot Prompting)
   
## 2. Visão Computacional
Tecnologia que lida com imagens e vídeos, identificando objetos com precisão.

## 3. System Instructions no Google AI Studio
Local em que é possível ditar o comportamento da IA, alguma característica que irá aparecer em todos os prompts. 

**Exemplo:** Dizer para o Gemini analisar as informações como um analista de dados, de maneira analítica. Ou criar um anúncio criativo para turismo, como um profissional de marketing.

## 4. Temperatura
Disponível na versão 1.0 Pro do Google IA Studio, a função irá determinar a "criatividade" das respostas do Gemini. Basicamente, quanto maior for a temperatura (máximo 1) maior será a variedade de respostas, e quanto mais baixa (máximo 0), as respostas dadas serão mais objetivas e sua formatação não mudará, independentemente de quantas vezes repita o prompt.

## 5. Add Stop Sequence
É o delimitador para as respostas da IA. Na interface do Gemini e do Google IA Studio, temos o botão "Stop", mas, quando programando, ele pode ser uma palavra (Fim), ou ponto final.

## 6. Advanced Settings
As configurações avançadas são divididas entre Top K e Top P.
1. **Top K:** Irá controlar o tamanho do glossário utilizado pela IA.
2. **Top P:** Soma a máxima das probabilidades em relação ao glossário definido no Top K (soma máxima de 1).
   
>A configuração "Temperatura" irá desempatar a seleção do token (explicado no tópico abaixo) caso necessário.

**Exemplo de Top K & Top P**

Na foto abaixo, estamos analisando o "Top K", que controla o tamanho do glossário utilizado. Temos um total de cinco tokens (palavras), porém, determinamos que a IA pode escolher apenas dois deles: *"k= 2"*. 

Ao utilizarmos o "Top P" (junto com o Top K), conseguimos determinar quais serão esses tokens através da soma de suas probabilidades. 

Ou seja, para a frase *"Ontem eu fui no cinema ver __"*, quais seriam os tokens (palavras) mais prováveis de serem utilizados para completá-la? A resposta seria: *filme* ou *documentário*, já que ambos estão dentro das condições Top K e Top P (duas palavras e suas probabilidades somadas resultam em 1).

<p align="center"> <img width="500" src="/images/Top-K-_-Top-P2.jpg"></p>  

>Reprodução: Medium

## 7. Token
É a transformação de texto (letras) em números para o LLM (Large Language Machine[^1]) compreender e economizar armazenamento de palavra ao enviar um prompt.

---

# 👩🏼‍💻 Ausência de desafios propostos.

---

# *Fim das anotações/ desafios do dia três.*
#### [↩Voltar para o Início](https://github.com/rafaelatn/Imersao-IA-Alura-Google/tree/main?tab=readme-ov-file)

[^1]: [O que é Large Language Machine?](https://canaltech.com.br/inteligencia-artificial/o-que-e-llm-large-language-model/#google_vignette)

