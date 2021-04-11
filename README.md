### Rafaela2.0

Same old dog, with different trick.

I love experimenting with my two wheel robot. But here´s the annoying thing, every time I need to change her behavior, I should plug her butt to my computer and upload the code. It´s bad for the microcontroller lifetime, as it has limited write cycle.

So, I came up with a clever idea: why don´t I just leave the microcontoller with basic commands like moving a wheel, get sonar data, etc. Sending and receiving data/commands from my computer, all through bluetooth module. So, the robot is just a body. My laptop does the heavy things, my laptop is the one that thinks. That way, if I want to update something, all I need to do is to edit the code in my laptop. I don´t have to touch the robot. With any programming language I want, as long as it supports bluetooth communication.