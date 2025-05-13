function [values, rejected] = gammaDistribution(n)
  shape = 7.5;
  scale = 1.0;
  x_min = 0;
  x_max = 20;

  density = @(x) gampdf(x, shape, scale);
  x_vals = linspace(x_min, x_max, max(1000, n));
  max_density = max(density(x_vals));

  values = zeros(1, n);
  count = 0;
  rejected = 0;

  while count < n
    x = x_min + (x_max - x_min) * rand;
    y = max_density * rand;

    if y <= density(x)
      count += 1;
      values(count) = x;
    else
      rejected += 1;
    end
  end
endfunction
