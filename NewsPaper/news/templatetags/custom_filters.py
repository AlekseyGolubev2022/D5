from django import template


register = template.Library()


@register.filter()
def censor(value):
   """
   value: значение, к которому нужно применить фильтр
   """
   censored_text = ['0000','1111']
   result = value
   i = 0
   while i < len(censored_text):
      word = censored_text[i].lower()
      text = value.lower()
      if text.find(word) == -1:
         i += 1
         continue
      result = value[0] + '*'*(len(value)-1)
      break
   return result