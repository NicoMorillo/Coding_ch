def check(str1):
  if len(str1) >= 4 and len(str1) <= 25:
    if str1[0].isalpha():
      if str1[-1] != "_":
        for x in str1:
          if not x.isalpha and not x.isdigit and x == "_":
              return False
          else:
              return True
      else:
        return False
    else:
      return False
  else:
    return False 

# keep this function call here 
print(check("viva__c345adi"))