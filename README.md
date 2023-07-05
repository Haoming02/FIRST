# FIRST - **F**rame **I**nterpolation **R**efined with **S**table diffusion via control **N**et

## Abstract
##### Problem Statement
Traditional frame interpolation techniques were mainly trained on the motions and colors of pixels.
As such, they work better for frames with relatively little difference in between. When the difference is too significant,
the estimations become unreliable, and the algorithms essentially start guessing,
resulting in ghosting artifacts that people usually associate with frame interpolation.

##### Proposed Solution
**Stable Diffusion**, on the other hand, is a generative model capable of creating more coherent pixels instead of artifacts.
By combining the newly introduced `reference_only` module from **ControlNet**, which influences the generated result with provided references as the name implies,
and the `img2img` feature from Stable Diffusion, you can refine the interpolated frame and generate a more cohesive result.

## Sample Images
> The following base interpolated frames were generated using [Flowframes](https://github.com/n00mkrad/flowframes) with the [RIFE](https://github.com/megvii-research/ECCV2022-RIFE) model

<table>
    <thead align="center">
        <tr>
            <td><b>Previous Frame</b></td>
            <td><b>Base</b></td>
            <td><b>F.I.R.S.T</b></td>
            <td><b>Next Frame</b></td>
        </tr>
    </thead>
    <tbody align="center">
        <tr>
            <td><img src="sample/215.jpg" width=384></td>
            <td><img src="sample/216.jpg" width=384></td>
            <td><img src="sample/216s.jpg" width=384></td>
            <td><img src="sample/217.jpg" width=384></td>
        </tr>
        <tr>
            <td><img src="sample/217.jpg" width=384></td>
            <td><img src="sample/218.jpg" width=384></td>
            <td><img src="sample/218s.jpg" width=384></td>
            <td><img src="sample/219.jpg" width=384></td>
        </tr>
    </tbody>
</table>

<p align="center"><b><i>These screenshots were used solely for academic purposes</i></b></p>

> Sample Videos Coming Soon...

## Code
***Coming Soon...***

I only used existing projects to accomplish this. You can also achieve this on your own for free.
I am simply developing a simple script that includes a user interface to streamline this process.