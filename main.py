import pprint


pos_d={
    11:" ",12:" ",13:" ",
    21:" ",22:" ",23:" ",
    31:" ",32:" ",33:" "
}
 #-------------- first print for intro
print(f'-----Guide:\n'
      f'(this is row-col addres for positioning X or O)\n'
      f'            11 | 12 | 13 \n            -----------\n'
      f'            21 | 22 | 23 \n            -----------\n'
      f'            31 | 32 | 33 \n'
      f'    for example (12 X) will be:\n'
      f'             {pos_d[11]} | X | {pos_d[13]} \n            -----------\n'
      f'             {pos_d[21]} | {pos_d[22]} | {pos_d[23]} \n            -----------\n'
      f'             {pos_d[31]} | {pos_d[32]} | {pos_d[33]} \n'
      f'            Good Luck!\n')

pos_filled=[]

#todo ----- function check win

def check_win(pos_d):
    check = list(pos_d.values())
    row_col_dict = {
        'col1': check[::3],
        'col2': check[1::3],
        'col3': check[2::3],
        'row1': check[:3],
        'row2': check[3:6],
        'row3': check[6:]}
    if row_col_dict['row1'][0] and row_col_dict['row2'][1] and row_col_dict['row3'][2] == 'X':
        return 'X'
    elif row_col_dict['row1'][0] and row_col_dict['row2'][1] and row_col_dict['row3'][2] == 'O':
        return 'O'
    else:
        for key, values in row_col_dict.items():
            if values[0] == 'X' and values[1] == 'X' and values[2] == "X":
                return 'X'
            elif values[0] == 'O' and values[1] == 'O' and values[2] == "O":
                return 'O'
            else:
                pass

#todo ----- while loop

win = False
while not win:
    pos_input = input(f'Inter --- position +space+ X or O ---\n'
                            f'Inter here:'
                            )
    listed_p_in = pos_input.split(" ")
    try:
        if int(listed_p_in[0]) in pos_d.keys():
            if int(listed_p_in[0]) not in pos_filled:
                pos_d[int(listed_p_in[0])] = (listed_p_in[1]).upper()
                print(f' {pos_d[11]} | {pos_d[12]} | {pos_d[13]} \n-----------\n'
                      f' {pos_d[21]} | {pos_d[22]} | {pos_d[23]} \n-----------\n'
                      f' {pos_d[31]} | {pos_d[32]} | {pos_d[33]} ')
            else:
                print('\n---- position taked already, pleas try again; ----\n')
        if int(listed_p_in[0]) not in pos_filled:
            pos_filled.append(int(listed_p_in[0]))

        if check_win(pos_d):
            win=True
            winner = check_win(pos_d)
    except ValueError :
        print('\n------ Please check you have inter "SPACE" ------\n'
              '------- Or Space in "first of entry" remove it-------\n'
              '------------ Or Entred A ValidValue ----------\n')



print('\n---------end----------\n'
      f'------winner: {winner} ------')






#todo ----- bot func for solo
