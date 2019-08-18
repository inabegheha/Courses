#NABEGHEHA.COM

def check_string(str,chr)
    str.tr(chr, '')
end
print check_string("JavaScript", 'a')
print "\n",check_string("Python", 'y')
print "\n",check_string("PHP", 'H')