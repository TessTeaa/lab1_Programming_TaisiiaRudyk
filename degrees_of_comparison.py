import re

# --- Друга задача: утворення вищого та найвищого ступенів прикметників (проста форма) ---

# Список прикметників, які не утворюють ступенів порівняння
ungradable_adjectives = {
    'нім', 'сліп', 'лис', 'мертв', 'жонат',
    'ворон', 'гнід', 'булан', 'чал',
    'вишнев', 'буряков', 'персиков',
    'превелик', 'завелик', 'маленьк', 
    'чорнесеньк', 'здоровенн', 'старезн', 
    'загребущ', 'чорняв', 'жовтуват', 'синюват',
    'білокрил', 'гостроок', 'прудконог'
}


def comparative_adjective(word: str) -> str:
    word = word.strip().casefold()

    #винятки
    irregulars = {
        'гарн': 'кращ',
        'хорош': 'кращ',
        'поган': 'гірш',
        'велик': 'більш',
        'мал': 'менш',
        'довг': 'довш',
        'легк': 'легш',
    }

    bad_prefix = r"\b(пре|за|над|пра)"
    bad_suffix = r"(ісіньк|юсіньк|еньк|ав|яв|уват|юват|яст|енн|езн|ющ|ущ|ащ|ист|ляв)\b"
    base_pattern = r"(\w+)(ий|а|е|і)$"
    match = re.match(base_pattern, word)
    
    if match:
        base = match.group(1)
        ending = match.group(2)

        # Перевірка, чи належить основа до незмінних прикметників
        if base in ungradable_adjectives or re.findall(bad_prefix, base) or re.findall (bad_suffix, base):
            return f"{word} - не утворює ступенів порівняння"
           
        # Вищий простий ступінь
        if base in irregulars.keys():
            return f"{irregulars[base]}{ending}"
        elif base.endswith(('ок', 'ек')):
            base = base[:-2]
            if base.endswith('л'):
              base += "ь"
            if base.endswith('г'):
                return f"{base[:-1]}жч{ending}"
            elif base.endswith('зь'):
                return f"{base[:-2]}жч{ending}"
            elif base.endswith('с'):
                return f"{base[:-1]}щ{ending}"
            return f"{base}ш{ending}"
        elif  base.endswith('гк'):
            return f"{base[:-2]}жч{ending}"
        elif base.endswith('зьк'):
            return f"{base[:-3]}жч{ending}"
        elif base.endswith('жк'):
            return f"{base[:-2]}ч{ending}"
        elif base.endswith('ск'):
            return f"{base[:-2]}щ{ending}"
        return f"{base}іш{ending}"

        


def superlative_adjective(word: str) -> str:
    word = word.casefold()
 
    bad_prefix = r"\b(пре|за|над|пра)"
    bad_suffix = r"(ісіньк|юсіньк|еньк|ав|яв|уват|юват|яст|енн|езн|ющ|ущ|ащ|ист|ляв)\b"
    base_pattern = r"(\w+)(ий|а|е|і)$"
    match = re.match(base_pattern, word)

    if match:
      base = match.group(1)
      if base in ungradable_adjectives or re.findall(bad_prefix, base) or re.findall (bad_suffix, base):
        return f"{word} - не утворює ступенів порівняння"
    
        # Простий найвищий ступінь
      return f"най{comparative_adjective(word)}"
    return f"{word} - не є прикметником"
    
def process_adjectives(text: str, degree: str) -> str:
    words = text.split()
    result = []
    
    if degree == "comparative":
      for word in words:
         result.append(comparative_adjective(word))
    elif degree == "superlative":
      for word in words:
         result.append(superlative_adjective(word))
    else:
      return "Некоректний ступінь порівняння"
    return " ".join(result)
