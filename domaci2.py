import pysam

#pysam.index("merged-tumor.bam")

samfile = pysam.AlignmentFile("merged-tumor.bam", "rb")
index_stats = samfile.get_index_statistics()


num_unmapped = 0
num_reads = 0

num_zero_map_Q = 0
avg_map_Q = 0

for i, read in enumerate(samfile.fetch()):
    num_reads = num_reads + 1
    if i == 0:
        print("flag of first read:{}".format(read.flag))
    avg_map_Q = avg_map_Q + read.mapping_quality
    if read.mapping_quality == 0:
        num_zero_map_Q = num_zero_map_Q + 1 

avg_map_Q_without_zeros = avg_map_Q/(num_reads-num_zero_map_Q)
avg_map_Q = avg_map_Q/num_reads


for stat in index_stats:
    if stat.unmapped != 0:
        num_unmapped = num_unmapped + 1
    

print("number of reads:{}".format(num_reads))
print("number of unmapped reads:{}".format(num_unmapped))
print("number of reads with mapping quality = 0:{}".format(num_zero_map_Q))
print("average mapping quality:{}".format(avg_map_Q))
print("average mapping quality without the zeros:{}".format(avg_map_Q_without_zeros))