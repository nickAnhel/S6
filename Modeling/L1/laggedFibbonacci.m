function retval = laggedFibbonacci(n)
  a = 63;
  b = 31;

  retval = multiplicativeCongruenceGenerator(n);

  for i = (a + 1):n
    if (retval(i - a) >= retval(i - b))
      retval(i) = retval(i - a) - retval(i - b);
    else
      retval(i) = retval(i - a) - retval(i - b) + 1;
    endif
  endfor
endfunction

