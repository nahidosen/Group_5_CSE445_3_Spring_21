import sys, yaml, csv, glob

yaml_file_names = glob.glob('./*.yaml')

write_in_row = []
need_items = ["dates", "city", "gender", "winner", "teams", "decision", "winner", "umpires", "venue"]

def find(key, dictionary):
    # everything is a dict
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result

for idx, each_yaml_file in enumerate(yaml_file_names):
    print("Processing file ", idx+1, "of", len(yaml_file_names), "file name:", each_yaml_file)
    with open(each_yaml_file) as f:
        data = yaml.load(f)
        for a in need_items:
            
            for x in find(a, data):
                write_in_row.append(x)
        with open('output_csv_file.txt', 'a') as out:        
            for listitem in write_in_row:
                out.write('%s,' % listitem)
            out.write('\n')
        write_in_row.clear()
 