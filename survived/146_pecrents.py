def MassVote(N: int, Votes: list) -> str:
    counter = 0
    for i in range(len(Votes)):
        counter += 1
        if Votes[i] == max(Votes):
            break
    if max(Votes) * 100 / sum(Votes) > 50 and Votes.count(max(Votes)) == 1:
        return 'majority winner ' + str(counter)
    elif max(Votes) * 100 / sum(Votes) <= 50 and Votes.count(max(Votes)) == 1:
        return 'minority winner ' + str(counter)
    else:
        return 'no winner'

#print(MassVote(5, [60, 10, 10, 15, 5]))     # majority winner 1
#print(MassVote(3, [10, 15, 10]))            # minority winner 2
#print(MassVote(4, [111, 111, 110, 110]))    # no winner
#print(MassVote(8, [111, 111, 110, 110, 50, 60, 70, 80]))
#print(MassVote(2, [111, 110]))
#print(MassVote(5, [10, 10, 60, 15, 5]))
print(MassVote(3, [23, 50, 27]))