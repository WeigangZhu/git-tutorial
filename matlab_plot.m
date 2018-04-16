%% 工作环境初始化
close all  % 关闭所有的图像
clear,clc  % 清空变量及命令历史

%% 数据及初始设置
CAN_SPEED = [5, 10, 20, 50, 100,125, 250, 500, 1000]; % Kbps
CAN_LENGTH = [10000, 6700, 3300, 1300, 620, 530, 270, 130, 40]; % m

font_size = 12; % 设置字体大小
font_name = 'Times New Roman'; % 设置某个字体

%% 创建图形，并设定大小
% CAN_LENGTH = CAN_LENGTH/1000
f = figure(1);
f.Units = 'centimeters'; % 设置图片距离度量单位
% 还可以是pixel，inches等等

f.Position = [5, 2, 16, 8]; % 前两个设置图片出现的位置，后两个设置图片像素大小
f.Color = [0.95, 0.95, 0.95]; % 画布颜色，越大越白，最大为1
% f.Visible = 'off'; % 当前图像是否显示

%% 画图
p1 = plot(CAN_LENGTH,CAN_SPEED*5, 'b--','LineWidth',2);
hold on
p2 = plot(CAN_LENGTH,CAN_SPEED, 'r-.','LineWidth',2);
p3 = plot(CAN_LENGTH,CAN_SPEED*3, 'g','LineWidth',2);

%% 设置图形属性
% f.Children ==  f.CurrentAxes % 这两个等同
% f.Children 设置整个图片的属性

f.Children.FontSize = font_size;
f.Children.FontName = font_name;
fc = f.CurrentAxes; % 获得属性，等同于取个别名，推荐用这个

%% Label 属性
f.Children.XLabel.String = '总线长度(m)'; % 设置xlabel
f.Children.XLabel.FontName = '宋体';      % 设置xlabel的字体
f.Children.XLabel.FontSize = font_size;   % 设置xlabel的字体大小

fc.YLabel.String =  '$speed(Kbps)$'; % 用latex解释的字体需要加$限定范围
fc.YLabel.FontName = 'Fraktur';  % 花体字
fc.YLabel.FontSize = font_size;
fc.YLabel.Interpreter = 'latex'; % 用latex解释String
fcy = fc.YLabel;
fcy.FontWeight = 'bold';
fc.YLim = [0 6000];
fc.YTick = [0 2000 4000 6000]; % 坐标轴刻度
fc.YTickLabel = {'0','2000', '4000', '6000'}; % 坐标轴刻度标签
fc.YColor = [0 0 0 ];  % 表示黑色

%% legend属性
L = legend('data1','data2','data3'); % legend初始化

L.FontName = font_name; % legend 字体
% L.String = {'data1','data2','data3'}; % legend名称
p2.HandleVisibility = 'off';% 某个数据是否选择显示legend

% 表示图例的最佳位置
L.Location = 'best';

 % legend位置，四个值都在0~1范围内，都以整个图片为比例
 % 前两个表示图例位置，后两个表示图例大小
 % 位置以左上角为[0, 0]
L.Position = [0.72 0.7837 0.15 0.1283];

%% 网格属性
fc.YGrid = 'off'; % Y轴网格关闭
fc.XMinorGrid = 'on'; % 细网格
grid on % 打开所有网格