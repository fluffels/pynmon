#!/usr/bin/gnuplot

set title "Time versus Transfer Rate"
set xlabel "Time (s)"
set ylabel "KB/s"
set timefmt '%Y-%m-%d %H:%M:%s'
set xdata time

set output "graph.png"

plot "out.dat" using 0:1