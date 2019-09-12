
folder_queue = ['d1','d2','d3','d4','d5','d6','d7','d8','d9','d10','d11','d12','d13','d14','d15','d16']
tmp = []
max_q_length = 5
if len(folder_queue) > max_q_length:
#    with open('output.csv', 'w') as csvfile:
#        writer = csv.writer(csvfile)
#        for i in range((len(folder_queue) - max_q_length)):
#            tmp.append(folder_queue[max_q_length + i])
#            writer.writerow(folder_queue[max_q_length + i])

    with open("tmp_q.txt", "a") as fp:
        for i in range((len(folder_queue) - max_q_length)):
            fp.write(folder_queue[max_q_length + i]+'\n')
