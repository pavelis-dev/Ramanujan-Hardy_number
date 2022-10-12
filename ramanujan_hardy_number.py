total = 0
for n in range(1, 34):
    for k in range(1, 34):
        for m in range(1, 34):
          for t in range(1, 34):
              if n**3 + k**3 == m**3 + t**3 and n!=t and k!=m and k!=t  and  n>k and m>t and n>m:
                n, k == m, t
                total += 1
                print('n =', n, 'k =', k, 'm =', m, 't=',  t, '=', n**3 + k**3)
print('Общее количество натуральных решений =', total)


