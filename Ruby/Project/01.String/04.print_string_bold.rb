#NABEGHEHA.COM

def make_tags(tag, word)
    "<#{tag}> #{word} </#{tag}>"
end
print make_tags("i", "Ruby")
print "\n",make_tags("b", "Ruby")