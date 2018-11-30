"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for i,rows in enumerate(texts):
        if i==1:
            row=rows
    print("First record of texts, "+row[0]+" texts "+row[1]+" at time "+row[2])
              

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
 for i,rows in enumerate(calls):
        if i==1:
            row=rows
    print("Last record of calls, "+row[0]+" calls "+row[1]+" at time "+row[2]+", lasting "+ row[3]+" seconds")

"""
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

