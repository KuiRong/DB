import os

folder_queue = []

max_q_length = 5
tmp_str=""
tmp_str_offset = 0
total_size = 0
file_offset = 0
with open("tmp_q.txt", "rw") as fp:
    statinfo = os.stat('tmp_q.txt')
#    print statinfo.st_size
#    fp.seek(16,0)
    fp.seek(file_offset,0)
    for i in range(max_q_length):
        line = fp.readline().strip()
        folder_queue.append(line)
        tmp_str += str(line)
        tmp_str_offset += 1
    print(folder_queue)
#    print(len(tmp_str)+tmp_str_offset)
#    print(fp.tell())
    file_offset = fp.tell()

