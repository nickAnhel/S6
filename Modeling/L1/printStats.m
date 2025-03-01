function printStats(data, p_title)
  fprintf(strcat(p_title, "\n"));
  fprintf("Mean: %d\n", mean(data));
  fprintf("Var:  %d\n", var(data));
  fprintf("Std:  %d\n", std(data));
endfunction
