import pandas
import re

#Evaluación REGREX
def evaluate_Fx(str_equ, valX):
  x = valX
  #strOut = str_equ
  strOut = str_equ.replace("x", '*(x)')
  strOut = strOut.replace("^", "**")
  out = eval(strOut)
  print(strOut)
  return out

#Deferencias finitas para derivadas
def evaluate_derivate_fx(str_equ, x, h):
  strOut = str_equ.replace("x", '*(x + h)')
  strOut = strOut.replace("^", "**")
  strOut = "-4*(" + strOut + ")"
  out = eval(strOut)
  
  strOut = str_equ.replace("x", '*(x + 2*h)')
  strOut = strOut.replace("^", "**")
  out = out + eval(strOut)
  
  strOut = str_equ.replace("x", '*(x)')
  strOut = strOut.replace("^", "**")
  strOut = "3*(" + strOut + ")"
  out = out + eval(strOut)
  
  out = -out/(2*h)
  print(out)
  return out

#Resolverdor de Newton
def newtonSolverX(x0, f_x, eps):
  x0 = float(x0)
  eps = float(eps)
  xn = x0
  error = 1
  arrayIters = []
  arrayF_x = []
  arrayf_x = []
  arrayXn = []
  arrayErr = []
  
  i = 0
  h = 0.000001
  while(error > eps):
    print("...")
    x_n1 = xn - (evaluate_Fx(f_x, xn)/evaluate_derivate_fx(f_x, xn, h))
    error = abs(x_n1 - xn)
    i = i + 1
    xn = x_n1
    arrayIters.append(i)
    arrayXn.append(xn)
    arrayErr.append(error)
    solution = [i, xn, error]

  print("Finalizo...")
  TableOut = pandas.DataFrame({'Iter':arrayIters, 'Xn':arrayXn, 'Error': arrayErr})
  return TableOut

def add(a, b):
  a = int(a)
  b = int(b)
  resultado = a + b
  return "El resultado es: " + str(resultado)

#Diferencias finitas 2 puntos
def dif_fin_dos_puntos(fx, x, h):
  x = float(x)
  h = float(h)
  import math
  valFx = eval(fx)
  fxp1 = fx.replace('x', '(x + h)') #Create f(x+h)
  fxp2 = fx.replace('x', '(x - h)') #Create f(x-h)
  fxp1r = fx.replace('x', '(x + (h/2))') #Create f(x+h)
  fxp2r = fx.replace('x', '(x - (h/2))') #Create f(x-h)
  
  #Evaluate the strings as code
  valFhx1 = eval(fxp1) 
  valFhx2 = eval(fxp2)
  valFhx1r = eval(fxp1r) 
  valFhx2r = eval(fxp2r)
  
  #Create f'(x)
  out_1 = ((valFhx1 - valFx)/h)
  out_2 = ((valFx - valFhx2)/h)
  out_3 = ((valFhx1 - valFhx2)/(2*h))
  out_4 = ((valFhx1r - valFhx2r)/h)
  out_5 = (((4*out_4) - out_3)/3)
  out = {"FDF":out_1, "BDF":out_2, "CDF":out_3, "Richardson": out_5}
  return out
  
def dif_fin_tres_puntos(fx, x, h):
  x = float(x)
  h = float(h)
  valFx = eval(fx)
  fxp1 = fx.replace('x', '(x + h)') #Create f(x+h)
  fxp2 = fx.replace('x', '(x - h)') #Create f(x-h)
  fxp1_2 = fx.replace('x', '(x + (2*h))')
  fxp2_2 = fx.replace('x', '(x - (2*h))')
  fxpr = fx.replace('x', '(x + (h/2))')
  
  #Evaluate the strings as code
  valFhx1 = eval(fxp1) 
  valFhx2 = eval(fxp2)
  valFhx1_2 = eval(fxp1_2) 
  valFhx2_2 = eval(fxp2_2)
  valFhxr = eval(fxpr)
  
  #Create f'(x)
  out_1 = (((-3*valFx) + (4*valFhx1) - valFhx1_2)/(2*h))
  out_2 = (((3*valFx) - (4*valFhx2) + valFhx2_2)/(2*h))
  out_3 = (((-3*valFx) + (4*valFhxr) - valFhx1)/h)
  out_4 = (((4*out_3) - out_1)/3) 
  out = {"FDF":out_1, "BDF":out_2, "Richardson":out_4}
  return out

#Integral trapezoide
def trapezoide(fx,a,b,n):
    import math
    
    a=a.replace('pi', str(math.pi))
    a=eval(a)
    
    b=b.replace('pi', str(math.pi))
    b=eval(b)

    n = float(n)
    
    # Compute the length of each trapezoid
    h = (b-a)/n

    # Evaluate the starting point and add it to the total summation S
    x = a
    fx = fx.replace('e', str(math.e))
    fx = fx.replace('pi', str(math.pi))
    fx = fx.replace('sin', 'math.sin')
    
    S = eval(fx)

    # Loop to compute all the values of xi for i = 1 to i = n-1. Then add it to the total summation S
    i = 1
    while (i < n):
      x = a + h*i
      S = S + 2*eval(fx)
      i = i + 1
    
    # Evalaute the ending point and add it to the total summation S
    x = b
    S = S + eval(fx)

    # Finalize the the approximation by multiplying the total summation S times h/2
    S = S*h/2
    return S

#Integral Simpson
def simpson(fx,a,b,n):
    import math
    # Compute the length of each trapezoid
    
    a=a.replace('pi', str(math.pi))
    a=eval(a)
    
    b=b.replace('pi', str(math.pi))
    b=eval(b)
    
    n = float(n)

    h = (b-a)/n

    # Evaluate the starting point and add it to the total summation S
    x = a
    fx = fx.replace('e', str(math.e))
    fx = fx.replace('pi', str(math.pi))
    fx = fx.replace('sin', 'math.sin')
    S = eval(fx)

    # Loop to compute all the values of xi for i = 1 to i = n-1. Then add it to the total summation S
    i = 1
    while (i < n):
        x = a + h*i
        if (i%2 != 0):
            S = S + 4*eval(fx)
        else:
            S = S + 2*eval(fx)

        i = i + 1


    # Evalaute the ending point and add it to the total summation S
    x = b
    S = S + eval(fx)

    # Finalize the the approximation by multiplying the total summation S times h/2
    S = S*h/3
    return S


# Incremental Search Method
def ISM(fx,x0,dx):
    import numpy as np
    import math

    x0=float(x0)
    dx=float(dx)

    fx = fx.replace('pi', str(math.pi))
    fx = fx.replace('sin', 'math.sin')
    fx = fx.replace('e', str(math.e))

    y0 = 1
    y1 = 1
    #print(x0)
    x = x0
    
    for n in range(1,100):
        x = x0
        y0 = eval(fx)
        x = x0 + dx
        y1 = eval(fx)
        if (y0*y1 < 0):
            break  
        else:
            x0 = x
            
    return x


# Bisection Method
def bisection(fx, e, x1, x2):
    import numpy as np
    import math

    e=float(e)
    x1=float(x1)
    x2=float(x2)

    epsilon = e
    fx = fx.replace('pi', str(math.pi))
    fx = fx.replace('sin', 'math.sin')
    fx = fx.replace('e', str(math.e))  

    x = x1
    y1 = eval(fx)
    x = x2
    y2 = eval(fx)

    if (y1*y2 < 0):
        for n in range(1,100):
            x = x1
            y1 = eval(fx)
            x3 = (x1+x2)/2
            x = x3
            y3 = eval(fx)
            if (y1*y3 < 0):
                x2 = x3
            else:
                x1 = x3
            if (abs(x1-x2)< epsilon):
                break
    return x



# Newton-Raphson Method
def NR(fx, e, x0):
  import numpy as np
  import math
  
  fx = fx.replace('pi', str(math.pi))
  fx = fx.replace('sin', 'math.sin')
  fx = fx.replace('e', str(math.e))
  
  def dif_fin_tres_puntos(fx, x, h):
      import math
      x = float(x)
      h = float(h)
      valFx = eval(fx)
      fxp1 = fx.replace('x', '(x + h)') #Create f(x+h)
      fxp2 = fx.replace('x', '(x - h)') #Create f(x-h)
      fxp1_2 = fx.replace('x', '(x + (2*h))')
      fxp2_2 = fx.replace('x', '(x - (2*h))')
      fxpr = fx.replace('x', '(x + (h/2))')

      #Evaluate the strings as code
      valFhx1 = eval(fxp1) 
      valFhx2 = eval(fxp2)
      valFhx1_2 = eval(fxp1_2) 
      valFhx2_2 = eval(fxp2_2)
      valFhxr = eval(fxpr)

      #Create f'(x)
      out_1 = (((-3*valFx) + (4*valFhx1) - valFhx1_2)/(2*h))
      out_2 = (((3*valFx) - (4*valFhx2) + valFhx2_2)/(2*h))
      out_3 = (((-3*valFx) + (4*valFhxr) - valFhx1)/h)
      out_4 = (((4*out_3) - out_1)/3) 
      return out_4
  
  f = str(fx)

  x = float(x0)
  epsilon = float(e)

  f_x = eval(f)
  h = 0.00001
  derivative = (dif_fin_tres_puntos(f, x, h))
  x_i_plus = x - (f_x/derivative)
  x_abs = abs(x - x_i_plus)


  while x_abs > epsilon:
      x = x_i_plus
      f_x = eval(f)
      derivative = (dif_fin_tres_puntos(f, x, h))
      x_i_plus = x - (f_x/derivative)
      x_abs = abs(x - x_i_plus)
  return x_i_plus



#FONC, SONC, SOSC
def conditions(InFun, Vars, Fd, Sd, Td):
    import numpy as np
    import re

    #####FONC#####
    xs=''
    names=[]
    values=[]
    
    #Get literals from input function
    xs = re.split("[^a-zA-Z]*",InFun)
    xs = list(dict.fromkeys(xs))
    xs = [i for i in xs if i]
    
    #Declare variables from input Vars
    Vars.split(',')
    names = re.split("[^a-zA-Z]*",Vars) #get letters only
    names = list(dict.fromkeys(names)) #convert to list
    names = [i for i in names if i] #remove empty elements
    
    values = re.sub(r"[a-z][=]+", "", Vars, re.I) #remove literals
    values = re.sub(r"\s+", "", values,flags=re.UNICODE) #remove all empty spaces
    values = list(values.split(",")) #convert to list
    values = [eval(i) for i in values] #evaluate each member of lists to accept divisions

    for a,b in zip(names, values): #create variables
        globals()[a] = b
    
    if xs == names:
        print('Variables OK')
    else:
        print('Variables Not OK')
        print ('Literals found in function: ' + str(xs))
        print ('Variables provided: ' + str(names))
        return
        
    #Split input function string and convert to a list
    fs = InFun.split(',')
    grad_vec = []
    for i in fs:
        fi = eval(i)
        grad_vec.append(fi)


    norm = np.sqrt(sum([x**2 for x in grad_vec]))

    #####SOSC###
    #Define variable values
    x=values[0]
    
    if (len(values)>1):
        y=values[1]
    else:
        y=0

    #Define input of the hessian matrix
    input_1 = Fd
    input_1 = list(input_1.split(","))
    input_1 = [eval(i) for i in input_1 if i]
    input_1 = ",".join(str(bit) for bit in input_1)
    input_2 = Sd
    input_2 = list(input_2.split(","))
    input_2 = [eval(i) for i in input_2 if i]
    input_2 = ",".join(str(bit) for bit in input_2)
    input_3 = Td
    input_3 = list(input_3.split(","))
    input_3 = [eval(i) for i in input_3 if i]
    input_3 = ",".join(str(bit) for bit in input_3)

    
    def parse_input(instring, x, y):
        xs = []
        for i in instring.split(','):
            if 'x' in i and 'y' in i:
                xs.append(x * y * float(i.replace('x', '').replace(y, '')))
            elif 'x' in i:
                xs.append(x * float(i.replace('x', '')))
            elif 'y' in i:
                xs.append(y * float(i.replace('y', '')))
            else:
                xs.append(float(i))
        return xs

    #Use the function to parse the input
    input_1 = input_1.replace("*","")
    input_2 = input_2.replace("*","")
    input_3 = input_3.replace("*","")
    hess = [parse_input(s, x, y) for s in (input_1, input_2, input_3)]
    hess = np.matrix([hess[0], hess[1], hess[2]]) #Convert to a matrix

    #Print Hessian
    print('Hessian: ',"\n", hess)

    #Calculate and print Eigenvalues
    eigenvals = np.linalg.eigvals(hess)
    print('Eigenvalues: ', "\n",eigenvals)

    #Compare to WolframAlpha https://www.wolframalpha.com/widgets/gallery/view.jsp?id=9e184384a47cc694e9cae76ab5a935e1
    eig_res = []
    for i in eigenvals:
        if (i > 0):
            eig_res.append(1)
        elif (i == 0):
            eig_res.append(0)
        else:
            eig_res.append(-100)

# PRINT RESULTS            
    t=''
    
    if (norm == 0):
        print('Satisface FONC')
        t='Satisface FONC | \n'
    else:
        print('No satisface FONC')
        print('Norm= ' + str(norm))
        t='No satisface FONC | \n'
            
    if (sum(eig_res) > 0):
        print('Satisface SONC')
        t= t + 'Satisface SONC | \n'
    else:
        print('No Satisface SONC')
        t= t + 'No satisface SONC | \n'
    
    if (np.all(eigenvals>=0)==True) and (sum(eig_res) > 0):
        print('Satisface SOSC')
        t= t + 'Satisface SOSC | \n'
    else:
        print('No satisface SOSC')
        t= t + 'No satisface SOSC'
    
    return t
    

# STEEPEST DESCENT
def sd(eq, X, epsilon):
  
  import numpy as np
  from math import sqrt
  epsilon = float(epsilon)

  X = X.split(',')
  X = [int(i) for i in X]

  phi = (1.0 + sqrt(5.0))/2.0

  #Transform variables
  def conditions(eq):
      import numpy as np
      import re
      InFun = eq
      InFun = InFun.split(',')
      InFun = list(InFun)

      xs=''
      names=[]
      values=[]
      
      #Get literals from input function
      for i in range(len(InFun)):
          xs = re.split("[^a-zA-Z]*",InFun[i])
          xs = list(dict.fromkeys(xs))
          xs = [i for i in xs if i]
       
      names = list(dict.fromkeys(xs)) #convert to list
      names = [i for i in names if i] #remove empty elements
      
      Vars = InFun[0]
      counter = 0
      for i in names:
        Vars = Vars.replace(i,'x'+ '['+str(counter)+']')
        counter = int(counter) + 1
      return Vars

  funfinal = conditions(eq)

  def equation(x):
        return eval(funfinal)

  def lr_searcher(X, d, prev_val, lower, upper, epsilon):

      x1 = upper - ((phi - 1)*(upper - lower))
      x2 = lower + ((phi - 1)*(upper - lower))
      val = x1

      param2 = X - np.dot(x2, d)
      param2 = param2.tolist()

      param1 = X - np.dot(x1, d)
      param1 = param1.tolist()

      if equation(param2) < equation(param1):
          if x1 > x2:
              upper = x1
          else:
              lower = x1

      else:
          if x2 > x1:
              upper = x2
          else:
              lower = x2

      if abs(prev_val - val) <= epsilon:
          return val
      else:
          return lr_searcher(X, d, val, lower, upper, epsilon)

  def derivate(f, X):
      h = 0.0000001
      delf = []

      for i in range(len(X)):
          E = np.zeros(len(X))
          E[i] = h
          vals = X + E
          delf.append((f(vals) - f(X))/h)

      return delf


  def difference(X, Y):
      total = 0

      for i in range(len(X)):
          total = total + abs(X[i] - Y[i])
      total = total / len(X)


      return total


  def steepest_descent(X, epsilon):

      while True:
          d = derivate(equation, X)
          x_prev = X
          learning_rate = lr_searcher(X, d, 1, -10, 10, 0.0001)
          X = X - np.dot(learning_rate, d)
          X = X.tolist()

          if difference(x_prev, X) < epsilon:
              return x_prev

      return x_prev

  Points = steepest_descent(X, epsilon)
  Minimal = equation(Points)
  
  Points = [round(i,6) for i in Points]

  results = 'La función tiene un mínimo en los puntos ~' + str(Points) +'. Donde el valor mínimo de la función es: ' + str(round(Minimal,6))
  
  return results
