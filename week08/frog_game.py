def jump(lake, i, j):

	assert i < j, 'Incorrect input.'

	return lake[:i] + list(lake[j]) + lake[i+1:j] + list(lake[i]) + lake[j+1:]


def find_all_jumps(lake):

	possible_states = []
	n = len(lake)

	for frog_position in range(n):

		if frog_position < n-1 and lake[frog_position] == '>' and lake[frog_position+1] == '_':
			possible_states.append(jump(lake, frog_position, frog_position+1))

		if frog_position < n-2 and lake[frog_position] == '>' and lake[frog_position+2] == '_':
			possible_states.append(jump(lake, frog_position, frog_position+2))

		if frog_position > 0 and lake[frog_position] == '<' and lake[frog_position-1] == '_':
			possible_states.append(jump(lake, frog_position-1, frog_position))

		if frog_position > 1 and lake[frog_position] == '<' and lake[frog_position-2] == '_':
			possible_states.append(jump(lake, frog_position-2, frog_position))

	return possible_states


def start_game(lake, end_state, current_path=None):

	if current_path is None:
		correct_path = []
	else:
		correct_path = current_path

	possible_states = find_all_jumps(lake)

	if end_state in possible_states:
		correct_path.append(end_state)
		return correct_path

	for state in possible_states:

		if find_all_jumps(state) != []:
			correct_path.append(state)
			start_game(state, end_state, correct_path)

		else:
			correct_path.pop()



def main():

	lake = ['>', '>', '>', '_', '<', '<', '<']
	print(find_all_jumps(lake))
	end_state = lake[::-1]


if __name__=='__main__':
	main()



