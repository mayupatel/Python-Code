

# Import the required modules
import argparse
import os


#this function takes in all the parsing arguments
def parse_args():
    parser = argparse.ArgumentParser(description='Combines lifted-over coordinates from two breakpoints into BEDPE. \
        Requires the original BEDPE and a BED for each set of breakpoints, generated by UCSC liftover tool. \
        BED and BEDPE files must all be in the same order (converted files in the same order as original)')
    parser.add_argument('-i', '--lift_bed_1', type=str, required=True,
        help='BED file of liftovers for breakpoint 1')
    parser.add_argument('-j', '--lift_bed_2', type=str, required=True,
        help='BED file of liftovers for breakpoint 2')
    parser.add_argument('-b', '--orig_bedpe', type=str, required=True,
        help='Original BEDPE with breakpoint 1 and 2 coordinates that were lifted-over')
    parser.add_argument('-o', '--out_bedpe', type=str, required=True,
        help='Output BEDPE file')
    return parser.parse_args()


#This function combines all the bed files and bedpe file
def combine_beds(lift_bed_1, lift_bed_2, orig_bedpe):
    with open(lift_bed_1, 'r') as b_1:
        b1_lines = b_1.readlines()
    with open(lift_bed_2, 'r') as b_2:
        b2_lines = b_2.readlines()
    with open(orig_bedpe, 'r') as bedpe:
        bedpe_lines = bedpe.readlines()

    new_bedpe = []
    failed_sv = []

    while len(bedpe_lines) > 0:
        this_sv = bedpe_lines[0].split('\t')
        next_b1 = b1_lines[0].split('\t')
        next_b2 = b2_lines[0].split('\t')

        this_end_1 = this_sv[2]
        this_end_2 = this_sv[5]
        b1_end = next_b1[3].split('-')[1]
        b2_end = next_b2[3].split('-')[1]

        if this_end_1 == b1_end and this_end_2 == b2_end:
            new_bedpe.append(next_b1[0:3] + next_b2[0:3] + this_sv[6:])
            bedpe_lines.pop(0)
            b1_lines.pop(0)
            b2_lines.pop(0)
        elif this_end_1 != b1_end and this_end_2 != b2_end:
            print "Both breakpoints failed liftover"
            print next_b1
            print next_b2
            failed_sv.append(this_sv)
            bedpe_lines.pop(0)
        elif this_end_1 != b1_end:
            print "Breakpoint 1 failed liftover"
            print next_b1
            failed_sv.append(this_sv)
            bedpe_lines.pop(0)
            b2_lines.pop(0)
        elif this_end_2 != b2_end:
            print "Breakpoint 2 failed liftover"
            print next_b2
            failed_sv.append(this_sv)
            bedpe_lines.pop(0)
            b1_lines.pop(0)

    return new_bedpe, failed_sv

#this writes the two new bedpe file
def write_bedpe(new_bedpe, out_bedpe):
    with open(out_bedpe, 'w') as out_file:
        for line in new_bedpe:
            out_file.write('\t'.join(line))

# the main MENU Function handles the code..
def main():
    args = parse_args()

    new_bedpe, failed_sv = combine_beds(args.lift_bed_1, args.lift_bed_2, args.orig_bedpe)
    
    write_bedpe(new_bedpe, args.out_bedpe) # write new bedpe file
    write_bedpe(failed_sv, args.out_bedpe.replace('.bedpe', '_failed.bedpe')) # rename the failed SV file


if __name__ == "__main__":
    print("Hello, Combining your lifted-over breakpoints...")
    main()
