# Using Python with LabVIEW

Python 3.6 32-bit version seems to be compatible with most versions of LabVIEW.

The bit version for Python and LabVIEW need to be the same. There is an in-built VI that lets us find the LabVIEW bit version. It can also be read off of the start-up window when LabVIEW is opened for the first time. When installing Python, select the "Add to PATH" option on the installer. Open the Windows Command Prompt and check the version by `python --version` and it should read 3.6.x. It should also read the bit number.

Install packages using pip on cmd, example `pip install numpy` to install numpy.

[LV_vs_PY_timing.vi](https://github.com/murthysindhu/CMU_LabVIEW/blob/main/LabVIEW_w_Python/LV_vs_PY_timing.vi) file performs a sample array calculation from Find_component_center.vi and displays the execution time for calculations performed directly on LV and via python. Clicking on the STOP button displays any errors that might have occured when running the python code. The python module path needs to be modified on the front panel based on the location of the [test_python.py](https://github.com/murthysindhu/CMU_LabVIEW/blob/main/LabVIEW_w_Python/test_python.py) file. The fiducials input array loaction also needs to be modified on the front panel based on the location of the [fiducials.txt](https://github.com/murthysindhu/CMU_LabVIEW/blob/main/LabVIEW_w_Python/fiducials.txt) file.

In general, Python gets opened in the directory where the LabVIEW file is located. Any files called in the Python script need to have paths relative to this directory.
