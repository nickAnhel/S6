function drawPlanarDistribution(data, p_title)
  x = data(1:2:end-1);
  y = data(2:2:end);

  figure();
  plot(x, y, ".");
  title(p_title);
  xlabel("R_n");
  ylabel("R_{n+1}");
  grid on;
endfunction
