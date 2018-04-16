%% ����������ʼ��
close all  % �ر����е�ͼ��
clear,clc  % ��ձ�����������ʷ

%% ���ݼ���ʼ����
CAN_SPEED = [5, 10, 20, 50, 100,125, 250, 500, 1000]; % Kbps
CAN_LENGTH = [10000, 6700, 3300, 1300, 620, 530, 270, 130, 40]; % m

font_size = 12; % ���������С
font_name = 'Times New Roman'; % ����ĳ������

%% ����ͼ�Σ����趨��С
% CAN_LENGTH = CAN_LENGTH/1000
f = figure(1);
f.Units = 'centimeters'; % ����ͼƬ���������λ
% ��������pixel��inches�ȵ�

f.Position = [5, 2, 16, 8]; % ǰ��������ͼƬ���ֵ�λ�ã�����������ͼƬ���ش�С
f.Color = [0.95, 0.95, 0.95]; % ������ɫ��Խ��Խ�ף����Ϊ1
% f.Visible = 'off'; % ��ǰͼ���Ƿ���ʾ

%% ��ͼ
p1 = plot(CAN_LENGTH,CAN_SPEED*5, 'b--','LineWidth',2);
hold on
p2 = plot(CAN_LENGTH,CAN_SPEED, 'r-.','LineWidth',2);
p3 = plot(CAN_LENGTH,CAN_SPEED*3, 'g','LineWidth',2);

%% ����ͼ������
% f.Children ==  f.CurrentAxes % ��������ͬ
% f.Children ��������ͼƬ������

f.Children.FontSize = font_size;
f.Children.FontName = font_name;
fc = f.CurrentAxes; % ������ԣ���ͬ��ȡ���������Ƽ������

%% Label ����
f.Children.XLabel.String = '���߳���(m)'; % ����xlabel
f.Children.XLabel.FontName = '����';      % ����xlabel������
f.Children.XLabel.FontSize = font_size;   % ����xlabel�������С

fc.YLabel.String =  '$speed(Kbps)$'; % ��latex���͵�������Ҫ��$�޶���Χ
fc.YLabel.FontName = 'Fraktur';  % ������
fc.YLabel.FontSize = font_size;
fc.YLabel.Interpreter = 'latex'; % ��latex����String
fcy = fc.YLabel;
fcy.FontWeight = 'bold';
fc.YLim = [0 6000];
fc.YTick = [0 2000 4000 6000]; % ������̶�
fc.YTickLabel = {'0','2000', '4000', '6000'}; % ������̶ȱ�ǩ
fc.YColor = [0 0 0 ];  % ��ʾ��ɫ

%% legend����
L = legend('data1','data2','data3'); % legend��ʼ��

L.FontName = font_name; % legend ����
% L.String = {'data1','data2','data3'}; % legend����
p2.HandleVisibility = 'off';% ĳ�������Ƿ�ѡ����ʾlegend

% ��ʾͼ�������λ��
L.Location = 'best';

 % legendλ�ã��ĸ�ֵ����0~1��Χ�ڣ���������ͼƬΪ����
 % ǰ������ʾͼ��λ�ã���������ʾͼ����С
 % λ�������Ͻ�Ϊ[0, 0]
L.Position = [0.72 0.7837 0.15 0.1283];

%% ��������
fc.YGrid = 'off'; % Y������ر�
fc.XMinorGrid = 'on'; % ϸ����
grid on % ����������