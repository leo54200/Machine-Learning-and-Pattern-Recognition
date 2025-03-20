import numpy
#Point a
def array2D(m, n):
        #x = numpy.float64(numpy.arange(n))        
        x = numpy.array(numpy.arange(n), dtype = numpy.float64)  
        #y = numpy.float64(numpy.arange(m))              
        y = numpy.array(numpy.arange(m), dtype = numpy.float64)
        return x.reshape(1, n) * y.reshape(m, 1)

def normalizationPercolumn(arr):
        sum = arr.sum(0)
        '''for i in range(len(sum)):
                if sum[i] == 0:
                        sum[i] = 1
        '''
        arr = arr / sum
        return arr

def normalizationPerRow(arr):
        sum = arr.sum(1).reshape(len(arr), 1)
        '''for i in range(len(sum)):
                if sum[i] == 0:
                        sum[i] = 1
        '''
        arr = arr / sum
        return arr

def noNegatives(arr):
        r = numpy.copy(arr)
        r[r < 0] = 0
        return r

def sumMatrixProduct(x, y):
        return numpy.sum(numpy.dot(x, y))


result_a = array2D(3, 4)
print("Point A\n" + str(result_a))

result_b = normalizationPercolumn(numpy.array([[1, 2, 6, 4], [3, 4, 3, 7], [1, 4, 6, 9]], dtype = numpy.float64))
print("Point B\n" + str(result_b))

result_c = normalizationPerRow(numpy.array([[1.0, 3.0, 1.0], [2.0, 4.0, 4.0], [6.0, 3.0, 6.0]], dtype = numpy.float64))
print("Point C\n" + str(result_c))

result_d = noNegatives(numpy.array([[1.0, 3.0, -1.0], [-2.0, 4.0, 4.0], [6.0, 3.0, 6.0]], dtype = numpy.float64))
print("Point D\n" + str(result_d))

result_e = sumMatrixProduct(result_d, result_c)
print("Point E\n" + str(result_e))