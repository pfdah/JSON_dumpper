import json
import os

inputs_loc = 'Your Input folder location here'
output_loc = 'Your Output location here'

if __name__ == '__main__':
    input_indt = int(input("Enter the indentation\n"))
    print("Starting")
    for js in os.listdir(inputs_loc):
        i_f = open(os.path.join(inputs_loc, js))
        data = json.load(i_f)
        with open(os.path.join(output_loc, js), 'w') as o_f:
            json.dump([data], o_f, indent=input_indt)
        i_f.close()
        o_f.close()

    print("Done")