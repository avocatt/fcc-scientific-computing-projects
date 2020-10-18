class Category:
  def __init__(self,name):
    self.ledger=[]
    self.category=name
    #added another variable to get balance easier
    self.balance=0

  def deposit(self,amount,description=None):
    #if no description is given
    if description==None:
      description=""

    self.balance+=amount
    self.ledger.append({"amount":amount,"description":description})
  
  def get_balance(self):
    return self.balance

  def transfer(self,amount,Cat):
    if self.withdraw(amount,"Transfer to "+Cat.category):
      Cat.deposit(amount,"Transfer from "+self.category)
      return True
    else:
      return False

  def check_funds(self,amount):
    #checks whether amount can be withdrawn or not
    if self.balance<amount:
      return False
    return True

  def withdraw(self,amount,description=None):
    if description==None:
      description=""
    #checks for sufficient funds for withdrawl operation
    if self.check_funds(amount):
      self.balance-=amount
      self.ledger.append({"amount":-amount,"description":description})
      return True
    else:
      return False
  
  def __str__(self):
    #adding * symbols and category name
    s="*"*((30-len(self.category))//2)+self.category
    #adding * symbols for right side
    s=s+"*"*(30-len(s))+"\n"
    for i in self.ledger:
      #making description left justified and amount right justified
      s+=i["description"][:23].ljust(23)+str("{:.2f}".format(i["amount"]).rjust(7))+"\n"
    s+="Total: "+str(self.balance)
    return s
  
def round_to_nearest_ten(n):
  if n<10:
    return 0
  return round(n/10.0)*10
  
  
def create_spend_chart(categories):
  withdrawls=[]

  #used to find the category name with max length
  max_len_category=0
  s=0

  for i in categories:

    withdraw_amount=0

    for j in i.ledger:

      #adding withdrawls to string 
      if j["amount"]<0:
        withdraw_amount+=-j["amount"]
        s+=(-j["amount"])
        
    #finding max len category name
    if len(i.category)>max_len_category:
      max_len_category=len(i.category)
    withdrawls.append([i.category,withdraw_amount])
  
  #used to calculate the percentage of a certain category
  for i in withdrawls:
    i.append(round_to_nearest_ten((i[1]/s)*100))
  s=""
  s+="Percentage spent by category\n"
  t=100
  while t>=0:
    
    #prints number and | symbol
    s+=str(t).rjust(3)+"|"+" "

    #loop for printing 'o' if the percentage>=t

    for i in range(len(withdrawls)):
      if withdrawls[i][2]>=t:
        s+="o"+"  "
      else:
        s+="   "
    t-=10
    s+="\n"

  #adding '-' to the last lines
  s+="    "+("-"*10)+"\n"

  loop_var=0

  for i in range(max_len_category):
    s+="     "
    for j in range(len(withdrawls)):
      #checks whether a character exists at a length
      if len(withdrawls[j][0])-1<loop_var:
        #if no character exists adds empty string and 2 spaces
        s+="   "
      else:
        #adds character 
        s+=withdrawls[j][0][loop_var]+"  "
    loop_var+=1
    if i!=max_len_category-1:
      s+="\n"


  return s
  
