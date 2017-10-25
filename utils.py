def test_sort(sorted_list):
	prev = sorted_list[0]
	for i in sorted_list:
		if i >= prev:
			prev = i
		else:
			print 'Sorting list failed'
			return False
	print 'Sorting list successful'
	return True