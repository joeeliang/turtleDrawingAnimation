import imageio

def pngToVideo (pngDirectory, fps, totalFrames):
    # List PNG files in the directory
    png_files = [f"{pngDirectory}/animation{i}.png" for i in range(1, totalFrames)]

    # Create MP4 video using imageio
    with imageio.get_writer("output.mp4", mode="I", fps=fps) as writer:
        for png_file in png_files:
            image = imageio.imread(png_file)
            writer.append_data(image)