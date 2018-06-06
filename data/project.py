import numpy as np


def ConvFtoMatrix(f):
    """
    :param: Input .txt File
    :return: Number Matrix
    """
    f1 = open(f, 'r')
    l = [line.split(',')for line in f1 if line.strip() != "" ]
    for i in range(len(l)):
        d = []
        for j in range(len(l[i])):
            d.append(float(l[i][j]))

        l[i] = d

    return l

def Transpose(m):
    """
    :param: Number Matrix
    :return: Transpose Of that Matrix
    """
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def MatrixMult (a, b):
    """
    :param a: Matrix
    :param b: Matrix
    :return: Multiplication of both the Matrices
    """
    zip_b = zip(*b)
    zip_b = list(zip_b)
    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
                 for col_b in zip_b] for row_a in a]
def MatrixInv (m):
     """
    :param m: Matrix
    :return: inverse of the matrix
    """
     mnv= np.linalg.inv (m)
     return mnv

def NormalEq (x,y):
	"""
	:param x: Matrix of values of features
	:param y: Matrix of results
	:return: Theta values for cost function
	"""
	t=MatrixMult(MatrixMult(MatrixInv(MatrixMult(Transpose(x),x)),Transpose(x)),y)

	return t


def Predict (m,y,f):
	"""
	:param m: Matrix of values of features
	:param y: Matrix of results
	:param f: Matrix to predict
	:return:  value
	"""

	M=ConvFtoMatrix(m)
	Y=ConvFtoMatrix(y)
	F=ConvFtoMatrix(f)
	t=NormalEq(M,Y)
    
	ans=0.0
	for i in range(len(t)):
		ans+=t[i][0]*(F[i][0])

	return ans





"""
f="f.txt"
y="y.txt"
print(Predict(k,y,f))
"""

a1=input("Enter your Price\n")
a=input("Enter Your Choice :\n 0.all 1. Bandra 2.SantaCruz 3.Andheri 4.South Bombay 5.Virar\n")
k="test.txt"

if a==1 or a==0:
	f="test.txt"
	y="y.txt"
	print(Predict(k,y,f))
if a==2 or a==0:
	f="test.txt"
	y="y.txt"
	print(Predict(k,y,f))
if a==3 or a==0:
	f="test.txt"
	y="y.txt"
	print(Predict(k,y,f))
if a==4 or a==0:
	f="test.txt"
	y="y.txt"
	print(Predict(k,y,f))
if a==5 or a==0:
	f="test.txt"
	y="y.txt"
	print(Predict(k,y,f))
