

#Import all the required packages to run this python code
import argparse
import os
import subprocess
import shlex


#This function takes in all the parsing arguments
def parse_args():
    parser = argparse.ArgumentParser(description='Merges variants in BEDPE format, based on bedtools pairtopair results. \
        Make sure original BEDPE has 10 columns before running bedtools pairtopair')
    parser.add_argument('-i', '--orig_bedpe', type=str, required=True,
        help='BEDPE file to be merged')
    parser.add_argument('-p', '--ptop_output', type=str, required=False, default=0,
        help='bedtools pairtopair output listing variants to merge')
    return parser.parse_args()

#This function takes bedpe file and get overlaps
def get_overlaps(overlap_bedpe):
    merge_ids = []
    merge_regions = []
    with open(overlap_bedpe, "r") as o_file:
        for line in o_file:
            line = line.strip().split()
            ids = [line[6], line[16]]
            ids.sort()
            if not ids in merge_ids:
                merge_ids.append(ids)
                chr1 = line[0]
                chr2 = line[3]
                match_chr1 = line[10]
                match_chr2 = line[13]
                if chr1 == chr2:
                    print("Warning: !!!!!!!!!!!!!! Event is on same chr !!!!!!!!!!!!")
                if chr1 == match_chr1 and chr2 == match_chr2:
                    start1 = min(int(line[1]), int(line[11]))
                    end1 = max(int(line[2]), int(line[12]))
                    start2 = min(int(line[4]), int(line[14]))
                    end2 = max(int(line[5]), int(line[15]))
                elif chr1 == match_chr2 and chr2 == match_chr1:
                    start1 = min(int(line[1]), int(line[14]))
                    end1 = max(int(line[2]), int(line[15]))
                    start2 = min(int(line[4]), int(line[11]))
                    end2 = max(int(line[5]), int(line[12]))
                else:
                    print("Warning: !!!!!!!!!!!!!! Chromosomes don't match !!!!!!!!!!!!")

                new_id = line[6] + '_' + line[16]
                region = [chr1, start1, end1, chr2, start2, end2, new_id] + line[7:10]
                merge_regions.append(region)
    
    id_list = [item for sublist in merge_ids for item in sublist]

    return id_list, merge_regions

#This function returns non-overlap regions
def get_non_overlaps(orig_bedpe, merge_ids):
    regions = []
    with open(orig_bedpe, "r") as o_file:
        for line in o_file:
            line = line.strip().split('\t')
            id = line[6]
            if not id in merge_ids:
                regions.append(line)
    return regions

#This is main function that takes in all the functions within it to run.
def main():
    args = parse_args()

    final_bedpe = args.orig_bedpe.replace("_sorted.bedpe", "_merged.bedpe")

    merge_ids, merge_regions = get_overlaps(args.ptop_output)
    
    regions = get_non_overlaps(args.orig_bedpe, merge_ids)

    regions.extend(merge_regions)

    with open(final_bedpe, 'w') as out_file:
        for line in regions:
            out_file.write('\t'.join([str(x) for x in line]) + '\n')


#this helps in running the python code as a script
if __name__ == "__main__":
    print("Hello, Merging BEDPE...")
    main()
    print("Done :)")
