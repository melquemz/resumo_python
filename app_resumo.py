import nltk
nltk.download('punkt')
import string
nltk.download('stopwords')

stopwords = nltk.corpus.stopwords.words('portuguese')

def preprocessamento(texto):
  texto_formatado = texto.lower() # deixa todo o texto minusculo 
  tokens = []
  for token in nltk.word_tokenize(texto_formatado): #work vai separa palavra por palavra
    tokens.append(token)

  tokens = [palavra for palavra in tokens if palavra not in stopwords and palavra not in string.punctuation] #vai percorrer todo o tokens e ver quais palavras sao stopworks e olhar tambem se nao sao pontos...
  texto_formatado = ' '.join([str(elemento) for elemento in tokens if not elemento.isdigit()]) #.join vai juntar tudo e deixa o texto normal e sem stopworks e pontuaçoes e nem numeros

  return texto_formatado



def sumarizar(texto, quantidade_sentencas):
  texto_original = texto
  texto_formatado = preprocessamento(texto_original)

  frequencia_palavras = nltk.FreqDist(nltk.word_tokenize(texto_formatado))
  frequencia_maxima = max(frequencia_palavras.values())
  for palavra in frequencia_palavras.keys():
    frequencia_palavras[palavra] = (frequencia_palavras[palavra] / frequencia_maxima)
  lista_sentencas = nltk.sent_tokenize(texto_original)
  
  nota_sentencas = {}
  for sentenca in lista_sentencas:
    for palavra in nltk.word_tokenize(sentenca):
      if palavra in frequencia_palavras.keys():
        if sentenca not in nota_sentencas.keys():
          nota_sentencas[sentenca] = frequencia_palavras[palavra]
        else:
          nota_sentencas[sentenca] += frequencia_palavras[palavra]

  import heapq
  melhores_sentencas = heapq.nlargest(quantidade_sentencas, nota_sentencas, key=nota_sentencas.get)

  return lista_sentencas, melhores_sentencas, frequencia_palavras, nota_sentencas