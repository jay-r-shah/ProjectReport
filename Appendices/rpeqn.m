%Filename rpeqn.m
%Defining Rayleigh Plesset equation as a system of first order odes
function drdt=rpeqn(t,R)
global rho P0 sig R0 gamma mu Pinf;
drdt=[R(2);(1/R(1))*(1/rho)*((P0+5000000*sin(2*pi*20000*t)+(2*sig/R0))*(R0/R(1))^(3*gamma)-2*sig/R(1)-4*mu*R(2)/R(1)-Pinf)-(3/2)*R(2)^2];