def SynchronizingTables(N: int, ids: list, salary: list) -> list:
	ids_dict = dict(zip(sorted(ids), [i for i in range(N)]))
	salary_dict = dict(zip([i for i in range(N)], sorted(salary)))
	salary = []
	for id in ids:
		salary.append(salary_dict[ids_dict[id]])
	return salary