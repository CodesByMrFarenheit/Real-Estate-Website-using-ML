from django.shortcuts import render
from main import forms
import numpy as np
# Create your views here.

def index(request):
    return render(request,'main/index.html')


def formNew(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
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

            	t=NormalEq(M,Y)
            	print("t lenght"+str(len(t)))
            	ans=0.0

            	for i in range(len(t)):
            		ans+=t[i][0]*(f[i])

            	return ans
            if form.cleaned_data['Planet']=="Naboo":
                k="data/Naboo.txt"
                f=(1,form.cleaned_data['FSI'],form.cleaned_data['BHK'])
                y="data/y.txt"
                ans=round(Predict(k,y,f))

            if form.cleaned_data['Planet']=="Endor":
                k="data/Endor.txt"
                f=(1,form.cleaned_data['FSI'],form.cleaned_data['BHK'])
                y="data/y.txt"
                ans=round(Predict(k,y,f))

            if form.cleaned_data['Planet']=="Tatooine":
                k="data/Tatooine.txt"
                f=(1,form.cleaned_data['FSI'],form.cleaned_data['BHK'])
                y="data/y.txt"
                ans=round(Predict(k,y,f))

            if form.cleaned_data['Planet']=="Hoth":
                k="data/Hoth.txt"
                f=(1,form.cleaned_data['FSI'],form.cleaned_data['BHK'])
                y="data/y.txt"
                ans=round(Predict(k,y,f))

            if form.cleaned_data['Planet']=="Alderaan":
                k="data/Alderaan.txt"
                f=(1,form.cleaned_data['FSI'],form.cleaned_data['BHK'])
                y="data/y.txt"
                ans=round(Predict(k,y,f))
            return render( request , 'main/ans.html' , {'ans':ans} )







    return render(request,'main/forms.html',{'form':form})
