import numpy


class Mixer(object):
    """Algrebraic description of a mixer with a matrix

    The linking matrix sastisfies the Melvin & Tufillaro
    orientation convention DOI
    """

    def __init__(self, size=1, content='0'):
        self.size = size
        self.matrix = numpy.matrix(content)

    def __str__(self):
        return self.matrix.__str__()

    def find(self, array, val):
        i = 0
        while array[i] != val:
            i += 1
        return i

    def get(self, i, j):
        return self.matrix.item(i-1, j-1)

    def concatenate(self, A, B):
        a = A.size
        b = B.size
        a_s = numpy.zeros(a*b)
        for i in range(1, a*b+1):
            a_s[i-1] = i
        # print('a_s', a_s)
        a_exp = numpy.zeros([a*b, a*b], dtype=int)
        for i in range(1, a+1):
            for j in range(1, a+1):
                for k in range(1, b+1):
                    for l in range(1, b+1):
                        a_exp[(i-1)*b+k-1, (j-1)*b+l-1] = A.get(i, j)
        # print(a_exp)
        a_e = numpy.zeros(a*b)
        for i in range(1, a*b+1):
            pos = 0
            neg = 0
            for j in range(i+1, a*b+1):
                if a_exp[i-1, j-1] % 2 == 1:
                    pos = pos+1
            for j in range(1, i):
                if a_exp[i-1, j-1] % 2 == 1:
                    neg = neg+1
            a_e[i+pos-neg-1] = i
        # print('a_e', a_e)
        b_s = numpy.zeros(a*b)
        k = 1
        for j in range(1, b+1):
            for i in range(1, a+1):
                #  print(i, j)
                b_s[k-1] = a_e[(i-1)*b+j-1]
                k += 1
        # print('b_s', b_s)
        a_tra = numpy.zeros([a*b, a*b], dtype=int)
        for k in range(1, a*b):
            l = self.find(b_s, a_e[k-1])
            for p in range(k+1, a*b+1):
                q = self.find(b_s, a_e[p-1])
                if q < l:
                    i = self.find(a_s, a_e[k-1])
                    j = self.find(a_s, a_e[p-1])
                    a_tra[i, j] = 1
                    a_tra[j, i] = 1
        # print(a_tra)
        b_exp = numpy.zeros([a*b, a*b], dtype=int)
        for i in range(1, a+1):
            for j in range(1, a+1):
                if A.get(i, i) % 2 == 0 and A.get(j, j) % 2 == 0:
                    for k in range(1, b+1):
                        for l in range(1, b+1):
                            b_exp[(i-1)*b+k-1, (j-1)*b+l-1] = B.get(k, l)
                elif A.get(i, i) % 2 == 0 and A.get(j, j) % 2 == 1:
                    for k in range(1, b+1):
                        for l in range(1, b+1):
                            b_exp[(i-1)*b+k-1, (j-1)*b+l-1] = B.get(k, b-l+1)
                elif A.get(i, i) % 2 == 1 and A.get(j, j) % 2 == 0:
                    for k in range(1, b+1):
                        for l in range(1, b+1):
                            b_exp[(i-1)*b+k-1, (j-1)*b+l-1] = B.get(b-k+1, l)
                else:
                    for k in range(1, b+1):
                        for l in range(1, b+1):
                            b_exp[(i-1)*b+k-1, (j-1)*b+l-1] = B.get(b-k+1, b-l+1)
        result = a_exp+a_tra+b_exp
        return Mixer(a*b, numpy.copy(result))

    def concatenate_before(self, C):
        return self.concatenate(self, C)

    def concatenate_after(self, C):
        return self.concatenate(C, self)

    def export_to_matrix_and_array(self):
        array = numpy.zeros(self.size)
        for i in range(1, self.size+1):
            positive = 0
            negative = 0
            for j in range(1, i):
                if self.get(i, j) % 2 == 1:
                    negative += 1
            for j in range(i+1, self.size+1):
                if self.get(i, j) % 2 == 1:
                    positive += 1
            # array[i+positive-negative-1] = self.size - i + 1
            array[i-1] = self.size - (i+positive-negative) + 1
        tab = numpy.copy(array)
        matrix_array = numpy.copy(self.matrix)
        swapped = True
        n = self.size
        while swapped:
            swapped = False
            for i in range(1, n):
                if tab[i-1] < tab[i]:
                    k = self.find(array, tab[i-1])
                    l = self.find(array, tab[i])
                    matrix_array[k, l] += 1
                    matrix_array[l, k] += 1
                    temp = tab[i]
                    tab[i] = tab[i-1]
                    tab[i-1] = temp
                    swapped = True
            n -= 1
        print(matrix_array)
        print(array)

    def import_from_matrix_and_array(sefl, matrix_array, array):
        # TODO
        pass
