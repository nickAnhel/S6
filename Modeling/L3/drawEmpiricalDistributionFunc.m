function drawEmpiricalDistributionFunc(data, p_title)
  [f, x] = ecdf(data);

  figure();
  plot(x, f);
  title(p_title);
  xlabel("x");
  ylabel("F(x)");
  grid on;
endfunction
