% The edge detection algorithum is used for detecting horizontal and 
% verical edges of an image. 
% This operation is also refers as the concolution Layer operation
% in Convolutional Neural networks (CNN's)

% clearing the command window
clc
% clearing workspace
clear all

% input image and Processing
img = imread('C:\Users\A\Downloads\.jpg');
[m n] = size(img);
img = imresize(img,[m,m]);
img = rgb2gray(img);
img1=img;
img = double(img);

% filter selection (horizontal/veritcal)
v = input('which filter you wnat to use(h/v) : ','s')
if(v=='v')
    filter = [1,0,-1;1,0,-1;1,0,-1];
elseif(v=='h')
    filter = [1,1,1;0,0,0;-1,-1,-1];
end

% creating random images
s = m-length(filter)+1;
pro_img = 255*ones(s,s)

% edge detection operaion
for j=1:1:s
    for i=1:1:s
       pro_img(i,j) = sum(sum(img(i:i+2,j:j+2).*filter));
    end
end

disp('INPUT IMAGE SIZE : ')
fprintf('%d %d\n',m,n)
disp('OUTPUT IMAGE SIZE : ')
fprintf('%d %d',size(pro_img))

pro_img = pro_img/255;

% displaying outputs
figure,imshow(pro_img)
figure,imshow(img1)

% storing outputs
op = input('Do you want to save(y/n) : ','s');
if(op=='y')
    folder = 'E:\programming\ML';
    imwrite(pro_img,fullfile(folder,'conv1.jpg'))
else
    disp('ok....')
end
