package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("I need a file as the first argument...exiting...")
		os.Exit(1)
	}
	file, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Println("Error reading file:", err)
		os.Exit(2)
	}

	_, err = io.Copy(os.Stdout, file)
	if err != nil {
		fmt.Println("Some error reading file:", err)
	}
}
