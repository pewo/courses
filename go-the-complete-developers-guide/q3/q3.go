package main

import (
	"fmt"
)

func main3() {
	greeting := "Hi There!"

	go (func() {
		fmt.Println(greeting)
	})()
}
