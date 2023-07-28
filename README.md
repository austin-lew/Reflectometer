# Reflectometer
## Motivation
Reflective surfaces are difficult to characterize due to the inconsistency of the image being reflected. We therefore want a way to identify how reflective a surface is, reliably and accurately.

## Description
A custom implementation of the Canny edge detection algorithm with interpolated non-max suppression and automatic threshold generation. 

## Advantages over OpenCV
Suppose we wish to determine the Canny threshold values such that 5% of an image contained detected edges. Using OpenCV's library, this would require performing the entire algorithm multiple times at different threshold values. This is incredibly inefficient as subtasks such as the Sobel operation and non-max suppression yield identical results regardless of threshold. 
This custom implementation allows for such threshold values to be determined without the need to perform identical tasks multiple times, significantly reducing processing time.
