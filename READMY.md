
PyAts_training

Repository is created for studying PyAts framework.

Before you can run the code from current repo you have to have a python 3+ installed, pyats shoud be installed as well.

You can use the next command: pip install -r requirements

In the requirements file placed all needed packeges.




Pyats-05

First pull image using the next command:
docker pull aquariumman/one
After that run docker with the command:
sudo docker run -it -v $(pwd)/archive:/my-tests/archive aquariumman/one && sudo chmod 777 -R archive/


