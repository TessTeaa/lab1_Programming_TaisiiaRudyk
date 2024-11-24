import re

#Гурт
def Noun(word:str) -> str: #word - параметр функції

  Noun_1 = r"(\w+)(ові|ами)\b"
  Noun_2 = r"(\w+)(ом|ів|ам|ах)\b"
  Noun_3 = r"(\w+)(у|а|і|е|и)\b"

  Is_Noun_1 = re.findall(Noun_1, (word.strip()).casefold())
  Is_Noun_2 = re.findall(Noun_2, (word.strip()).casefold())
  Is_Noun_3 = re.findall(Noun_3, (word.strip()).casefold())

  if Is_Noun_1:
    return "-".join((Is_Noun_1)[0]) #беремо перший елемент
  elif Is_Noun_2:
    return "-".join((Is_Noun_2)[0])
  elif Is_Noun_3:
    return "-".join((Is_Noun_3)[0])
  else:
    return f"{(word.strip()).casefold()}-0"

def process_noun(text: str) -> str:
  words = text.split()  # Розділяємо текст на окремі слова
  result =" ".join(Noun(word) for word in words)  # Викликаємо Noun для кожного слова
  return result


#Зелений
def Adjective(word:str) -> str:

  Adj_1 = r"(\w+)(ого|ому|ими)\b"
  Adj_2 = r"(\w+)(ий|им|ім|ої|ій|их)\b"
  Adj_3 = r"(\w+)(е|а|і)\b"

  Is_Adj_1 = re.findall(Adj_1, (word.strip()).casefold())
  Is_Adj_2 = re.findall(Adj_2, (word.strip()).casefold())
  Is_Adj_3 = re.findall(Adj_3, (word.strip()).casefold())

  if Is_Adj_1:
    return "-".join((Is_Adj_1)[0])
  elif Is_Adj_2:
    return "-".join((Is_Adj_2)[0])
  elif Is_Adj_3:
    return "-".join((Is_Adj_3)[0])
  else:
    return f"\"{(word.strip()).casefold()}\ не є прикметником"

def process_adj(text: str) -> str:
  words = text.split()  # Розділяємо текст на окремі слова
  result =" ".join(Adjective(word) for word in words)  # Викликаємо Noun для кожного слова
  return result

#Прохати
def Verb(word:str) -> str:

  Verb_1 = r"(\w+)(ти)(м)(емо|ете|уть)\b"
  Verb_2 = r"(\w+)(ти)(м)(ем|еш)\b"
  Verb_3 = r"(\w+)(ти)(м)(у|е)\b"
  Verb_4 = r"(\w+)(ємо|єте|ють|ймо|йте)\b"
  Verb_5 = r"(\w+)(л)(а|о|и)\b"
  Verb_6 = r"(\w+)(єш)\b"
  Verb_7 = r"(\w+)(ю|є|в|й)\b"

  Is_Verb_1 = re.findall(Verb_1, (word.strip()).casefold())
  Is_Verb_2 = re.findall(Verb_2, (word.strip()).casefold())
  Is_Verb_3 = re.findall(Verb_3, (word.strip()).casefold())
  Is_Verb_4 = re.findall(Verb_4, (word.strip()).casefold())
  Is_Verb_5 = re.findall(Verb_5, (word.strip()).casefold())
  Is_Verb_6 = re.findall(Verb_6, (word.strip()).casefold())
  Is_Verb_7 = re.findall(Verb_7, (word.strip()).casefold())

  if Is_Verb_1:
    return "-".join((Is_Verb_1)[0])
  elif Is_Verb_2:
    return "-".join((Is_Verb_2)[0])
  elif Is_Verb_3:
    return "-".join((Is_Verb_3)[0])
  elif Is_Verb_4:
    return "-".join((Is_Verb_4)[0])
  elif Is_Verb_5:
    return "-".join((Is_Verb_5)[0])
  elif Is_Verb_6:
    return "-".join((Is_Verb_6)[0])
  elif Is_Verb_7:
    return "-".join((Is_Verb_7)[0])
  else:
    return f"{(word.strip()).casefold()}-0-0"

def process_verb(text: str) -> str:
  words = text.split()  # Розділяємо текст на окремі слова
  result =" ".join(Verb(word) for word in words)  # Викликаємо Noun для кожного слова
  return result

def selector(text: str, type) -> str:
  if type == "Noun":
    return process_noun(text)
  elif type == "Adjective":
    return process_adj(text)
  elif type == "Verb":
    return process_verb(text)
  else: 
    return "некоректний тип"
