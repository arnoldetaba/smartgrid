[Demo](https://www.youtube.com/watch?v=7btvw_rZboU)

### Installation

smartgrid requires [Python3](https://www.python.org/downloads/) to run.

##### Server
Install the dependencies and  start the server.

```sh
$ cd smartgrid
$ pip3 install -r requirements.txt
$ cd GridControlUnit
$ python3 ./GridController.py
```
start the matplotlib graph dashboard on server side
```sh
$ cd smartgrid
$ python3 ./graph.py
```

Controlling clients,
from the server prompt, operator can type help
and get access to list commands used to control
devices remotely.
```sh
(command)> help
```

#### Client
Install the dependencies
```sh
$ cd smartgrid
$ pip3 install -r requirements.txt
```
Configure the client

Open **Home/Home.py** with your preferred text editor
and edit CU_IP to contain the IP address of your server



![image.png](./image.png)

Run client,
```sh
$ cd Home
$ python3 ./Home.py
```

Client can be run independently of server code in any machine
of the network.

Server supports multiple clients connecting to it


### Issues
You may encounter the following errors

#### 1. Agg backend problem

```sh
$ python3 graph.py
graph.py:149: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
  plt.show()
```

Solution:

#### Ubuntu
https://stackoverflow.com/questions/56656777/userwarning-matplotlib-is-currently-using-agg-which-is-a-non-gui-backend-so
```sh
$ sudo apt-get install python3-tk
```

#### Fedora
```sh
$ sudo dnf install -y python3-tkinter
```


