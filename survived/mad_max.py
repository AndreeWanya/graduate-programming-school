def MadMax(N: int, Tele: list) -> list:
	max_n = max(Tele)
	Tele.remove(max_n)
	left_el, right_el = [], []
	while len(Tele) > 0:
		left_el.append(min(Tele))
		Tele.remove(min(Tele))
		right_el.append(max(Tele))
		Tele.remove(max(Tele))
	left_el.append(max_n)
	return left_el + right_el