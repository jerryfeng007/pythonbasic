""" 图案1
*
**
***
****
*****
"""
for i in range(1, 6):
    print('*' * i)


"""图案2
    *
   **
  ***
 ****
*****
"""
for i in range(1, 6):
    print(' ' * (6-1-i) + '*' * i)


"""图案3
    *
   ***
  *****
 *******
*********
"""
for i in range(1, 6):
    print(' ' * (6-1-i) + '*' * (i*2-1) + ' ' * (6-1-i))
