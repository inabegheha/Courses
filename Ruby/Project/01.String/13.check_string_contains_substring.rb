#NABEGHEHA.COM

def check_string(my_string, my_substr)
    if my_string.include? my_substr
      "True"
   else
      "False"
   end
end
print check_string("JavaScript","Script")
print "\n",check_string("JavaScript","Scriptt")