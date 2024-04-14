def MassVote(N: int, Votes: list) -> str:
    winner = 0
    for i in range(len(Votes)):
        if Votes[i] == max(Votes):
            winner += 1
    if max(Votes) * 100 / sum(Votes) >= 50 and winner == 1:
        return 'majority winner ' + str(Votes.count(max(Votes)))
    elif max(Votes) * 100 / sum(Votes) < 50 and winner == 1:
        return 'minority winner ' + str(Votes.count(max(Votes)))
    else:
        return 'no winner'

#print(MassVote(5, [60, 10, 10, 15, 5]))     # majority winner 1
#print(MassVote(3, [10, 15, 10]))            # minority winner 2
#print(MassVote(4, [111, 111, 110, 110]))    # no winner
#print(MassVote(8, [111, 111, 110, 110, 50, 60, 70, 80]))
#print(MassVote(2, [111, 110]))