# AKA- database
# USER DATA- hardcoded /INPUT
user_name  = "Johny888" # STRING
user_email = "johny@somemail.example" # STRING
user_online= False #BOOLEAN
user_last  = 15 # INTEGER
user_rank  = 4.5 #FLOAT

# LOGIC/PROCESSING
user_last  = user_last + 5

#PRESENTATION / OUTPUT

print("##### USER DATA #####")
print("name:      ", user_name)
print("email:     ", user_email)
print("online:    ", user_online)
print("last seen: ", user_last, "mins")
print("rank:      ", user_rank, "stars")
