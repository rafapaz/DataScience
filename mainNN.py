
import mnist_loader
import Network as NN

print("Loading data...", end="", flush=True)
training_data, validation_data, test_data =  mnist_loader.load_data_wrapper()
print("DONE")

print("Training data...")
net = NN.Network([784, 30, 10])
net.SGD(training_data, 20, 10, 3.0, test_data=test_data)
print("DONE")

while True:
    press = input('Press any char to predict images 0.png to 9.png and q to exit:')
    if (press[0] == 'q'):
        break
    
    for i in range(10):
        print("Image {0}.png is number {1}".format(i, net.predict("{0}.png".format(i))))