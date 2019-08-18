#NABEGHEHA.COM

def text_int(a, b)
    ma = (10 - a).abs
	mb = (10 - b).abs
	if (ma < mb)
		return a
	end
	if (mb < ma)
		return b
	end
	return 0
end
print text_int(7, 14),"\n"
print text_int(6, 9),"\n"
print text_int(5, 5)