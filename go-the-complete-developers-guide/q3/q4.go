package main

func main4() {
	c := make(chan string)
	c <- []byte("Hi there!")
}
