
#Import the required modules

import argparse
import os


#This function calls the parsing argument
def parse_args():
    parser = argparse.ArgumentParser(description='Combines the regions in all BEDPEs \
        in a directory into one big BED')
    parser.add_argument('-i', '--in_dir', type=str, required=True,
        help='Input directory containing BEDPE files')
    parser.add_argument('-o', '--out_bed', type=str, required=True,
        help='Output BED filename')
    return parser.parse_args()


#this function returns the bedpe regions
def get_bedpe_regions(bedpe_file):
    regions = []

    # will add the source filename in the fourth column to know where this variant came from
    f_name = os.path.basename(bedpe_file)

    with open(bedpe_file, 'r') as bedpe:
        for line in bedpe:
            line = line.split('\t')
            r1 = line[0:3]
            r2 = line[3:6]

            # Some of the regions have -1 start after the BEDPE conversion
            if int(r1[1]) < 0:
                r1[1] = '0'
            if int(r2[1]) < 0:
                r2[1] = '0'
            if int(r1[2]) < 0:
                r1[2] = '1'
            if int(r2[2]) < 0:
                r2[2] = '1'

            # Check that end is larger than start
            if int(r1[1]) > int(r1[2]):
                print(f_name)
                print(r1)
            if int(r2[1]) > int(r2[2]):
                print(f_name)
                print(r2)
            
            if r1[0] != r2[0]: # for interchr TRA, take each breakpoint
                # Add 1 to all end positions, to be sure regions cover at least 1 base
                # Some regions have the same pos for start and end... 
                # The BEDPE coords are off by 1 or 2... added 1 to end will make them
                # closer to correct, but still not exactly right, depending on the
                # original VCF format and variant type
                if r1[1] == r1[2]:
                    r1[2] = str(int(r1[2])+1)
                # else:
                #     print(f_name)
                #     print(r1[1], r1[2])
                if r2[1] == r2[2]:
                    r2[2] = str(int(r2[2])+1)

                regions.append(r1 + [f_name])
                regions.append(r2 + [f_name])
            else: # for other variant types, take from start1 to end2
                if r1[1] == r2[2]:
                    r2[2] = str(int(r2[2])+1)
                r = [r1[0], r1[1], r2[2], f_name]
                regions.append(r)

    return regions


#this main function takes in all other function to call each of them and run a script
def main():
    args = parse_args()

    bedpe_files = os.listdir(args.in_dir)
    bedpe_files = [x for x in bedpe_files if x.endswith(".bedpe")]

    regions = []

    for bedpe_file in bedpe_files:
        new_regions = get_bedpe_regions(bedpe_file)
        regions.extend(new_regions)

    with open(os.path.join(args.in_dir, args.out_bed), 'w') as out_file:
        for line in regions:
            # Check that end is larger than start
            if int(line[1]) > int(line[2]):
                print(line)

            out_file.write('\t'.join(line) + '\n')


if __name__ == "__main__":
    print("Hello, Combining your BEDPE regions into a BED...")
    main()
