import json
import os

inputs_loc = '/home/pratik/Downloads/JSONs/Input'
output_loc = '/home/pratik/Downloads/JSONs/Output'

if __name__ == '__main__':
    print("Starting")
    for js in os.listdir(inputs_loc):
        i_f = open(os.path.join(inputs_loc, js))
        data = json.load(i_f)
        with open(os.path.join(output_loc, js), 'w') as o_f:
            json.dump([data], o_f, indent=2)
        i_f.close()
        o_f.close()

    print("Done")