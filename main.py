import time

print("this is the half life calculator, enter '?' if you don't know what a field is.")

"""
This is the half life calculator.
5 fields

- half life time (h)
- original mass (M0)
- ending mass (M) 
- time passed (t)
- number of half lives (n)

Equations:
  m_o = m * 2^n
  n = t/h

Your answer, along with all of the other data, will be printed out for display.

"""

def calc_exponent(m_o, m):
  power = m_o/m
  n = 0

  while(power > 1):
    power /= 2
    n += 1
    # print("power", power)
  
  # print("exponent: ", n)
  return n


m_o = input("Enter original mass: ")

m = input("Enter remaining mass: ")

t = input("Enter total time passed: ")

h = input("Enter half life time: ")


try: 
  m_o = float(m_o)
except:
  pass
try: 
  m = float(m)
except:
  pass
try: 
  t = float(t)
except:
  pass
try: 
  h = float(h)
except:
  pass

try:
  n = t/h # solivng for m or m_o
except:
  n = "dead"

# print("hi")
if(m_o == '?'):
  print("missing m_o? We gotcha")
  m_o = m * (2**n)

elif (m == '?'):
  print("missing m? We gotcha")

  m = m_o / (2**n)

elif (t == '?'):
  # calculate the exponent (n)
  print("missing t? We gotcha")

  n = calc_exponent(m_o, m)

  # calculate for t

  t = n * h

elif (h == '?'):
  # calculate the exponent (n)
  print("missing h? We gotcha")

  n = calc_exponent(m_o, m)

  # calculate for h

  h = t/n
else:
  print("ain't missing nothing")

print("analyzing results...")
time.sleep(1.5)
print("")
print("----- printing info -----")
print("")
print("Original mass: ", m_o)

print("Remaining Mass: ", m)

print("Total Time: ", t)

print("Half Life: ", h)

print("Number of half lives: ", n)

print("Remember to put units!!")