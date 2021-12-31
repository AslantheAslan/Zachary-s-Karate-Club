import numpy as numpy

def text_to_array(self, path):

    my_file = open(path, "r")
    content = my_file.read()

    def split(word):
        return [char for char in word]

    content_list = content.split("\n")
    my_file.close()

    final = []
    for i in range(len(content_list)):
        final.append(split(content_list[i]))

    return numpy.asarray(final)

def int_to_array(path):
    my_array = numpy.loadtxt(path, dtype="uint8", delimiter=' ')
    return my_array

print(int_to_array('edges.txt'))
print(int_to_array('capacities.txt'))
print(int_to_array('nodes.txt').shape)