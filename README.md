# NB TTY
### Web :globe_with_meridians: terminal :computer: for jupyter notebooks :notebook:.

Today many cloud services provide jupyter notebooks as a service to users, e.g. Google colab, Kaggle Kernel, Microsoft Azure Notebooks ... These services are great, easy to use, people do not have to install jupyter, CUDA, or GPU driver themselves.

However without access to the shell, 


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
