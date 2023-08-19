import turtle
import subprocess

def convert_eps_to_png(eps_path, png_path, dpi=200):
    gs_command = [
        "gs",
        "-dNOPAUSE", "-dBATCH", "-dSAFER",
        "-sDEVICE=pngalpha", "-dEPSCrop",
        f"-r{dpi}",
        f"-sOutputFile={png_path}",
        eps_path
    ]
    # Run Ghostscript command
    subprocess.run(gs_command)

def save(counter=[1]):
    turtle.getscreen().getcanvas().postscript(file = "animation{}.eps".format(counter[0]))
    convert_eps_to_png("animation{}.eps".format(counter[0]), "animation{}.png".format(counter[0]))
    counter[0] += 1