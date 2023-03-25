import csv
from django.shortcuts import render
def get_last_row(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        return rows[-1]
def data(request):
    filename1 = '/home/a/Desktop/project/dash_board/server_side/PORT6000.csv'
    filename2 = '/home/a/Desktop/project/dash_board/server_side/PORT6001.csv'
    filename3 = '/home/a/Desktop/project/dash_board/server_side/PORT6002.csv'
    filename4 = '/home/a/Desktop/project/dash_board/server_side/PORT6003.csv'
    last_row_node1 = get_last_row(filename1)
    last_row_node2 = get_last_row(filename2)
    last_row_node3 = get_last_row(filename3)
    last_row_node4 = get_last_row(filename4)
    context = {'last_row_node1': last_row_node1,
               'last_row_node2': last_row_node2,
               'last_row_node3': last_row_node3,
               'last_row_node4': last_row_node4}
    return render(request, 'list.html', context)
