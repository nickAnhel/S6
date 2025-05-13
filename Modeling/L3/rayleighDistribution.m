function retval = rayleighDistribution(n)
  r1 = rand(1, n);
  s = 1;

  retval = [];

  for i = 1:n
    if (r1(i) >= 0)
      retval(i) = ( -2 * s^2 * log( r1(i) ) ) .^ ( 1/2 );
    end
  end
endfunction
