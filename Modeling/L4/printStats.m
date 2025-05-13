function printStats(data, rejected, p_title)
  fprintf(strcat("\n", p_title, "\n"));
  fprintf("Mean: %d\n", mean(data));
  fprintf("Var:  %d\n", var(data));
  fprintf("Std:  %d\n", std(data));
  fprintf("Rejected: %d\n\n", rejected);
endfunction

