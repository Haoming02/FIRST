# FIRST - **F**rame **I**nterpolation **R**efined with **S**table diffusion via control ne**T**

<h5 align="center">Problem Statement</h5>

Traditional frame interpolation techniques were mainly trained on the motions and colors of pixels.
As such, they work better for frames with relatively little difference in between. When the difference is too significant,
the estimations become unreliable, and the algorithms essentially start guessing,
resulting in ghosting artifacts that people usually associate with frame interpolation.

<h5 align="center">Proposed Solution</h5>

**Stable Diffusion**, on the other hand, is a generative model capable of creating more coherent pixels instead of artifacts.
By combining the newly introduced `reference_only` module from **ControlNet**, which influences the generated result with provided references as the name implies,
and the `img2img` feature from Stable Diffusion, you can refine the interpolated frame and generate a more cohesive result.

## Sample Images
> The following base interpolated frames were generated using [Flowframes](https://github.com/n00mkrad/flowframes) with the [RIFE](https://github.com/megvii-research/ECCV2022-RIFE) model

<table>
    <thead align="center">
        <tr>
            <td><b>Previous Frame</b></td>
            <td><b>RIFE</b></td>
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

## Sample Videos

<h5 align="center">RIFE</h5>
<p align="center"><img src="sample/RIFE.gif"></p>

<h5 align="center">F.I.R.S.T</h5>
<p align="center"><img src="sample/FIRST.gif"></p>

<p align="center"><b><i>Above contents were used solely for research purposes</i></b></p>

## Code
A simple Python GUI that streamlines this process

#### Prerequisite
- [Automatic1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) Webui
- [sd-webui-controlnet](https://github.com/Mikubill/sd-webui-controlnet) Extension
- (Highly Recommended) [FFmpeg](https://ffmpeg.org/)

#### How to Use
0. In the settings of Automatic1111, set `Multi ControlNet: Max models amount` to `2` or above
    - Recommended to set `Model cache size` to `2` as well
1. Launch Automatic1111 with `api` enabled
    - Open the `webui-user.bat` and add `--api` after `COMMANDLINE_ARGS=`
    - Set your checkpoint accordingly *(Realistic / Anime)*
2. **(Optionally)** Edit `parameters.py` to change the Stable Diffusion settings, such as `steps` or `sampler`
3. Launch `main.py` to open the GUI
    - On Windows, you can just use `launch.bat`
    
4. Enter the path containing the frames
    - The path should contain both the original and the interpolated frames in sequence *(Default behavior of `Flowframes` when you set the export to `Image Sequence`)*
    - Only supports **2x** interpolations, meaning the odd files should be original frames while even files should be interpolated frames
5. Enter the path to store the outputs
    - Recommended to set a different path from Source
6. Enter the port 
    - The default is `7860`
7. Press **Run**
8. Check the console for progress
9. Use `FFmpeg` to merge the frames into video
