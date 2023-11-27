import random

num_repeats = 1000

example_records = [
"[NEW] tcp 6 120 SYN_SENT src=10.1.2.3 dst={dst1} sport=47800 dport=21 [UNREPLIED] src=203.0.113.47 dst={dst2} sport=21 dport=47800 helper=ftp",
"[UPDATE] tcp 6 60 SYN_RECV src=10.1.2.3 dst={dst1} sport=47800 dport=21 src=203.0.113.47 dst={dst2} sport=21 dport=47800 helper=ftp",
"[UPDATE] tcp 6 432000 ESTABLISHED src=10.1.2.3 dst={dst1} sport=47800 dport=21 src=203.0.113.47 dst={dst2} sport=21 dport=47800 [ASSURED] helper=ftp"
]

simulated_records = []

for _ in range(num_repeats):
    random_dst1 = "203.0.113." + str(random.randint(1,5))
   # print(random_dst1)
    random_dst2 = "198.52.100." + str(random.randint(1, 5))
#print(random_dst2)
    for record in example_records:
        record = record.format(dst1=random_dst1, dst2=random_dst2)
        simulated_records.append(record)

output_file = "simulated_records.txt"
with open(output_file, "w") as file:
    for record in simulated_records:
        file.write(record + "\n")

print(f"{num_repeats} sets of example records have been generated and saved to {output_file}.")
