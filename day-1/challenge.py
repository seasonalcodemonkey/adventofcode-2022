def load_input(filename):
    try:
        file = open(filename, "r")
    except Exception as exc:
        return exc
    
    lines = []

    for line in file:
        lines.append(line)

    file.close()    

    return lines

def parse_input(lines):
    elf_num, elf = 0, []
    
    elf.append([])

    for line in lines:
        
        if line.isspace():
            elf.append([]) 
            elf_num += 1
        else:
            elf[elf_num].append(int(line))
    
    return elf

def elf_carrying_most(elfs, top = 1):
    total_i, total = 0, [0]

    for elf in elfs:
        for calories in elf:
            total[total_i] += calories
        
        total.append(0)    
        total_i += 1
    
    total.sort()

    return total[len(total) - top:]
    
    
if __name__ == "__main__":
    filename = "input"
    input = load_input(filename)
    
    if isinstance(input, Exception):
        print("Could not load from %s: %s" % (filename, input)) 
    else:
        elfs = parse_input(input)
        top_most = elf_carrying_most(elfs)
        print(top_most)

        top_three_most = elf_carrying_most(elfs, 3)
        print(sum(top_three_most))

