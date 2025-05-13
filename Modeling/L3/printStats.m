function printStats(data, p_title)
  fprintf(strcat("\n", p_title, "\n"));
  fprintf("Mean: %d\n", mean(data));
  fprintf("Var:  %d\n", var(data));
  fprintf("Std:  %d\n\n", std(data));
endfunction

