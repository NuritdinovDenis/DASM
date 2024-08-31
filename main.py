def assemble(file_input, file_output):
    instruction_set = {
        "mov ax, bx": b'\x89\xD8',
        "add ax, bx": b'\x01\xD8'  
    }
    
    with open(file_input, 'r') as infile, open(file_output, 'wb') as outfile:
        for line in infile:
            line = line.strip()
            print(line)
            if line in instruction_set:
                outfile.write(instruction_set[line])
            else:
                print(f"Неизвестная инструкция: {line}")

assemble('input.asm', 'output.bin')
