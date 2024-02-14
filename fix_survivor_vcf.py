
#Import the required modules to run this python code

import argparse
import os
import copy
from operator import itemgetter


#this function is to call the parsing arguments
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--in_vcf', type=str, required=True,
        help='Input vcf file')
    parser.add_argument('-c', '--contigs', type=str, required=True,
        help='txt file with header lines for contigs')
    parser.add_argument('-o', '--out_vcf', type=str, required=True,
        help='Output vcf file')
    parser.add_argument('-b', '--keep_tra', action='store_true', required=False,
        help='Flag to retain TRA in the output VCF')
    return parser.parse_args()

#This function read the vcf file 
def read_vcf_file(vcf_file, keep_tra):
    header = []
    var_list = []
    tra_list = []
    with open(vcf_file, 'r') as f:
        for row in f:
            if row.startswith("##"):
                header.append(row)
            if not row.startswith("#"):
                row = row.strip().split()
                line = {}
                line['CHROM'] = row[0]
                line['POS'] = row[1]
                line['ID'] = row[2]
                line['REF'] = row[3]
                line['ALT'] = row[4]
                line['QUAL'] = row[5]
                line['FILTER'] = row[6]
                line['INFO'] = row[7]
                line['FORMAT'] = row[8]
                line['SAMPLE'] = row[9]

                if line['ALT'] == "<INS>":
                    var_list.append(fix_ins(line))

                elif line['ALT'] == "<DEL>":
                    var_list.append(fix_del(line))
                    
                elif line['ALT'] == "<TRA>" and keep_tra: # May need to change this to SVTYPE=BND and has a MATEID
                    # Represent TRA breakpoints twice, once in each direction
                    line, line2, pos_tup = fix_tra(line)
                    # Some TRA are alraedy listed in both directions, others aren't
                    if not pos_tup in tra_list:
                        tra_list.append(pos_tup)
                        var_list.append(line)
                        var_list.append(line2) # represent TRA from both directions
                
                elif line['ALT'] == "<TRA>" and not keep_tra:
                    pass

                elif line['ALT'] == "<BND>": # May need to change this to SVTYPE=BND and no MATEID
                    #var_list.append(fix_single_bnd(line))
                    pass

                else:
                    var_list.append(line)

    return var_list, header


#This function adds the header to the vcf file for hg38 coordinates
def add_to_header(header, contig_file):
    strands_tag = '##INFO=<ID=STRANDS,Number=1,Type=String,Description="Strands">\n'
    ins_len_tag = '##INFO=<ID=INSLEN,Number=1,Type=String,Description="Length of Insertion. For INS, SVLEN is length of region where the INS might be.">\n'
    last_header = '#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tsample\n'
    
    header.append(strands_tag)
    header.append(ins_len_tag)

    with open(contig_file, 'r') as f:
        for row in f:
            header.append(row)

    header.append(last_header)

    return header


#This function fixs the insertion SVtype 
def fix_ins(line):
    info = line['INFO']
    info = info.split(';')
    info = [i for i in info if not i.startswith("CHR2")]
    info = [i for i in info if not i.startswith("SVLEN")]

    # SVLEN and ALT changes prevent end being larger than start when intersect the VCF with a BED
    # Change SVLEN to length of the region where the INS may be
    end = next(i for i in info if i.startswith("END"))
    end = int(end.replace("END=", ""))
    svlen = end - int(line['POS'])
    if svlen == 0: # Region needs to have length of at least 1
        svlen = 1
    info.append("SVLEN=" + str(svlen))

    # Change ALT to DUP - SVTYPE will still say INS
    line['ALT'] = "<DUP>"
    #info = [i for i in info if not i.startswith("SVTYPE")]
    #info.append("SVTYPE=DUP")

    # Add INSLEN to hold the actual length of the insertion
    inslen = next(i for i in info if i.startswith("OTHER"))
    inslen = inslen.replace("OTHER=", "")
    info.append("INSLEN=" + inslen)

    line['INFO'] = ';'.join(info)
    return line


#this function fix the deletion
def fix_del(line):
    info = line['INFO']
    info = info.split(';')
    info = [i for i in info if not i.startswith("CHR2")]
    
    line['INFO'] = ';'.join(info)
    return line


def generate_breakend_alt(chr1, chr2, end1, end2, strand1, strand2):

    # See https://simpsonlab.github.io/2015/06/15/merging-sv-calls/
    if strand1 == "+" and strand2 == "+":
        alt1 = "N[" + chr2 + ":" + end2 + "["
        alt2 = "]" + chr1 + ":" + end1 + ']N'
    if strand1 == "-" and strand2 == "-":
        alt1 = "]" + chr2 + ":" + end2 + "]N"
        alt2 = "N[" + chr1 + ":" + end1 + "["
    if strand1 == "-" and strand2 == "+":
        alt1 = "[" + chr2 + ":" + end2 + "[N"
        alt2 = "[" + chr1 + ":" + end1 + "[N"
    if strand1 == "+" and strand2 == "-":
        alt1 = "N]" + chr2 + ":" + end2 + "]"
        alt2 = "N]" + chr1 + ":" + end1 + "]"
    
    return alt1, alt2

#this fixs the TRA svtype
def fix_tra(line):
    info = line['INFO']
    info = info.split(';')

    chr1 = line['CHROM']
    end1 = line['POS']
    id1 = line['ID']

    chr2 = next(i for i in info if i.startswith("CHR2"))
    chr2 = chr2.replace("CHR2=", "")
    end2 = next(i for i in info if i.startswith("END"))
    end2 = end2.replace("END=", "")
    id2 = id1 + ".1"

    strands = next(i for i in info if i.startswith("STRANDS"))
    strands = strands.replace("STRANDS=", "")
    strand1 = strands[0]
    strand2 = strands[1]

    alt1, alt2 = generate_breakend_alt(chr1, chr2, end1, end2, strand1, strand2)
    
    info = [i for i in info if not i.startswith("CHR2")]
    info = [i for i in info if not i.startswith("END")]
    info = [i for i in info if not i.startswith("SVLEN")]
    info = [i for i in info if not i.startswith("SVTYPE")]
    info.append("MATEID=" + id2)
    info.append("SVTYPE=BND")

    line['INFO'] = ';'.join(info)
    line['ALT'] = alt1

    line2 = copy.deepcopy(line)
    line2['CHROM'] = chr2
    line2['POS'] = end2
    line2['ALT'] = alt2
    line2['ID'] = id2
    info2 = line2['INFO'].split(';')
    info2 = [i for i in info2 if not i.startswith("MATEID")]
    info2.append("MATEID=" + id1)
    line2['INFO'] = ';'.join(info2)

    if chr1 < chr2:
        pos_tup = (chr1, end1, chr2, end2)
    else:
        pos_tup = (chr2, end2, chr1, end1)

    return line, line2, pos_tup


def fix_single_bnd(line):
    info = line['INFO']
    info = info.split(';')

    chr1 = line['CHROM']
    end1 = line['POS']

    chr2 = next(i for i in info if i.startswith("CHR2"))
    chr2 = chr2.replace("CHR2=", "")
    end2 = next(i for i in info if i.startswith("END"))
    end2 = end2.replace("END=", "")

    strands = next(i for i in info if i.startswith("STRANDS"))
    strands = strands.replace("STRANDS=", "")
    strand1 = strands[0]
    strand2 = strands[1]

    alt1, alt2 = generate_breakend_alt(chr1, chr2, end1, end2, strand1, strand2)

    line['ALT'] = alt1

    return line


#This function writes the final vcf file
def write_vcf(vcf, header, out_vcf):

    # Sort by position
    vcf = sorted(vcf, key=lambda k: (k['CHROM'], int(k['POS'])))

    with open(os.path.join(out_vcf), 'w') as vcf_file:
        # Write the header
        vcf_file.write(''.join(header))
        
        # Add the variants
        for variant in vcf:
            vcf_file.write('\t'.join([variant['CHROM'], str(variant['POS']),
                variant['ID'], variant['REF'], variant['ALT'], variant['QUAL'],
                variant['FILTER'], variant['INFO'], variant['FORMAT'],
                variant['SAMPLE']]) + '\n')


def main():
    args = parse_args()

    vcf, header = read_vcf_file(args.in_vcf, args.keep_tra)

    header = add_to_header(header, args.contigs)
    
    write_vcf(vcf, header, args.out_vcf)


if __name__ == "__main__":
    print("Hello, fixing your VCF now...")
    main()
