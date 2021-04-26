# Gaussian Noise

> AUthor : Ya Chen<br>
> Date : 2021 / 4 / 26

---

<br>
<div>

## Description

1. Create an image g(x,y) whose pixels all have the same gray value of 100. Show the image g(x,y).
2. Generate Gaussian noise n(x,y), with <b>μ = 0, σ<sup>2</sup> = 15,</b> using the algorithm shown following.<br>

> ### Algorithm : Generation of zero mean Gaussian noise
>
> 1.  Suppose an image has gray-level range |0, G-1|. Select σ > 0;
> 2.  For eah pair of horizontally neighboring pixels (x, y), (x, y+1) generate a pair of uniform random numbers γ, φ in the range [0, 1].
> 3.  Calculate z<sub>1</sub> = σ _ cos(2πφ) _ sqrt(-2 _ ln γ), &emsp;z<sub>2</sub> = σ _ sin(2πφ) _ sqrt(-2 _ ln γ)
> 4.  Set f'(x, y) = g(x, y) + z<sub>1</sub> and f'(x, y+1) = g(x, y+1) + z<sub>2</sub>, where g is the input image.
> 5.  Set &emsp;&emsp;&emsp;| = 0 &emsp;&emsp; if f'(x, y) < 0,<br> >&emsp;&emsp;f(x, y) | = G -1 &emsp;if f'(x, y) > G - 1, <br> >&emsp; &emsp; &emsp;&emsp;| = f'(x, y)&emsp;otherwise<br><br> >&emsp; &emsp; &emsp; &emsp;&emsp;| = 0 &emsp;&emsp; if f'(x, y+1) < 0,<br> >&emsp;&emsp;f(x, y+1) | = G -1 &emsp;if f'(x, y+1) > G - 1, <br> >&emsp; &emsp; &emsp; &emsp;&emsp;| = f'(x, y+1)&emsp;otherwise<br>
>     Show the noisy image f(x,y) = g(x,y) + n(x,y).<br>
> 6.  Go to 3 until all pixels have been scanned.

3. Display the histogram h(i) of f(x,y).
4. Comment on your results.

</div>
<br>
<br>
<div>

## In-Output Example

### Input:

&emsp;&emsp; Original Image :<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "pictures/gray_100_image.jpg" width = "200">

### Output:

&emsp;&emsp; Image-generated-by-Gaussian-noise :<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "pictures/Image-generated-by-Gaussian-noise.jpg" width = "200">

&emsp;&emsp; Histogram-of-image-generated-by-Gaussian-noise :<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
<img src = "pictures/Histogram-of-image-generated-by-Gaussian-noise.png" width = "200">

</div>
