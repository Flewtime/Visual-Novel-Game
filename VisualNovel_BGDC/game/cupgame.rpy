# $ bet = 0

# Protag "What should I do..."
# Fraud "Psst. Hey, You there!"
# Protag "Hmm?"
# Fraud "Yeah you. Do you want some easy money?"
# Fraud "Fear not my friend, come and try this ball game."
# Fraud "If you can find the ball, you'll win twice the money you bet. If you fail... I get the money"
# Fraud "How's that sound?"

# Menu BallGame:
#     "PLAY THE GAME":
#         jump BallGameYes
#     "PASS":
#         jump BallGameNo

# Label BallGameYes:
# "You chose to play"
# Protag "You bet!"
# Fraud "Alrighty then, how much will you bet?"

# Menu Bet:
#     "100":
#     $ bet = 100
#     Fraud "Playing it safe i see"
#     jump BallGameRes
    
#     "200":
#     $ bet = 200
#     Fraud "Alrighty then let's start"
#     jump BallGameRes

#     "500":
#     $ bet = 500
#     Fraud "Love the spirit, ya either go big or go home"

# Label BallGameRes:
# ## Ini rng 0.0-1.0
# $ ballpoint = renpy.random.random()
# if ballpoint >= 0.7:
#     Fraud "Looks like lady luck is on your side kiddo, here take it"
#     Fraud "See you around boy"
#     Protag "Phew, I got lucky"
#         ## nominal di bet tambahin ke uang 

# else 
#     Fraud "HAH! More for me"
#     Fraud "See you around boy"
#     Protag "Looks like I'm running out of luck"
#     Protag "Better leave before it's too late"
#         ## nominal di bet kurangin dari uang 


# Label BallGameNo:
# if has_job=1
# Protag "Nah I'll pass"
# Protag "Oh!"
# Protag "It's time for my work shift"
# ## jump Cashier (kerjaannya)

# else
# Protag "Even I know this is a fraud."
# Protag "Damn, my life is not getting better"
# ## jump Act ending summary