# PongAI

Using the NEAT algorithm in order to train a "Pong" artificial intelligence. <br/>

## Description

The project architecture can be modeled as so: <br/>
![Pong](https://user-images.githubusercontent.com/80195693/136804292-5a95ec92-27a0-4961-b033-6477841cd1e1.png)
* The pongGame directory implements everything to do with the gaming platform. <br/>
* The pongAI directory implements the learning NEAT algorithm. <br/>

## Getting Started

### Dependencies

* all of the dependencies are described in the requirements.txt file.

### Installing

* you can clone the project via the clone link.

### Executing program
start.py file is responsible for running the project. <br/>
* To run the project with a trained model:
```
if __name__ == '__main__':
    main()
```
* To test a trained model:
```
if __name__ == '__main__':
    AI.test()
```
* To train a new model:
```
if __name__ == '__main__':
    AI.train()
```



## Author
Ofek Ophir
