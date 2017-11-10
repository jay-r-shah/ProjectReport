%Filename rpsoln.n
%Solving the differential equation rpeqn.m
clc
clf
clear
format('long')
global rho P0 sig R0 gamma mu Pinf;
rho=1000;
P0=10000000;
sig=72*0.001;
R0=2*10^(-8);
gamma=1.4;
mu=10^(-3);
Pinf=100000;
Ri=[2*sig/(P0-Pinf);0];
time=[0,0.0003];
[t,R]=ode15s(@rpeqn,time,Ri);
plot(t,R(:,1));
xlabel('time (s)');
ylabel('bubble radius (m)');