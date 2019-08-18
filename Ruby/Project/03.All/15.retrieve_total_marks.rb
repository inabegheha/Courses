#NABEGHEHA.COM

student_marks = Hash.new
student_marks['Adabiat'] = 74
student_marks['Oloom'] = 89
student_marks['Riazi'] = 91
total_marks = 0
student_marks.each {|key,value| total_marks +=value} 
puts "Total Marks: "+total_marks.to_s