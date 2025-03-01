function retval = multiplicativeCongruenceGenerator(n)
  a = 7^5;
  c = 0;
  m = 2^32 - 1;

  retval = zeros(1, n);
  retval(1) = 2^(-52);

  for i = 2:n
    retval(i) = (
      mod(a * retval(i-1) + c, m) - floor(mod(a * retval(i-1) + c, m))
    );
  endfor
endfunction

