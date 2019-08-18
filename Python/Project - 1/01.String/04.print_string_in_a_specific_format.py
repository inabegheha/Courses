#NABEGHEHA.COM

# Sample String: "Twinkle, twinkle, little star, How I wonder what you are! 
# Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, 
# little star, How I wonder what you are!"

# Output:

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are!


#Raveshe Aval : 

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#Raveshe Dovom:

a = "Twinkle, twinkle, little star,"
b = "How I wonder what you are!"
c = "Up above the world so high,"
d = "Like a diamond in the sky."
e = "Twinkle, twinkle, little star,"
f = "How I wonder what you are."

#Yeki az 2 ta Print Haye Paen mitone Faal bashe :

#1
print("{}\n\t\t{}\n\t\t\t{}\n\t\t\t{}\n{}\n\t\t{}".format(a, b, c, d, e, f))

#2
print("\n{}\n{:>34}\n{:>45}\n{:>44}\n{}\n{:>34}".format(a, b, c, d, e, f))

#Raveshe Sevom:

print("\nTwinkle, twinkle, little star,\n\t\tHow I wonder what you are!\n\t\t\tUp above the world so high,\n\t\t\t"
      "Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\t\tHow I wonder what you are")

