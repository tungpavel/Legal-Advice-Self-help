print("Assured shorthold tenancies")
try:
  leave = input("Does the tenant want to leave the property? (YES/NO) ")
  if leave.lower() == "yes":
      print("""Advice:
  Express surrender
    -	made by deed
    -	signed by both landlord and tenant
    -	witnesses
    -	immediate effect termination 
          
  Implied surrender 
    -	acts or series of act that are inconsistent with the continuation of the tenancy
    -	beyond scope to confirm, requires prospects  but can discuss points that would suggest surrender
          
  Abandonment
    -	leave without notice by tenant
    -	very risky as if tenant comes back maybe illegal eviction risk
  """)
  elif leave.lower() == "no":
      what_term = input(
          "Is it \n 1 - Fixed term; or \n 2 - Periodic term?\n (1 or 2) ")
      if what_term == "1":
          in_two_months = input("Expiration in 2 months? (YES/NO) ")
          if in_two_months.lower() == "yes":
              print("""Advice:
    Can serve s21 providing it expires at the end of the fixed term but action must be taken 6 months from service date
    If forfeiture clause then possibly highlighted s8 grounds, 1 year time frame for action so can use to expire after fixed term if no clause
  """)
          elif in_two_months.lower() == "no":
              print("""Advice:
              
  BREAK OR FORFEITURE CLAUSE?
              
  DEPENDING ON CLAUSE POSSIBLE S21 or s8
  IF NEITHER, CAN BRING BOC CLAIM FOR RENT OWED BUT CAN’T EVICT UNTIL PERIODIC 
  CONSIDER GUARANTORS
  """)
      elif what_term == "2":
          print("""Advice:
    - Serve s21/s8""")
except ValueError as err:
  print(err)