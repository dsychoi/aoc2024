from utils import fetch_data


def parse_data(data):
    a = int(data[0].split(':')[1].strip())
    b = int(data[1].split(':')[1].strip())
    c = int(data[2].split(':')[1].strip())
    program = data[4].split(':')[1].strip().split(',')
    program = [int(x) for x in program]

    return a, b, c, program


def run_program(a, b, c, program):
    instructions = [program[i:i+2] for i in range(0, len(program), 2)]

    current_instruction = 0
    result = []
    while current_instruction < len(instructions):
        instruction = instructions[current_instruction]
        op_code = instruction[0]
        operand = instruction[1]
        combo_operand = 0

        # print("Current instruction", current_instruction, "OP code", op_code, "Operand", operand)

        if op_code in [0, 2, 5]:
            if operand < 4:
                combo_operand = operand
            elif operand == 4:
                combo_operand = a
            elif operand == 5:
                combo_operand = b
            elif operand == 6:
                combo_operand = c

        if op_code == 0:
            a = int(a / (2 ** combo_operand))
        elif op_code == 1:
            b = b ^ operand
        elif op_code == 2:
            b = combo_operand % 8
        elif op_code == 3:
            if a != 0:
                current_instruction = operand
                continue
        elif op_code == 4:
            b = b ^ c
        elif op_code == 5:
            result.append(str(combo_operand % 8))
        elif op_code == 6:
            b = int(a / (2 ** operand))
        elif op_code == 7:
            c = int(a / (2 ** operand))

        current_instruction += 1
    return result



raw_data = fetch_data(17)
a, b, c, program = parse_data(raw_data)
result = run_program(a, b, c, program)
# result = ''.join(run_program(729, 0, 0, [0, 1, 5, 4, 3, 0]))
# 204072340 not correct
print(result)