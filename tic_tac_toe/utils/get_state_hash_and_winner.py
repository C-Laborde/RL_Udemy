def get_state_hash_and_winner(env, i, j):
    """
    i, j = coordinates on the board where to place the next value
    """
    results = []

    for v in (0, env.x, env.o):
        env.board[i, j] = v  # if empty board it should already be 0
        if j == 2:
            # j goes back to 0, increase i, unless i = 2, then we're done
            if i == 2:
                # the board is full, collect results and return
                state = env.get_state()
                ended = env.game_over(force_recalculate=True)
                winner = env.winner
                results.append((state, winner, ended))
            else:
                results += get_state_hash_and_winner(env, i + 1, 0)
        else:
            # increment j, i stays the same
            results += get_state_hash_and_winner(env, i, j + 1)

    return results
