function main()
  % 1000, 5000 or 10000
  n = 10000;

  [data, rejected] = gammaDistribution(n);
  p_title = strcat("Gamma  Distribution. N=", num2str(n));

  % Plots
  drawHist(data, p_title);
  drawEmpiricalDistributionFunc(data, p_title);
  drawPlanarDistribution(data, p_title);

  % Stats
  printStats(data, rejected, p_title);
endfunction
