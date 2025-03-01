function drawHist(data, p_title)
  figure();
  hist(data);
  title(p_title);
  xlabel("Value");
  ylabel("Frequency");
  grid on;
endfunction

