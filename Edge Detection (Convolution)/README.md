Algorithum : 
==================================
Edge detection is an image processing technique for finding the boundaries of objects within images. It works by detecting discontinuities in brightness and significant changes in image. The approch of edge detection was inspired from the approch of Convolutional layer in Deep Learning with multiple filters. Use of Different filters leads Different outputs. We have already mention the results achived from both horizintal and vertical filter, even the use of different strides leads to different outcomes.

<p align = 'center'>
<img src = "https://miro.medium.com/max/700/1*TAo3aselJNVwrLLr654Myg.gif", width = 500>  
</p>

Advantages : 
==================================
- Feature Extraction
- Down-Sampling
- Image Classification
- Object Localization

Steps : 
==================================
- Select the Subject image for operation
- Use the below formula for output Dimention Selection 

<p align = 'center'>
<img src = "https://miro.medium.com/max/258/1*HoOLVDujrz1TKJJ6ijR6Bw.gif", width = 400>  
</p>

- Decide the appropriate kernel for better output
- Perform the element wise multiplication of every block as shown : 

<p align = 'center'>
<img src = "https://miro.medium.com/max/2560/1*ciDgQEjViWLnCbmX-EeSrA.gif", width = 640>  
</p>

Conclusion : 
===================================
The achived results can be shown Below:
<p align = 'center'>
<img src = "https://raw.githubusercontent.com/rawat126/Algorithums/master/Edge%20Detection%20(Convolution)/edge_Detection_test.jpg", width = 600>  
</p>
