

function main()
  % "mcg", "fibbonacci" or "mersenne"
  alg = "mersenne";

  % 1000, 5000 or 10000
  n = 10000;

  switch alg
    case "mcg"
      data = multiplicativeCongruenceGenerator(n);
      p_title = strcat("Multiplicative Congruence Generator. N=", num2str(n));
    case "fibbonacci"
      data = laggedFibbonacci(n);
      p_title = strcat("Lagged Fibbonacci. N=", num2str(n));
    case "mersenne"
      data = mersenneTwister(n);
      p_title = strcat("Mersenne Twister. N=", num2str(n));
  endswitch

  drawHist(data, p_title);
  drawEmpiricalDistributionFunc(data, p_title);
  drawPlanarDistribution(data, p_title);
  printStats(data, p_title);
endfunction

