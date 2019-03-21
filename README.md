# NB TTY
### Web :globe_with_meridians: terminal :computer: for jupyter notebooks :notebook:.

Today many cloud services provide jupyter notebooks as a service to users, e.g. Google colab, Kaggle Kernel, Microsoft Azure Notebooks ... These services are great, easy to use, people do not have to install jupyter, CUDA, or GPU driver themselves. However without access to the shell, my data science workflow is quite inefficient because I use commandline heavily.

So I create this little tool.  It starts a web shell (gotty) locally and exposes the shell to the ngrok. Then you can use the in  the browser, gotty is pretty powerful and the user experience is very similar to the real terminal.

## Usage
1. Install nbtty inside a jupyter notebook like other Python packages:
```
！pip install nbtty
```

3. Start the web tty, it will print the url of the web shell when service is ready:
```python
from nbtty import TTY
TTY().start()
```
## Screenshots
![alt text](https://github.com/glasslion/nbtty/raw/master/assets/images/Screenshot_20190321_174407.png)
![alt text](https://github.com/glasslion/nbtty/raw/master/assets/images/Screenshot_20190321_174544.png)
![alt text](https://raw.githubusercontent.com/glasslion/nbtty/master/assets/images/Screenshot_20190321_174627.png)

## Acknowledgments
- ngrok
- [gotty](https://github.com/yudai/gotty)
