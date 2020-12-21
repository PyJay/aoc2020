from copy import copy

def parse_instructions(fname):
    with open(fname) as f:
        instructions = f.read().splitlines()
    instructions = [i.split() for i in instructions]
    return instructions


def solve(instructions):
    instruction_address = 0
    accumulator = 0
    visited_addresses = set()
    while instruction_address not in visited_addresses:
        if instruction_address == len(instructions):
            return accumulator, True
        instruction = instructions[instruction_address]
        op_str, num_str = instruction
        if op_str == 'nop':
            visited_addresses.add(instruction_address)
            instruction_address += 1
        elif op_str == 'acc':
            num = int(num_str)
            accumulator += num 
            visited_addresses.add(instruction_address)
            instruction_address += 1
        elif op_str == 'jmp':
            num = int(num_str)
            visited_addresses.add(instruction_address)
            instruction_address += num
    return accumulator, False

def trial_variations(fname):
    instructions = parse_instructions(fname)
    for i in range(len(instructions)):
        if instructions[i][0] in ['nop', 'jmp']:
            print(f'flipping {i}')
            new_instruction = 'nop' if instructions[i][0] == 'jmp' else 'jmp'
            new_instructions = copy(instructions)
            new_instructions[i] = new_instruction, instructions[i][1]
            acc, complete = solve(new_instructions)
            if complete:
                return acc


if __name__ == "__main__":
    print(trial_variations('day08.txt'))
