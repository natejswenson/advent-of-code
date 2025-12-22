with open(f'main.txt', 'r') as file:
    for line in file:
        # 'line' will still contain the newline character '\n'
        # You can use line.strip() to remove leading/trailing whitespace and the newline
        processed_line = line.strip()
        
        # print items up to the ] character
        buttons = processed_line.split()[0]
        print(buttons)
        states=processed_line.split('{')[:1]
        print(states)